# Minh Nguyen Studios – Website

Statische Seite (GitHub Pages), Test-URL: https://minh.systems/MinhNguyenStudios/ · Ziel-Domain: minhnguyen.studio

Zwei Seiten je Sprache:

- `index.html` – deutsche Startseite (Quelle): Hero, große Spiele, Streifen „Jetzt verfügbar“, Ratgeber, Studio, Kontakt. Inhalte, Menü und Fuß nur hier ändern.
- `apps/index.html` – **generiert**: Katalogseite „Apps & Spiele“ mit Bereichs- und Gerätefilter. Kopf, Menü und Fuß stammen aus `index.html`.
- `en/index.html`, `en/apps/index.html` – **generiert**. Neue/geänderte deutsche Texte in `tools/build_en.py` übersetzen;
  das Skript bricht ab, wenn ein deutscher Ausgangstext nicht mehr gefunden wird.
- `site.css`, `site.js` – gemeinsam für alle vier Seiten (Menü, Hell/Dunkel, Katalogfilter). Das Skript in `index.html` enthält nur, was die Startseite braucht.
- Katalog in `tools/catalog.py` pflegen (eine Datenquelle für Streifen und Katalogseite; Auswahl des Streifens: `FEATURED`).
- Bauen nach jeder Änderung: `python3 tools/catalog.py && python3 tools/build_en.py`.
- Gerätefilter per Adresse vorwählen: `apps/#geraet=Windows` (auch `iPhone`, `Android`, `Mac`; Bereich: `#bereich=spiele`). Alte Sprungziele `#apps` und `#katalog` führen zum Streifen.
- Katalogkarten: Store-Badges in einer Reihe (Apple, Google Play, Microsoft), „Website“ immer in eigener Zeile darunter.
- `impressum.html`, `datenschutz.html` – nur Weiterleitungen auf das zentrale Impressum/Datenschutz unter minh.systems.
- Store-Badges: nur für live veröffentlichte Apps, Grafik nie ändern, Apple zuerst, Höhe 44 px, mindestens 11 px Abstand. Apple-SVGs unverändert aus dem Apple-Marketing-Toolbox; Microsoft-Badge von get.microsoft.com eingebunden.
- Logo/CI-Quellen: `~/Developer/Logo/final/`.
- Beim Umzug auf minhnguyen.studio: `CNAME` anlegen und `https://minh.systems/MinhNguyenStudios/` in den Meta-Tags ersetzen.
- Live-Status aller Titel und Prüfweg: `docs/LIVE_STATUS.md` (Stand 09.11.2026). Vor neuen Badges dort nachprüfen und ergänzen.
