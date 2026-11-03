"""App- und Spielekatalog – eine Datenquelle für DE und EN.
python3 tools/catalog.py schreibt den deutschen Block in index.html (zwischen den katalog-Markern);
tools/build_en.py ersetzt ihn beim Bauen der englischen Seite durch render("en").
Store-Links nur eintragen, wenn die Store-Seite live ist (geprüft 03.11.2026)."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = "https://minh.systems/"
APPLE = "https://apps.apple.com/app/id"
MS = "https://apps.microsoft.com/detail/"

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
 ("nomad", "Nomad Kitchen Tycoon", "spiele", ["iPhone"], True, S+"NomadKitchenTycoon/", [("apple", APPLE+"6759504817")],
  "Foodtruck-Management in zwei Städten.", "Food truck management across two cities."),
 ("cogwisp", "Cogwisp", "spiele", ["Windows"], True, S+"Cogwisp/", [("ms", MS+"9NSRPBK9PL5N")],
  "Entspannte Zahnrad-Rätsel ohne Werbung.", "Relaxing gear puzzles without ads."),
 ("littlekeepings", "Little Keepings", "spiele", ["Windows"], True, S+"LittleKeepings/", [("ms", MS+"9N1WQT29BF8W")],
  "Ruhiges Sortierrätsel ohne Zeitdruck.", "A calm sorting puzzle with no timer."),
 ("folvane", "Folvane", "ordnung", ["Windows"], True, S+"Folvane/", [("ms", MS+"9NSDC58HLFRR")],
  "Ordner vergleichen, synchronisieren und Backups prüfen – mit Vorschau und Rückgängig.", "Compare and sync folders and check backups – with preview and undo."),
 ("pathrova", "Pathrova", "ordnung", ["Windows"], False, S+"Pathrova/", [],
  "Findet zu lange Pfade und ungültige Namen, bevor du nach OneDrive oder SharePoint synchronisierst.", "Finds overly long paths and invalid names before you sync to OneDrive or SharePoint."),
 ("ablagefuchs", "Ablagefuchs", "ordnung", ["Windows"], False, S+"Ablagefuchs/", [],
  "Verträge, Rechnungen und Schreiben an einem Ort – mit Texterkennung und Fristen, offline.", "Contracts, invoices and letters in one place – with text recognition and deadlines, offline."),
 ("fotokehr", "Fotokehr", "ordnung", ["Windows"], False, S+"Fotokehr/", [],
  "Fotos und Videos lokal nach Datum sortieren – Originale bleiben unverändert.", "Sort photos and videos by date, locally – originals stay untouched."),
 ("plauderbuch", "Plauderbuch", "ordnung", ["Windows"], False, None, [],
  "Exportierte Chatverläufe zusammenführen und als Erinnerung aufbewahren.", "Merge exported chat histories and keep them as a keepsake."),
 ("shotsift", "ShotSift", "ordnung", ["iPhone"], True, S+"ShotSift/", [("apple", APPLE+"6758222349")],
  "Fotos aufräumen – Duplikate, Screenshots und Serien, alles auf dem Gerät.", "Tidy your photos – duplicates, screenshots and bursts, all on-device."),
 ("monatsklar", "Monatsklar", "finanzen", ["Windows"], True, S+"Monatsklar/", [("ms", MS+"9N6JM2J3LC27")],
  "Haushaltsbuch für Windows – offline und ohne Abo.", "Household budget book for Windows – offline, no subscription."),
 ("belegora", "Belegora", "finanzen", ["Windows"], True, S+"belegora/", [("ms", MS+"9NB7QSNC6MJQ")],
  "Belege, Geräte und Garantiefristen an einem Ort, offline.", "Receipts, devices and warranty dates in one place, offline."),
 ("tastenflink", "Tastenflink", "lernen", ["Windows"], False, None, [],
  "Zehnfingerschreiben lernen – Schritt für Schritt, ohne Konto.", "Learn to touch-type – step by step, no account."),
 ("ridgefocus", "RidgeFocus", "lernen", ["iPhone"], True, S+"RidgeFocus/", [("apple", APPLE+"6758014649")],
  "Pomodoro-Timer für konzentriertes Arbeiten und Lernen.", "Pomodoro timer for focused work and study."),
 ("rootling", "Rootling", "lernen", ["iPhone"], True, S+"Rootling/", [("apple", APPLE+"6758851487")],
  "Stecklinge bewurzeln – mit Prognosen und Pflanzentagebuch.", "Root cuttings – with forecasts and a plant journal."),
 ("mushbloom", "MushBloom", "lernen", ["iPhone"], True, "https://mushbloom.minh.systems/", [("apple", APPLE+"6758917023")],
  "Begleiter für die Pilzzucht zu Hause.", "A companion for growing mushrooms at home."),
 ("horsehold", "Horsehold", "lernen", ["iPhone"], True, S+"Stable/", [("apple", APPLE+"6826688753")],
  "Stallbuch fürs Pferd: Pflege, Termine und Dokumente.", "A stable book for your horse: care, appointments and documents."),
 ("summgarten", "Summgarten", "kinder", ["iPhone", "Mac", "Windows"], True, S+"Summgarten/", [("apple", APPLE+"6824160993"), ("ms", MS+"9PGTW423BB1H")],
  "Singender Garten für Kinder ab 3 – im Microsoft Store als Hum Garden.", "A singing garden for kids 3+ – called Hum Garden in the Microsoft Store."),
 ("reparierer", "Kleiner Reparierer", "kinder", ["iPhone"], False, S+"KleinerReparierer/", [],
  "Mit Biber Bruno reparieren, putzen und anmalen – ohne Texte, ohne Scheitern.", "Fix, scrub and paint with Bruno the beaver – no reading, no failing."),
]

L = {
 "de": dict(all="Alle", ok="Verfügbar", soon="Demnächst", ms="Microsoft Store", apple="App Store", site="Website",
            kicker="Alles aus unserer Werkstatt", h2="Apps &amp; Spiele",
            lead="Kleine, private Werkzeuge und ruhige Spiele für Windows, iPhone, iPad und Mac – ohne Konto, meist offline.",
            filter="Nach Bereich filtern"),
 "en": dict(all="All", ok="Available", soon="Coming soon", ms="Microsoft Store", apple="App Store", site="Website",
            kicker="Everything from our workshop", h2="Apps &amp; games",
            lead="Small, private tools and calm games for Windows, iPhone, iPad and Mac – no account, mostly offline.",
            filter="Filter by category"),
}
PF = {"de": {"iPhone": "iPhone &amp; iPad"}, "en": {"iPhone": "iPhone &amp; iPad"}}


def card(a, lang):
    key, name, cat, pfs, ok, site, stores, de, en = a
    t = L[lang]
    if site and lang == "en" and site.startswith(S + "Summgarten"):
        site += "en/"
    title = f'<a href="{site}">{name}</a>' if site else name
    badges = "".join(f'<span class="pf">{PF[lang].get(p, p)}</span>' for p in pfs)
    st = f'<span class="st ok">{t["ok"]}</span>' if ok else f'<span class="st soon">{t["soon"]}</span>'
    go = "".join(f'<a class="store" href="{u}" target="_blank" rel="noopener">{t[k]}</a>' for k, u in stores)
    if site:
        go += f'<a class="more" href="{site}">{t["site"]} →</a>'
    return (f'<article class="app" data-cat="{cat}"><img class="ico" src="img/icons/{key}.webp" alt="" width="56" height="56" loading="lazy">'
            f'<div><h4>{title}</h4><p>{de if lang == "de" else en}</p><div class="badges">{st}{badges}</div>'
            + (f'<div class="go">{go}</div>' if go else "") + '</div></article>')


def render(lang):
    t = L[lang]
    chips = f'<button class="chip on" data-k="all">{t["all"]}</button>' + "".join(
        f'<button class="chip" data-k="{k}">{de if lang == "de" else en}</button>' for k, de, en in CATS)
    out = [f'<!-- katalog:start -->\n<section id="apps">\n  <div class="head"><div class="reveal"><div class="kicker">{t["kicker"]}</div>'
           f'<h2 class="serif">{t["h2"]}</h2><p class="lead">{t["lead"]}</p></div>\n'
           f'  <div class="chips reveal" id="kat" role="group" aria-label="{t["filter"]}">{chips}</div></div>']
    for k, de, en in CATS:
        note = NOTE.get(k)
        out.append(f'  <div class="group" data-k="{k}"><h3 class="serif">{de if lang == "de" else en}</h3>'
                   + (f'<p class="hint-note">{note[0 if lang == "de" else 1]}</p>' if note else "")
                   + '<div class="cat">' + "".join(card(a, lang) for a in APPS if a[2] == k) + '</div></div>')
    out.append('</section>\n<!-- katalog:end -->')
    return "\n".join(out)


BLOCK = re.compile(r"<!-- katalog:start -->.*?<!-- katalog:end -->", re.S)

if __name__ == "__main__":
    p = os.path.join(ROOT, "index.html")
    s = open(p, encoding="utf-8").read()
    if not BLOCK.search(s):
        raise SystemExit("katalog-Marker fehlen in index.html")
    open(p, "w", encoding="utf-8").write(BLOCK.sub(lambda m: render("de"), s))
    print("Katalog in index.html geschrieben")
