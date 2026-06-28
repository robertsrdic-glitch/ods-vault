# Vibecode

Pregled mini-projektov, ki jih delava skupaj za učenje hitrega AI-podprtega razvoja ("vibecode").

## Repo
Vsi novi vibecode projekti gredo v en zbirni repo: [vibe-projects](https://github.com/robertsrdic-glitch/vibe-projects) (private), v mapo `claude-code/<ime-projekta>`.

## Projekti

### 1. Obsidian — avtomatski pregled odprtih nalog
- Skript: `_scripts/update_tasks.py` (v tem vault-u)
- Kaj naredi: pobere vse odprte `- [ ]` naloge iz vseh zapiskov in jih zbere v [[Auto-Pregled]]
- Status: ✅ deluje

### 2. Hitra beležka — Firebase Firestore + Hosting
- Kaj: preprosta web app (HTML/JS + Firebase Firestore realtime baza), naučili se git/GitHub + Firebase CLI/deploy od začetka do konca
- Koda: `vibe-projects/claude-code/vibecode-firebase-todo`
- Live: https://vibecode-todo.web.app
- Status: ✅ deployano in delujoče

### 3. ODS-Vault → GitHub sync + povezava s Hermesom
- Kaj: cel vault (ta) je zdaj pod git-om in pushan na GitHub, da ima Hermes (VPS agent) resničen, samodejno posodabljan dostop do baze znanja
- Koda/repo: [ods-vault](https://github.com/robertsrdic-glitch/ods-vault) (private)
- Workflow naprej: po vsaki spremembi v Obsidianu poženi `git add . && git commit -m "update" && git push` v tej mapi — Hermes pobere spremembe ob naslednjem cron pull-u
- Status: ✅ repo živ, Hermes obveščen prek Telegrama, naj nastavi klon + cron

### 4. Navade — Habit tracker PWA (mobilna app)
- Kaj: PWA (HTML/JS + Firebase Firestore) z manifest.json, service worker-jem in lastno generirano ikono (Python/Pillow) — nameščena kot prava app na Samsung Galaxy S25 Ultra
- Koda: `vibe-projects/claude-code/habit-tracker-pwa`
- Live: https://navade-app.web.app
- Nameščeno na telefon prek Chrome "Add to Home screen" — deluje standalone, brez naslovne vrstice
- Naslednji korak: pot do Play Store prek Bubblewrap (TWA → `.aab`), Google Play Console račun ($25)
- Status: ✅ PWA deployano in nameščeno na telefonu · ⏳ Play Store objava še ni narejena

## Opomba
To stran sproti dopolnjujem z novimi projekti, ko jih naredimo.

## Povezave
- [[Tasks]]
