# Minh Nguyen Studios – Website

Statische Seite (GitHub Pages), Test-URL: https://minh.systems/MinhNguyenStudios/ · Ziel-Domain: minhnguyen.studio

- `index.html` – deutsche Seite (Quelle). Inhalte nur hier ändern.
- `en/index.html` – **generiert**: `python3 tools/build_en.py`. Neue/geänderte deutsche Texte in `tools/build_en.py` übersetzen;
  das Skript bricht ab, wenn ein deutscher Ausgangstext nicht mehr gefunden wird.
- `impressum.html`, `datenschutz.html` – nur Weiterleitungen auf das zentrale Impressum/Datenschutz unter minh.systems.
- Katalog (Apps & Spiele) in `tools/catalog.py` pflegen, dann `python3 tools/catalog.py && python3 tools/build_en.py`.
- Store-Badges: nur für live veröffentlichte Apps, Grafik nie ändern, Apple zuerst, Höhe 44 px, mindestens 11 px Abstand. Apple-SVGs unverändert aus dem Apple-Marketing-Toolbox; Microsoft-Badge von get.microsoft.com eingebunden.
- Logo/CI-Quellen: `~/Developer/Logo/final/`.
- Beim Umzug auf minhnguyen.studio: `CNAME` anlegen und `https://minh.systems/MinhNguyenStudios/` in den Meta-Tags ersetzen.
