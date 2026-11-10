"""Builds en/index.html from index.html. Edit the German page, then run: python3 tools/build_en.py
Every source string must exist, so a changed German text fails loudly instead of leaving German in the English page."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import catalog
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://minh.systems/MinhNguyenStudios/"

T = [
 # head
 ('<html lang="de">', '<html lang="en">'),
 ('<title>Minh Nguyen Studios – Apps &amp; Spiele für Windows, iPhone, Android und Mac</title>', '<title>Minh Nguyen Studios – Apps &amp; games for Windows, iPhone, Android and Mac</title>'),
 ('content="Unabhängiges Studio aus Deutschland: private Werkzeuge für Ordnung, Dateien und Belege, Lern-Apps, ruhige Spiele und Kinder-Apps für Windows, iPhone, iPad, Android und Mac."', 'content="Independent studio from Germany: private tools for files, folders and receipts, learning apps, calm games and kids’ apps for Windows, iPhone, iPad, Android and Mac."'),
 ('content="Private Werkzeuge, ruhige Spiele und Kinder-Apps für Windows, iPhone, iPad, Android und Mac – von einem unabhängigen Studio aus Deutschland."', 'content="Private tools, calm games and kids’ apps for Windows, iPhone, iPad, Android and Mac – from an independent studio in Germany."'),
 ('<meta property="og:title" content="Minh Nguyen Studios – Apps &amp; Spiele">', '<meta property="og:title" content="Minh Nguyen Studios – Apps &amp; games">'),
 (f'<meta property="og:url" content="{BASE}">', f'<meta property="og:url" content="{BASE}en/">'),
 (f'<link rel="canonical" href="{BASE}">', f'<link rel="canonical" href="{BASE}en/">'),
 ('content="de_DE"', 'content="en_US"'),
 ('og:locale:alternate" content="en_US"', 'og:locale:alternate" content="de_DE"'),
 ('<meta name="twitter:title" content="Minh Nguyen Studios – Apps &amp; Spiele">', '<meta name="twitter:title" content="Minh Nguyen Studios – Apps &amp; games">'),
 ('>Zum Inhalt springen</a>', '>Skip to content</a>'),
 # nav
 ('<a class="lang" href="en/" hreflang="en" lang="en" title="English">EN</a>', '<a class="lang" href="../" hreflang="de" lang="de" title="Deutsch">DE</a>'),
 ('aria-label="Minh Nguyen Studios – Startseite"', 'aria-label="Minh Nguyen Studios – home"'),
 ('<li><a href="#spiele">Werkstatt</a></li><li><a href="#apps">Apps &amp; Spiele</a></li><li><a href="#ratgeber">Ratgeber</a></li>', '<li><a href="#spiele">Workshop</a></li><li><a href="#apps">Apps &amp; games</a></li><li><a href="#ratgeber">Guides</a></li>'),
 ('aria-label="Hell oder dunkel" title="Hell oder dunkel"', 'aria-label="Light or dark" title="Light or dark"'),
 ('<li><a href="#kontakt">Kontakt</a></li>', '<li><a href="#kontakt">Contact</a></li>'),
 ('title="Ton an/aus"', 'title="Sound on/off"'),
 ('<span id="sndl">Ton aus</span>', '<span id="sndl">Sound off</span>'),
 # hero
 ('Apps &amp; Spiele, die man <em>weitererzählt.</em>', 'Apps &amp; games you can’t <em>stop recommending.</em>'),
 ('Ein unabhängiges Studio aus Deutschland. Wir bauen kleine, private Werkzeuge für Ordnung und Alltag, liebevolle Welten für die Kleinsten – und tiefe Strategiespiele für alle, die gern lange nachdenken.',
  'An independent studio from Germany. We build small, private tools for tidying up and everyday life, loving worlds for the little ones – and deep strategy games for everyone who likes to think things through.'),
 ('>Neue Spiele ansehen<', '>See our new games<'),
 ('>Alle Apps &amp; Spiele<', '>All apps &amp; games<'),
 # featured
 ('<div class="kicker">Aus der Werkstatt</div><h2 class="serif">Zehn Welten, an denen wir bauen</h2>', '<div class="kicker">From the workshop</div><h2 class="serif">Ten worlds we’re building</h2>'),
 ('Veröffentlicht oder mitten in der Produktion – das ist, woran wir gerade mit ganzem Herzen arbeiten.', 'Released or deep in production – this is what we’re pouring our hearts into right now.'),
 ('>Alle</button>', '>All</button>'), ('>Für Kinder</button>', '>For kids</button>'), ('>Strategie &amp; Geschichte</button>', '>Strategy &amp; history</button>'),
 ('alt="Summgarten – der singende Garten mit Figuren auf den Beeten"', 'alt="Summgarten – the singing garden with creatures on the flower beds"'),
 ('Singender Garten · iPhone, iPad, Android, Mac &amp; Windows · ab 3 Jahren', 'Singing garden · iPhone, iPad, Android, Mac &amp; Windows · ages 3+'),
 ('<span class="status">Im App Store, Microsoft Store &amp; bei Google Play</span>', '<span class="status">On the App Store, Microsoft Store &amp; Google Play</span>'),
 ('<img src="brand/badges/app-store-de.svg" alt="Laden im App Store"', '<img src="brand/badges/app-store-en.svg" alt="Download on the App Store"'),
 ('<img src="https://get.microsoft.com/images/de%20dark.svg" alt="Download im Microsoft Store" width="183"', '<img src="https://get.microsoft.com/images/en-us%20dark.svg" alt="Get it from Microsoft" width="161"'),
 ('<img src="brand/badges/google-play-de.svg" alt="Jetzt bei Google Play" width="148" height="44">', '<img src="brand/badges/google-play-en.svg" alt="Get it on Google Play" width="148" height="44">'),
 ('https://play.google.com/store/apps/details?id=de.michelnguyen.klanggarten&amp;hl=de', 'https://play.google.com/store/apps/details?id=de.michelnguyen.klanggarten&amp;hl=en'),
 ('Apple, das Apple-Logo und App Store sind Marken der Apple Inc., eingetragen in den USA und anderen Ländern. Microsoft und das Microsoft-Logo sind Marken der Microsoft-Unternehmensgruppe. Google Play und das Google-Play-Logo sind Marken von Google LLC.', 'Apple, the Apple logo and App Store are trademarks of Apple Inc., registered in the U.S. and other countries. Microsoft and the Microsoft logo are trademarks of the Microsoft group of companies. Google Play and the Google Play logo are trademarks of Google LLC.'),
 ('Die Stimme deines Kindes wird zum Samen: Jedes aufgenommene Geräusch lässt eine Pflanze oder ein Tierchen wachsen, das den Klang im Takt vorsingt – bis ein kleines Orchester entsteht. Ohne Werbung, ohne In-App-Käufe, ohne Datensammeln.',
  'Your child’s voice becomes a seed: every recorded sound grows a plant or a little creature that sings it back in rhythm – until a tiny orchestra appears. No ads, no in-app purchases, no data collection.'),
 ('alt="Gute Nacht, Spielzeug – Spielzeug im Kinderzimmer am Abend"', 'alt="Good Night, Toys – toys in a child’s room in the evening"'),
 ('<span class="status prod">In Arbeit</span>', '<span class="status prod">In the works</span>'),
 ('<h3 class="serif">Gute Nacht, Spielzeug</h3>', '<h3 class="serif">Good Night, Toys</h3>'),
 ('Interaktives Bilderbuch · iPhone &amp; iPad · ab 3 Jahren', 'Interactive picture book · iPhone &amp; iPad · ages 3+'),
 ('Jedes Spielzeug hatte einen großen Tag. Dein Kind schenkt ihm einen kleinen, liebevollen Abschluss – ein ruhiges Bilderbuch zum Mitspielen, gemacht für die letzten Minuten vor dem Einschlafen.',
  'Every toy had a big day. Your child gives each one a small, loving goodnight – a calm picture book to play along with, made for the last minutes before sleep.'),
 ('href="https://minh.systems/GuteNachtSpielzeug/" target="_blank" rel="noopener">Zur Website →', 'href="https://minh.systems/GuteNachtSpielzeug/en/" target="_blank" rel="noopener">Visit the website →'),
 ('alt="Biber Bruno freut sich über ein repariertes Fahrrad"', 'alt="Bruno the beaver celebrates a repaired bike"'),
 ('<h3 class="serif">Kleiner Reparierer</h3>', '<h3 class="serif">Little Fixer <small style="font-size:.5em;color:var(--muted)">(Kleiner Reparierer)</small></h3>'),
 ('Werkstatt-Spiel · Windows · 3–6 Jahre', 'Workshop game · Windows · ages 3–6'),
 ('Biber Bruno hat eine Werkstatt, und die Tiere aus dem Dorf bringen ihm ihre kaputten Sachen. Dein Kind findet durch Ausprobieren heraus, was passt: reparieren, putzen, anmalen – ganz ohne Texte und ohne Scheitern.',
  'Bruno the beaver runs a workshop, and the village animals bring him their broken things. Your child figures out what fits by trying: fixing, cleaning, painting – no reading required and no way to fail.'),
 ('alt="Kontor – Hamburger Handelskontor um 1600"', 'alt="Kontor – a Hamburg trading house around 1600"'),
 ('<span class="status prod">In Vorbereitung</span>', '<span class="status prod">In preparation</span>'),
 ('href="https://minh.systems/KleinerReparierer/" target="_blank" rel="noopener">Zur Website →', 'href="https://minh.systems/KleinerReparierer/" target="_blank" rel="noopener">Visit the website →'),
 ('Wirtschafts- &amp; Strategiespiel · iPad, Mac, PC', 'Economic &amp; strategy game · iPad, Mac, PC'),
 ('Hamburg, 1600. Dein Siegel. Dein Risiko. Du führst ein Kontor und erfindest die Versicherung – handelst mit Gefahr und baust aus Briefen, Schiffslisten und Totenregistern deine eigene Statistik auf.',
  'Hamburg, 1600. Your seal. Your risk. You run a trading house and invent insurance – dealing in danger and building your own statistics from letters, ship lists and death registers.'),
 ('href="https://minh.systems/Kontor/" target="_blank" rel="noopener">Zur Website →', 'href="https://minh.systems/Kontor/" target="_blank" rel="noopener">Visit the website →'),
 ('alt="Germ Theory – Querschnitt durch eine Krankenstation"', 'alt="Germ Theory – cutaway of a hospital ward"'),
 ('Krankenhaus-Aufbausimulation · Steam', 'Hospital building sim · Steam'),
 ('„The germs are real. Nobody believes you.“ Leite ein Krankenhaus in einer Hafenstadt zwischen 1875 und 1892 – in den Jahren, in denen die Medizin von Miasmen zu Mikroben wechselt. Jede Entdeckung ist echt, jeder Fortschritt hart erkämpft.',
  '“The germs are real. Nobody believes you.” Run a hospital in a port city between 1875 and 1892 – the years when medicine moved from miasma to microbes. Every discovery is real, every step forward hard-won.'),
 ('alt="Breach Inc. – IT-Security-Büro im Keller bei Nacht"', 'alt="Breach Inc. – a basement IT security office at night"'),
 ('<span class="status prod">In Entwicklung</span>', '<span class="status prod">In development</span>'),
 ('Die Nachtschicht gehört dir. Führe einen kleinen IT-Security-Dienstleister aus dem Kellerbüro: Kunden gewinnen, Admins einteilen, Schutz kaufen – und entscheiden, wie viel Marge du opferst, bevor die nächste Phishing-Welle zuschlägt.',
  'The night shift is yours. Run a small IT security firm from a basement office: win clients, assign admins, buy protection – and decide how much margin to sacrifice before the next phishing wave hits.'),
 ('(Arbeitstitel)</small>', '(working title)</small>'),
 ('alt="Brinehold – Nordsee-Insel mit Deich und Fähre im aufziehenden Sturm"', 'alt="Brinehold – a North Sea island with dike and ferry as a storm gathers"'),
 ('Insel-Aufbauspiel · PC', 'Island builder · PC'),
 ('Das Wasser steigt nach einem öffentlichen Gezeitenplan. Baue Deiche und Schleusen, verlege Gebäude und bringe die Bewohner rechtzeitig per Fähre in Sicherheit – bis am letzten Tag die höchste Flut kommt.', 'The water rises on a public tide table. Build dikes and sluices, move buildings and ferry residents to safety in time – before the highest tide arrives on the last day.'),
 ('alt="Maladoro – ein Schlosshotel als Luxusklinik in den Alpen"', 'alt="Maladoro – a chateau turned luxury clinic in the Alps"'),
 ('<span class="status prod">Prototyp</span>', '<span class="status prod">Prototype</span>'),
 ('Satirische Klinik-Aufbausimulation · PC', 'Satirical clinic builder · PC'),
 ('Baue die teuerste Privatklinik der Alpen, erfinde Reichen immer kostspieligere Leiden wie Yachtnacken und Erbschaftsmüdigkeit und halte Prüfer und Anwälte hin. Eine böse Komödie über Gier.', 'Build the most expensive private clinic in the Alps, invent ever costlier ailments for the rich and stall inspectors and lawyers. A wicked comedy about greed.'),
 ('<span class="status">Im Microsoft Store</span>', '<span class="status">On the Microsoft Store</span>'),
 # guides
 ('<div class="kicker">Hilfe &amp; Anleitungen</div><h2 class="serif">Ratgeber</h2>', '<div class="kicker">Help &amp; how-tos</div><h2 class="serif">Guides</h2>'),
 ('Kurze Anleitungen zu typischen Alltagsfragen – mit und ohne unsere Apps.', 'Short guides to everyday questions – with or without our apps. (Some in German.)'),
 ('<h3>Ordnung &amp; Dateien</h3>', '<h3>Files &amp; folders</h3>'),
 ('Folvane/de/ordner-vergleichen-windows.html">Ordner unter Windows vergleichen', 'Folvane/compare-folders-windows.html">Compare folders on Windows'),
 ('Folvane/de/doppelte-dateien-finden.html">Doppelte Dateien finden', 'Folvane/find-duplicate-files-windows.html">Find duplicate files'),
 ('Folvane/de/backup-pruefen.html">Backup prüfen', 'Folvane/check-backup.html">Check a backup'),
 ('Folvane/de/dateien-synchronisieren-ohne-loeschen.html">Dateien synchronisieren, ohne zu löschen', 'Folvane/sync-folders-without-deleting.html">Sync folders without deleting'),
 ('<h3>Haushaltsbuch</h3>', '<h3>Budget book (German)</h3>'),
 ('>Haushaltsbuch ohne Abo<', '>Budget book without subscription<'),
 ('>Haushaltsbuch offline unter Windows<', '>Offline budget book on Windows<'),
 ('>Kontoauszüge als CSV importieren<', '>Import bank statements as CSV<'),
 ('<h3>Spiele &amp; Kinder</h3>', '<h3>Games &amp; kids</h3>'),
 ('>Zahnrad-Rätsel lösen: Tipps<', '>Solving gear puzzles: tips<'),
 ('>Entspannende Puzzlespiele ohne Werbung<', '>Relaxing puzzle games without ads<'),
 ('LittleKeepings/de/sortierspiel-ohne-zeitdruck.html">Sortierspiel ohne Zeitdruck', 'LittleKeepings/sorting-puzzle-no-timer.html">Sorting puzzle with no timer'),
 ('Summgarten/musik-app-fuer-kinder/">Musik-App für Kinder', 'Summgarten/en/music-app-for-kids/">Music app for kids'),
 ('Summgarten/kinder-zum-singen-bringen/">Kinder zum Singen bringen', 'Summgarten/en/get-kids-to-sing/">Getting kids to sing'),
 # studio
 ('<div class="kicker">Das Studio</div><h2 class="serif">Wofür wir stehen</h2>', '<div class="kicker">The studio</div><h2 class="serif">What we stand for</h2>'),
 ('Minh Nguyen Studios ist ein kleines, unabhängiges Studio. Wir machen weniger Spiele – und dafür jedes so, als wäre es das einzige.', 'Minh Nguyen Studios is a small, independent studio. We make fewer games – and make each one as if it were the only one.'),
 ('<b>Staunen</b><p>Jede Welt soll sich beim ersten Blick wie ein kleines Geschenk anfühlen.</p>', '<b>Wonder</b><p>Every world should feel like a small gift at first sight.</p>'),
 ('<b>Respekt vor Kindern</b><p>Spiele für Kinder ohne Druck, ohne Tricks und mit Eltern im Blick.</p>', '<b>Respect for kids</b><p>Games for children without pressure, without tricks, and with parents in mind.</p>'),
 ('<b>Echte Tiefe</b><p>Systeme, die man stundenlang erforscht – leicht zu lernen, schwer zu meistern.</p>', '<b>Real depth</b><p>Systems you explore for hours – easy to learn, hard to master.</p>'),
 ('<b>Geschichte, ernst genommen</b><p>Historische Spiele, gründlich recherchiert und offen darüber, wo sie vereinfachen.</p>', '<b>History, taken seriously</b><p>Historical games, carefully researched and open about where they simplify.</p>'),
 # contact + footer
 ('<div class="kicker">Presse, Partner, Fans</div><h2 class="serif">Schreib uns.</h2>', '<div class="kicker">Press, partners, fans</div><h2 class="serif">Write to us.</h2>'),
 ('Für Presseanfragen, Kooperationen oder einfach ein Hallo.', 'For press, partnerships or just to say hello.'),
 ('<a href="https://minh.systems/impressum/">Impressum</a><a href="https://minh.systems/datenschutz/">Datenschutz</a>', '<a href="https://minh.systems/impressum/" hreflang="de">Legal notice (DE)</a><a href="https://minh.systems/datenschutz/" hreflang="de">Privacy (DE)</a>'),
 # script strings
 ("sfx.on?'Ton an':'Ton aus'", "sfx.on?'Sound on':'Sound off'"),
 ("label:'Garten singen lassen',hint:'Tippe in den Garten – oben singt es hoch, unten tief'", "label:'Make the garden sing',hint:'Tap the garden – high notes up top, low notes below'"),
 ("label:'Licht ausmachen',hint:'Gute Nacht! Tippe, um Sterne an die Decke zu malen'", "label:'Turn off the light',hint:'Good night! Tap to paint stars on the ceiling'"),
 ("label:'Fahrrad reparieren',hint:'Zieh die drei Schrauben fest'", "label:'Fix the bike',hint:'Tighten the three screws'"),
 ("label:'Police besiegeln',hint:'Drück dein Siegel auf – jede Police ein Risiko'", "label:'Seal a policy',hint:'Press your seal – every policy is a risk'"),
 ("label:'Mikroskop ansetzen',hint:'Such die Keime mit der Lupe – tippe, um sie zu vernichten'", "label:'Use the microscope',hint:'Hunt the germs with the lens – tap to wipe them out'"),
 ("label:'Nachtschicht übernehmen',hint:'Blocke die Angriffe, bevor sie durchkommen!'", "label:'Take the night shift',hint:'Block the attacks before they get through!'"),
 ("banner(L,'Repariert! Bruno freut sich ✦')", "banner(L,'Fixed! Bruno is delighted ✦')"),
 ("banner(L,'Acht Policen gezeichnet. Möge kein Schiff sinken.')", "banner(L,'Eight policies signed. May no ship sink.')"),
 ("'Keime: '", "'Germs: '"),
 ("banner(L,'Alles sauber. Semmelweis wäre stolz.')", "banner(L,'All clean. Semmelweis would be proud.')"),
 ("'Passwort-Leak','Fake-Rechnung'", "'Password leak','Fake invoice'"),
 ("'Abgewehrt: 0/'", "'Blocked: 0/'"),
 ("`Abgewehrt: ${ok}/${total}`", "`Blocked: ${ok}/${total}`"),
 ("`Nachtschicht überstanden: ${ok}/${total} ✦`:`${ok}/${total} abgewehrt – der Kaffee war zu dünn.`", "`Night shift survived: ${ok}/${total} ✦`:`${ok}/${total} blocked – the coffee was too weak.`"),
 ("'✓ Geblockt'", "'✓ Blocked'"),
 ("'<b>✕</b> Fertig'", "'<b>✕</b> Done'"),
 ("' · 🔈 mit Ton schöner'", "' · 🔈 better with sound'"),
]

PATHS = [('src="brand/badges/', 'src="../brand/badges/'), ('src="img/', 'src="../img/'), ('src="brand/', 'src="../brand/'), ('href="brand/', 'href="../brand/'),
         ('href="fonts.css"', 'href="../fonts.css"'), ('href="fonts/', 'href="../fonts/'), ('data-video="video/', 'data-video="../video/')]

s = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
s = catalog.BLOCK.sub(lambda m: catalog.render("en"), s)
missing = [de for de, _ in T if de not in s]
if missing:
    raise SystemExit("German source strings not found (update tools/build_en.py):\n- " + "\n- ".join(m[:90] for m in missing))
for de, en in T + PATHS:
    s = s.replace(de, en)
os.makedirs(os.path.join(ROOT, "en"), exist_ok=True)
open(os.path.join(ROOT, "en", "index.html"), "w", encoding="utf-8").write(s)
print("en/index.html written")
