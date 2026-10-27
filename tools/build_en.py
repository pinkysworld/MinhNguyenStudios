"""Builds en/index.html from index.html. Edit the German page, then run: python3 tools/build_en.py
Every source string must exist, so a changed German text fails loudly instead of leaving German in the English page."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://minh.systems/MinhNguyenStudios/"

T = [
 # head
 ('<html lang="de">', '<html lang="en">'),
 ('content="Minh Nguyen Studios – unabhängiges Spielestudio aus Deutschland. Spiele für Kinder, Strategie und Geschichte."', 'content="Minh Nguyen Studios – an independent game studio from Germany. Games for kids, strategy and history."'),
 ('content="Unabhängiges Spielestudio aus Deutschland – liebevolle Spiele für Kinder und tiefe Strategie- und Geschichtsspiele."', 'content="An independent game studio from Germany – lovingly made games for kids and deep strategy and history games."'),
 (f'<meta property="og:url" content="{BASE}">', f'<meta property="og:url" content="{BASE}en/">'),
 ('content="de_DE"', 'content="en_US"'),
 # nav
 ('<a class="lang" href="en/" hreflang="en" lang="en" title="English">EN</a>', '<a class="lang" href="../" hreflang="de" lang="de" title="Deutsch">DE</a>'),
 ('aria-label="Minh Nguyen Studios – Startseite"', 'aria-label="Minh Nguyen Studios – home"'),
 ('<li><a href="#spiele">Spiele</a></li><li><a href="#mehr">Mehr Spiele</a></li>', '<li><a href="#spiele">Games</a></li><li><a href="#mehr">More games</a></li>'),
 ('<li><a href="#kontakt">Kontakt</a></li>', '<li><a href="#kontakt">Contact</a></li>'),
 ('title="Ton an/aus"', 'title="Sound on/off"'),
 ('<span id="sndl">Ton aus</span>', '<span id="sndl">Sound off</span>'),
 # hero
 ('Spiele, die man <em>weitererzählt.</em>', 'Games you can’t <em>stop retelling.</em>'),
 ('Ein unabhängiges Studio aus Deutschland. Wir bauen liebevolle Welten für die Kleinsten – und tiefe Strategie- und Geschichtsspiele für alle, die gern lange nachdenken.',
  'An independent studio from Germany. We build loving worlds for the little ones – and deep strategy and history games for everyone who likes to think things through.'),
 ('>Unsere Spiele entdecken<', '>Discover our games<'),
 ('<a class="btn ghost" href="#kontakt">Kontakt</a>', '<a class="btn ghost" href="#kontakt">Contact</a>'),
 # featured
 ('<div class="kicker">Aktuelle Spiele</div><h2 class="serif">Sechs Welten aus unserer Werkstatt</h2>', '<div class="kicker">Current games</div><h2 class="serif">Six worlds from our workshop</h2>'),
 ('Veröffentlicht, in der Prüfung oder mitten in der Produktion – das ist, woran wir gerade mit ganzem Herzen arbeiten.', 'Released, in review or deep in production – this is what we’re pouring our hearts into right now.'),
 ('>Alle</button>', '>All</button>'), ('>Für Kinder</button>', '>For kids</button>'), ('>Strategie &amp; Geschichte</button>', '>Strategy &amp; history</button>'),
 ('alt="Summgarten – der singende Garten mit Figuren auf den Beeten"', 'alt="Summgarten – the singing garden with creatures on the flower beds"'),
 ('Singender Garten · iPhone, iPad, Mac &amp; Windows · ab 3 Jahren', 'Singing garden · iPhone, iPad, Mac &amp; Windows · ages 3+'),
 ('<span class="status">Im App Store &amp; Microsoft Store</span>', '<span class="status">On the App Store &amp; Microsoft Store</span>'),
 ('>Im Microsoft Store laden<', '>Get it from Microsoft<'),
 ('Die Stimme deines Kindes wird zum Samen: Jedes aufgenommene Geräusch lässt eine Pflanze oder ein Tierchen wachsen, das den Klang im Takt vorsingt – bis ein kleines Orchester entsteht. Ohne Werbung, ohne In-App-Käufe, ohne Datensammeln.',
  'Your child’s voice becomes a seed: every recorded sound grows a plant or a little creature that sings it back in rhythm – until a tiny orchestra appears. No ads, no in-app purchases, no data collection.'),
 ('>Im App Store laden<', '>Download on the App Store<'),
 ('alt="Gute Nacht, Spielzeug – Spielzeug im Kinderzimmer am Abend"', 'alt="Good Night, Toys – toys in a child’s room in the evening"'),
 ('<span class="status review">Bald im App Store</span>', '<span class="status review">Coming to the App Store</span>'),
 ('<h3 class="serif">Gute Nacht, Spielzeug</h3>', '<h3 class="serif">Good Night, Toys</h3>'),
 ('Interaktives Bilderbuch · iPhone &amp; iPad · ab 3 Jahren', 'Interactive picture book · iPhone &amp; iPad · ages 3+'),
 ('Jedes Spielzeug hatte einen großen Tag. Dein Kind schenkt ihm einen kleinen, liebevollen Abschluss – ein ruhiges Bilderbuch zum Mitspielen, gemacht für die letzten Minuten vor dem Einschlafen.',
  'Every toy had a big day. Your child gives each one a small, loving goodnight – a calm picture book to play along with, made for the last minutes before sleep.'),
 ('href="https://minh.systems/GuteNachtSpielzeug/" target="_blank" rel="noopener">Zur Website →', 'href="https://minh.systems/GuteNachtSpielzeug/en/" target="_blank" rel="noopener">Visit the website →'),
 ('alt="Biber Bruno freut sich über ein repariertes Fahrrad"', 'alt="Bruno the beaver celebrates a repaired bike"'),
 ('<h3 class="serif">Kleiner Reparierer</h3>', '<h3 class="serif">Little Fixer <small style="font-size:.5em;color:var(--muted)">(Kleiner Reparierer)</small></h3>'),
 ('Werkstatt-Spiel · iPhone &amp; iPad · 3–6 Jahre', 'Workshop game · iPhone &amp; iPad · ages 3–6'),
 ('Biber Bruno hat eine Werkstatt, und die Tiere aus dem Dorf bringen ihm ihre kaputten Sachen. Dein Kind findet durch Ausprobieren heraus, was passt: reparieren, putzen, anmalen – ganz ohne Texte und ohne Scheitern.',
  'Bruno the beaver runs a workshop, and the village animals bring him their broken things. Your child figures out what fits by trying: fixing, cleaning, painting – no reading required and no way to fail.'),
 ('alt="Kontor – Hamburger Handelskontor um 1600"', 'alt="Kontor – a Hamburg trading house around 1600"'),
 ('<span class="status prod">In Vorbereitung</span>', '<span class="status prod">Coming soon</span>'),
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
 # more games
 ('<div class="kicker">Schon erschienen</div><h2 class="serif">Mehr Spiele</h2>', '<div class="kicker">Already out</div><h2 class="serif">More games</h2>'),
 ('Frühere Spiele von uns – zum direkten Ausprobieren.', 'Earlier games of ours – ready to play.'),
 ('Endzeit-Strategie mit Ereignissen und wachsendem Überlebensdruck', 'Post-apocalyptic strategy with events and rising survival pressure'),
 ('Foodtruck-Management in zwei Städten', 'Food truck management across two cities'),
 ('href="https://minh.systems/Ringjahr/"', 'href="https://minh.systems/Ringjahr/en/"'),
 ('Ruhiges Puzzle über Baumringe und Klima', 'A calm puzzle about tree rings and climate'),
 ('Leben als Bader-Chirurg im Jahr 1382 · im Browser', 'Life as a barber-surgeon in 1382 · in your browser'),
 # apps
 ('<div class="kicker">Auch aus unserer Werkstatt</div>', '<div class="kicker">Also from our workshop</div>'),
 ('Mit derselben Sorgfalt gebaut: kleine, private Werkzeuge für iPhone und iPad.', 'Built with the same care: small, private tools for iPhone and iPad.'),
 ('Fotos aufräumen – Duplikate, Screenshots, Serien, alles auf dem Gerät', 'Tidy your photos – duplicates, screenshots, bursts, all on-device'),
 ('Stecklinge bewurzeln mit Prognosen und Tagebuch', 'Root cuttings with forecasts and a journal'),
 ('Begleiter für die Pilzzucht', 'A companion for growing mushrooms'),
 ('Pomodoro und konzentriertes Arbeiten', 'Pomodoro and deep work'),
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
 ('<a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a>', '<a href="../impressum.html" hreflang="de">Legal notice (DE)</a><a href="../datenschutz.html" hreflang="de">Privacy (DE)</a>'),
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

PATHS = [('src="img/', 'src="../img/'), ('src="brand/', 'src="../brand/'), ('href="brand/', 'href="../brand/'),
         ('href="fonts.css"', 'href="../fonts.css"'), ('data-video="video/', 'data-video="../video/')]

s = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
missing = [de for de, _ in T if de not in s]
if missing:
    raise SystemExit("German source strings not found (update tools/build_en.py):\n- " + "\n- ".join(m[:90] for m in missing))
for de, en in T + PATHS:
    s = s.replace(de, en)
os.makedirs(os.path.join(ROOT, "en"), exist_ok=True)
open(os.path.join(ROOT, "en", "index.html"), "w", encoding="utf-8").write(s)
print("en/index.html written")
