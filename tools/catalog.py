"""App- und Spielekatalog – eine Datenquelle für DE und EN, für Startseite und Katalogseite.
python3 tools/catalog.py schreibt den Streifen „Jetzt verfügbar“ in index.html (zwischen den katalog-Markern)
und baut die Katalogseite apps/index.html; tools/build_en.py baut daraus en/index.html und en/apps/index.html.
Store-Links nur eintragen, wenn die Store-Seite live ist (alle Stores geprüft 09.11.2026, siehe docs/LIVE_STATUS.md)."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://minh.systems/MinhNguyenStudios/"
S = "https://minh.systems/"
APPLE = "https://apps.apple.com/app/id"
MS = "https://apps.microsoft.com/detail/"
PLAY = "https://play.google.com/store/apps/details?id="

CATS = [
 ("spiele", "Spiele", "Games"),
 ("ordnung", "Ordnung &amp; Dateien", "Organising &amp; files"),
 ("finanzen", "Finanzen &amp; Belege", "Money &amp; receipts"),
 ("lernen", "Lernen &amp; Alltag", "Learning &amp; everyday"),
 ("kinder", "Für Kinder", "For kids"),
]
NOTE = {"finanzen": ("Zum Erfassen und Ordnen – keine Finanz- oder Steuerberatung.",
                     "For recording and organising – no financial or tax advice.")}

# id, Name, Kategorie, Plattformen, verfügbar?, Website, Stores [(Art, URL)], DE, EN
APPS = [
 ("shelterfall", "Shelter Fall", "spiele", ["iPhone"], True, "https://shelterfall.minh.systems/", [("apple", APPLE+"6759238842")],
  "Endzeit-Strategie mit Ereignissen und wachsendem Überlebensdruck.", "Post-apocalyptic strategy with events and rising survival pressure."),
 ("nomad", "Nomad Kitchen Tycoon", "spiele", ["iPhone", "Android"], True, S+"NomadKitchenTycoon/", [("apple", APPLE+"6759504817"), ("play", PLAY+"com.minhstudios.nomadkitchen")],
  "Foodtruck-Management in zwei Städten.", "Food truck management across two cities."),
 ("ringjahr", "Ringjahr", "spiele", ["iPhone"], False, S+"Ringjahr/", [],
  "Ruhiges Puzzle über Baumringe und Klima.", "A calm puzzle about tree rings and climate."),
 ("signallost", "Signal Lost", "spiele", ["iPhone"], False, S+"SignalLost/", [],
  "Funkstationen bauen und die Verbindung durch die Wildnis wiederherstellen.", "Build relay stations and restore communication across the wilderness."),
 ("cogwisp", "Cogwisp", "spiele", ["Windows"], True, S+"Cogwisp/", [("ms", MS+"9NSRPBK9PL5N")],
  "Entspannte Zahnrad-Rätsel ohne Werbung.", "Relaxing gear puzzles without ads."),
 ("littlekeepings", "Little Keepings", "spiele", ["Windows"], True, S+"LittleKeepings/", [("ms", MS+"9N1WQT29BF8W")],
  "Ruhiges Sortierrätsel ohne Zeitdruck.", "A calm sorting puzzle with no timer."),
 ("folvane", "Folvane", "ordnung", ["Windows"], True, S+"Folvane/", [("ms", MS+"9NSDC58HLFRR")],
  "Ordner vergleichen, synchronisieren und Backups prüfen – mit Vorschau und Rückgängig.", "Compare and sync folders and check backups – with preview and undo."),
 ("pathrova", "Pathrova", "ordnung", ["Windows"], True, S+"Pathrova/", [("ms", MS+"9NJN21Z01WPM")],
  "Findet zu lange Pfade und ungültige Namen, bevor du nach OneDrive oder SharePoint synchronisierst.", "Finds overly long paths and invalid names before you sync to OneDrive or SharePoint."),
 ("ablagefuchs", "Ablagefuchs", "ordnung", ["Windows"], False, None, [],
  "Verträge, Rechnungen und Schreiben an einem Ort – mit Texterkennung und Fristen, offline.", "Contracts, invoices and letters in one place – with text recognition and deadlines, offline."),
 ("fotokehr", "SafeSort Photos", "ordnung", ["Windows"], False, S+"SafeSort-Photos/", [],
  "Fotos und Videos lokal nach Datum sortieren – Originale bleiben unverändert.", "Sort photos and videos by date, locally – originals stay untouched."),
 ("plauderbuch", "Chatbound", "ordnung", ["Windows"], True, S+"Chatbound/", [("ms", MS+"9PJV28CQJV8K")],
  "Exportierte Chats durchsuchen, zusammenführen und als Buch-PDF setzen – lokal, ohne Konto.", "Search and merge exported chats and set them as a book PDF – local, no account."),
 ("appsweep", "AppSweep", "ordnung", ["Mac"], True, S+"AppSweep/", [],
  "Findet Updates für deine Mac-Apps und öffnet die offiziellen Update-Links.", "Finds updates for your Mac apps and opens the official update links."),
 ("diskloom", "DiskLoom", "ordnung", ["Mac"], True, S+"DiskLoom/", [],
  "Laufwerksgesundheit, Langzeittrends und Time-Machine-Bereitschaft am Mac.", "Drive health, long-term trends and Time Machine readiness on the Mac."),
 ("shotsift", "ShotSift", "ordnung", ["iPhone"], True, S+"ShotSift/", [("apple", APPLE+"6758222349")],
  "Fotos aufräumen – Duplikate, Screenshots und Serien, alles auf dem Gerät.", "Tidy your photos – duplicates, screenshots and bursts, all on-device."),
 ("erechnung", "E-Rechnung Viewer", "finanzen", ["Windows"], False, S+"erechnung/", [],
  "XRechnung und ZUGFeRD lesbar anzeigen und nach den offiziellen Regeln prüfen, offline.", "View XRechnung and ZUGFeRD invoices and validate them against the official rules, offline."),
 ("monatsklar", "Monatsklar", "finanzen", ["Windows"], True, S+"Monatsklar/", [("ms", MS+"9N6JM2J3LC27")],
  "Haushaltsbuch für Windows – offline und ohne Abo.", "Household budget book for Windows – offline, no subscription."),
 ("belegora", "Belegora", "finanzen", ["Windows"], True, S+"belegora/", [("ms", MS+"9NB7QSNC6MJQ")],
  "Belege, Geräte und Garantiefristen an einem Ort, offline.", "Receipts, devices and warranty dates in one place, offline."),
 ("tastenflink", "Tenfingo", "lernen", ["Windows"], False, S+"Tenfingo/", [],
  "Zehnfingerschreiben lernen – Schritt für Schritt, ohne Konto.", "Learn to touch-type – step by step, no account."),
 ("speakanchor", "SpeakAnchor", "lernen", ["Windows"], True, S+"SpeakAnchor/", [("ms", MS+"9PF13FM93XSJ")],
  "Teleprompter mit Redner-Timer, beim Teilen in Teams, Zoom und OBS nicht zu sehen.", "Teleprompter with speaker timer, not visible when sharing in Teams, Zoom or OBS."),
 ("vietnamese", "Chào nhà", "lernen", ["Browser"], True, S+"VietnameseTrainer/", [],
  "Freundlicher Browser-Trainer für vietnamesischen Alltag.", "A friendly browser trainer for everyday Vietnamese."),
 ("ridgefocus", "RidgeFocus", "lernen", ["iPhone"], True, S+"RidgeFocus/", [("apple", APPLE+"6758014649")],
  "Pomodoro-Timer für konzentriertes Arbeiten und Lernen.", "Pomodoro timer for focused work and study."),
 ("focusledger", "Focusledger", "lernen", ["Mac"], True, S+"Focusledger-Pro/", [],
  "Privater Fokus-Timer mit Zielen, Journal und Notizen für den Mac.", "A private focus timer with goals, journal and notes for the Mac."),
 ("nighttalk", "NightTalk", "lernen", ["iPhone"], False, S+"Nighttalk/", [],
  "Nächtliche Sprachereignisse privat auf dem Gerät festhalten und ansehen.", "Record and review nighttime voice events privately on your device."),
 ("rootling", "Rootling", "lernen", ["iPhone"], True, S+"Rootling/", [("apple", APPLE+"6758851487")],
  "Stecklinge bewurzeln – mit Prognosen und Pflanzentagebuch.", "Root cuttings – with forecasts and a plant journal."),
 ("mushbloom", "MushBloom", "lernen", ["iPhone"], True, "https://mushbloom.minh.systems/", [("apple", APPLE+"6758917023")],
  "Begleiter für die Pilzzucht zu Hause.", "A companion for growing mushrooms at home."),
 ("horsehold", "Horsehold", "lernen", ["iPhone"], True, S+"Stable/", [("apple", APPLE+"6826688753")],
  "Stallbuch fürs Pferd: Pflege, Termine und Dokumente.", "A stable book for your horse: care, appointments and documents."),
 ("summgarten", "Summgarten", "kinder", ["iPhone", "Mac", "Windows", "Android"], True, S+"Summgarten/", [("apple", APPLE+"6824160993"), ("ms", MS+"9PGTW423BB1H"), ("play", PLAY+"de.michelnguyen.klanggarten")],
  "Singender Garten für Kinder ab 3 – im Microsoft Store als Hum Garden.", "A singing garden for kids 3+ – called Hum Garden in the Microsoft Store."),
 ("reparierer", "Kleiner Reparierer", "kinder", ["Windows"], True, S+"KleinerReparierer/", [("ms", MS+"9N71QS2JNCVW")],
  "Mit Biber Bruno reparieren, putzen und anmalen – ohne Texte, ohne Scheitern.", "Fix, scrub and paint with Bruno the beaver – no reading, no failing."),
]

# Auswahl für den Streifen „Jetzt verfügbar“ auf der Startseite (nur Titel mit Store-Link; die großen Spiele stehen darüber)
FEATURED = ["shelterfall", "nomad", "cogwisp", "folvane", "monatsklar", "shotsift"]

L = {
 "de": dict(all="Alle", ok="Verfügbar", soon="In Arbeit", site="Website",
            kicker="Alles aus unserer Werkstatt", h2="Apps &amp; Spiele",
            lead="Kleine, private Werkzeuge und ruhige Spiele für Windows, iPhone, iPad, Android und Mac – ohne Konto, meist offline.",
            filter="Nach Bereich filtern", pfilter="Nach Gerät filtern", pfall="Alle Geräte",
            none="Für diese Auswahl gibt es noch nichts.",
            s_kicker="Apps &amp; Spiele", s_h2="Jetzt verfügbar",
            s_lead="Eine kleine Auswahl. Der ganze Katalog steht auf einer eigenen Seite – mit Filter nach Bereich und Gerät.",
            s_btn="Alle Apps &amp; Spiele ansehen", s_count="{n} verfügbare Titel für Windows, iPhone, iPad, Android und Mac",
            title="Apps &amp; Spiele – alle Titel von Minh Nguyen Studios", short="Apps &amp; Spiele – Minh Nguyen Studios",
            desc="Alle Apps und Spiele von Minh Nguyen Studios auf einen Blick – nach Bereich und Gerät filterbar, mit Links zu App Store, Google Play und Microsoft Store."),
 "en": dict(all="All", ok="Available", soon="In the works", site="Website",
            kicker="Everything from our workshop", h2="Apps &amp; games",
            lead="Small, private tools and calm games for Windows, iPhone, iPad, Android and Mac – no account, mostly offline.",
            filter="Filter by category", pfilter="Filter by device", pfall="All devices",
            none="Nothing for this selection yet.",
            s_kicker="Apps &amp; games", s_h2="Available now",
            s_lead="A small selection. The full catalogue has its own page – with filters for category and device.",
            s_btn="See all apps &amp; games", s_count="{n} available titles for Windows, iPhone, iPad, Android and Mac",
            title="Apps &amp; games – everything from Minh Nguyen Studios", short="Apps &amp; games – Minh Nguyen Studios",
            desc="All apps and games from Minh Nguyen Studios at a glance – filter by category and device, with links to the App Store, Google Play and the Microsoft Store."),
}
PF = {"de": {"iPhone": "iPhone &amp; iPad"}, "en": {"iPhone": "iPhone &amp; iPad"}}
FILTER_PF = ["iPhone", "Android", "Windows", "Mac"]
ORDER = {"apple": 0, "play": 1, "ms": 2}  # Apple zuerst (Regeln: README), dann Google Play, dann Microsoft


def badge(kind, lang):
    """Badge-Grafik, unverändert und überall 44 px hoch. Pfade relativ zur Startseite der Sprache."""
    if kind == "play":
        # Aktuelle, unveränderte Grafik aus Googles Partner Marketing Hub; mindestens so hoch wie die übrigen Badges.
        alt = {"de": "Jetzt bei Google Play", "en": "Get it on Google Play"}[lang]
        return f'<img src="brand/badges/google-play-{lang}.svg" alt="{alt}" width="148" height="44" loading="lazy">'
    if kind == "apple":
        src, w, alt = f"brand/badges/app-store-{lang}.svg", 132, {"de": "Laden im App Store", "en": "Download on the App Store"}[lang]
    else:  # Microsoft-Badge bleibt bei Microsoft gehostet
        src, w, alt = (("https://get.microsoft.com/images/de%20dark.svg", 183, "Download im Microsoft Store") if lang == "de"
                       else ("https://get.microsoft.com/images/en-us%20dark.svg", 161, "Get it from Microsoft"))
    return f'<img src="{src}" alt="{alt}" width="{w}" height="44" loading="lazy">'


def store_links(stores, lang):
    return "".join(f'<a class="badge" href="{u + "&amp;hl=" + lang if k == "play" else u}" target="_blank" rel="noopener">{badge(k, lang)}</a>'
                   for k, u in sorted(stores, key=lambda x: ORDER[x[0]]))


def site_url(site, lang):
    return site + "en/" if site and lang == "en" and site.startswith(S + "Summgarten") else site


def icon(key, name):
    if os.path.exists(os.path.join(ROOT, "img/icons", key + ".webp")):
        return f'<img class="ico" src="img/icons/{key}.webp" alt="" width="56" height="56" loading="lazy">'
    return f'<span class="ico mono" aria-hidden="true">{name[0]}</span>'


def card(a, lang):
    """Eine Regel für alle Karten: oben Icon, Name, Status, Geräte, Text; darunter über die ganze Kartenbreite
    die Store-Badges in einer Reihe (Apple, Google Play, Microsoft) und in einer eigenen Zeile der Website-Knopf."""
    key, name, cat, pfs, ok, site, stores, de, en = a
    t = L[lang]
    site = site_url(site, lang)
    title = f'<a href="{site}">{name}</a>' if site else name
    badges = "".join(f'<span class="pf">{PF[lang].get(p, p)}</span>' for p in pfs)
    st = f'<span class="st ok">{t["ok"]}</span>' if ok else f'<span class="st soon">{t["soon"]}</span>'
    go = (f'<div class="stores">{store_links(stores, lang)}</div>' if stores else "") + (f'<a class="more" href="{site}">{t["site"]} →</a>' if site else "")
    return (f'<article class="app{"" if ok else " wip"}" data-cat="{cat}" data-a="{key}" data-pf="{" ".join(pfs)}">{icon(key, name)}'
            f'<div><h3>{title}</h3><div class="badges">{st}{badges}</div><p>{de if lang == "de" else en}</p></div>'
            + (f'<div class="go">{go}</div>' if go else "") + '</article>')


def catalog(lang):
    """Ganzer Katalog mit Bereichs- und Gerätefilter – Inhalt der Katalogseite."""
    t = L[lang]
    chips = f'<button class="chip on" data-k="all" aria-pressed="true">{t["all"]}</button>' + "".join(
        f'<button class="chip" data-k="{k}" aria-pressed="false">{de if lang == "de" else en}</button>' for k, de, en in CATS)
    pchips = f'<button class="chip on" data-p="all" aria-pressed="true">{t["pfall"]}</button>' + "".join(
        f'<button class="chip" data-p="{p}" aria-pressed="false">{PF[lang].get(p, p)}</button>' for p in FILTER_PF)
    out = [f'<section id="apps" class="catalog-page">\n  <div class="head"><div><div class="kicker">{t["kicker"]}</div>'
           f'<h1 class="serif pagetitle">{t["h2"]}</h1><p class="lead">{t["lead"]}</p></div>\n'
           f'  <div class="filters"><div class="chips" id="kat" role="group" aria-label="{t["filter"]}">{chips}</div>'
           f'<div class="chips" id="pfk" role="group" aria-label="{t["pfilter"]}">{pchips}</div></div></div>']
    for k, de, en in CATS:
        note = NOTE.get(k)
        out.append(f'  <div class="group" data-k="{k}"><h2 class="serif">{de if lang == "de" else en}</h2>'
                   + (f'<p class="hint-note">{note[0 if lang == "de" else 1]}</p>' if note else "")
                   # Verfügbares zuerst, sonst Reihenfolge wie in APPS
                   + '<div class="cat">' + "".join(card(a, lang) for a in sorted((a for a in APPS if a[2] == k), key=lambda a: not a[4])) + '</div></div>')
    out.append(f'  <p class="none" id="none" hidden>{t["none"]}</p>')
    out.append('</section>')
    return "\n".join(out)


def strip(lang):
    """Schmaler Streifen „Jetzt verfügbar“ für die Startseite: Icon, Name, ein Store-Badge, Knopf zum Katalog.
    id="apps" bleibt als Sprungziel für alte Links erhalten."""
    t = L[lang]
    by = {a[0]: a for a in APPS}
    items = []
    for key in FEATURED:
        _, name, cat, pfs, ok, site, stores, de, en = by[key]
        if not (ok and stores):
            raise SystemExit(f"FEATURED: {key} ist nicht verfügbar oder hat keinen Store-Link")
        pf = ", ".join(PF[lang].get(p, p) for p in pfs)
        first = sorted(stores, key=lambda x: ORDER[x[0]])[:1]
        items.append(f'<div class="nowi">{icon(key, name)}<div><b><a href="{site_url(site, lang)}">{name}</a><small>{pf}</small></b>{store_links(first, lang)}</div></div>')
    n = sum(1 for a in APPS if a[4])
    return (f'<!-- katalog:start -->\n<section id="apps">\n  <div class="head"><div class="reveal"><div class="kicker">{t["s_kicker"]}</div>'
            f'<h2 class="serif">{t["s_h2"]}</h2><p class="lead">{t["s_lead"]}</p></div></div>\n'
            f'  <div class="now reveal">{"".join(items)}</div>\n'
            f'  <div class="nowmore reveal"><a class="btn primary" href="apps/">{t["s_btn"]}</a><span>{t["s_count"].format(n=n)}</span></div>\n'
            '</section>\n<!-- katalog:end -->')


BLOCK = re.compile(r"<!-- katalog:start -->.*?<!-- katalog:end -->", re.S)


def sub1(pattern, repl, s):
    s, n = re.subn(pattern, repl, s, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("Katalogseite: Muster nicht gefunden: " + pattern)
    return s


def page(home, lang):
    """Baut die Katalogseite aus der fertigen Startseite derselben Sprache: Kopf, Menü und Fuß werden übernommen,
    alle relativen Pfade eine Ebene tiefer gesetzt. So gibt es Menü und Fuß nur einmal (in index.html)."""
    t = L[lang]
    top = home[:home.index('<header class="hero"')]
    foot = home[home.index("<footer>"):home.index("<script src=")]
    js = re.search(r'<script src="[^"]*site\.js"></script>', home).group(0)
    pre = "" if lang == "de" else "../"   # Pfade wie auf der Startseite der Sprache, danach gemeinsam eine Ebene tiefer
    body = catalog(lang).replace('src="img/', f'src="{pre}img/').replace('src="brand/', f'src="{pre}brand/')
    s = top + "<main>\n" + body + "\n</main>\n\n" + foot + js + "\n</body>\n</html>\n"
    # nur für die Startseite nötig: Stimmung, Glühwürmchen, Ton, Logo-Filter
    for pat in (r'<div id="mood"[^>]*></div>\n', r'<canvas id="fx"[^>]*></canvas>\n', r'\s*<button class="snd" id="snd".*?</button>',
                r'<style>\.mark \.glow\{[^<]*</style>\n', r'<link rel="preconnect" href="https://get\.microsoft\.com" crossorigin>\n'):
        s = sub1(pat, "", s)
    s = sub1(r'<a class="skip" href="#spiele">', '<a class="skip" href="@apps">', s)
    s = re.sub(r'\b(src|href)="(?!https?:|mailto:|data:|#|@)([^"]*)"', r'\1="../\2"', s)
    s = s.replace('href="#top"', 'href="../"')
    s = re.sub(r'href="#([a-z]+)"', r'href="../#\1"', s).replace('href="@apps"', 'href="#apps"')
    s = sub1(r'<a href="\.\./apps/">', '<a href="./" aria-current="page">', s)
    if lang == "de":
        s = sub1(r'<a class="lang" href="\.\./en/"', '<a class="lang" href="../en/apps/"', s)
    else:
        s = sub1(r'<a class="lang" href="\.\./\.\./"', '<a class="lang" href="../../apps/"', s)
    # Kopf: eigene Titel, Beschreibung, canonical, hreflang, OG
    s = re.sub(r'(content|href)="' + re.escape(BASE) + r'(en/)?"', lambda m: f'{m.group(1)}="{BASE}{m.group(2) or ""}apps/"', s)
    s = sub1(r"<title>.*?</title>", f'<title>{t["title"]}</title>', s)
    for prop, val in (('name="description"', t["desc"]), ('property="og:title"', t["short"]), ('property="og:description"', t["desc"]),
                      ('name="twitter:title"', t["short"]), ('name="twitter:description"', t["desc"])):
        s = sub1(f'<meta {prop} content="[^"]*">', f'<meta {prop} content="{val}">', s)
    return s


def write(rel, s):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(s)
    print(rel, "geschrieben")


if __name__ == "__main__":
    s = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    if not BLOCK.search(s):
        raise SystemExit("katalog-Marker fehlen in index.html")
    s = BLOCK.sub(lambda m: strip("de"), s)
    write("index.html", s)
    write("apps/index.html", page(s, "de"))
