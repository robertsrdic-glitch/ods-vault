Title: NorthStar Decision Register
Version: 0.6
Status: Founder Approved — Pending CTO File Review, Commit, Push and GitHub Verification
Founder: Robert
Product: NorthStar
Decision date: 2026-07-20
Last updated: 2026-07-20

---

# NorthStar Decision Register

## DR-001 — Prvi zaslon prve faze

**Status:** FOUNDER APPROVED

**Odločitev:** NorthStar uporablja vizualno osnovo **Concept A**.

Prvi zaslon ima štiri primarne vstopne točke:

1. **Stanovanjski kredit**
2. **Leasing**
3. **Koliko kredita si lahko privoščim**
4. **Pojasni pojme**

**Utemeljitev:** Concept A je bil izbran kot uradna osnova. Poznejša vsebinska struktura v2 je bila izrecno naročena in jo je Founder ponovno potrdil kot zadnjo veljavno osnovo prve faze.

---

## DR-002 — Razlaga bančne ponudbe in PDF flow

**Status:** FOUNDER APPROVED / SUPERSEDED

**Odločitev:** Kartica **Razloži ponudbo banke** ni del prvega zaslona in ni del prve faze.

**Zgodovina:**

- V starejši verziji Concept A v1 je bila kartica prisotna.
- V Concept A v2 je bila odstranjena.
- Nadomestila jo je kartica **Pojasni pojme**.
- Founder je to strukturo ponovno potrdil kot zadnjo veljavno osnovo.

**Odprto za prihodnost:** Ta odločitev ne pomeni avtomatske trajne ukinitve PDF razlage. Njen morebitni status v poznejši fazi še ni določen.

---

## DR-003 — Affordability

**Status:** FOUNDER APPROVED na UX ravni

**Odločitev:** **Koliko kredita si lahko privoščim** je samostojna primarna vstopna točka prvega zaslona.

Predvideni namen:

> Uporabniku pomaga oceniti varen mesečni obrok glede na njegove prihodke in finančne obveznosti.

**Arhitekturni status:** Razrešen z [[#DR-011 — Arhitektura Affordability|DR-011]] in [[#DR-013 — Samostojni produkti prve faze in shared capabilities|DR-013]].

**Koliko kredita si lahko privoščim** je samostojen produkt prve faze, ki ga podpira shared Affordability capability.

---

## DR-004 — Financial Terms

**Status:** FOUNDER APPROVED na UX ravni

**Odločitev:** **Pojasni pojme** je samostojna primarna vstopna točka prvega zaslona.

Predvideni namen:

> Preproste razlage finančnih pojmov brez žargona.

**Superseded:** Starejša kartica **Razloži ponudbo banke** je bila na prvem zaslonu nadomeščena s to vstopno točko.

**Arhitekturni status:** Razrešen z [[#DR-012 — Arhitektura Financial Terms|DR-012]] in [[#DR-013 — Samostojni produkti prve faze in shared capabilities|DR-013]].

**Pojasni pojme** je samostojen produkt prve faze, ki ga podpira shared Financial Terms capability.

---

## DR-005 — Design okolje

**Status:** FOUNDER APPROVED

**Odločitev:**

- Figma je bila opuščena.
- Dejanski NorthStar design je bil izdelan v Claude Designu.
- Figma ni avtoritativni vir veljavnega designa.

**Avtoritativni design dokazi:**

1. Founder potrjene odločitve,
2. izvorne Claude Design HTML datoteke,
3. zaslonski posnetki potrjenih verzij,
4. design-review dokumenti v ODS.

---

## DR-006 — Visual design foundation

**Status:** FOUNDER APPROVED

**Odločitev:** Concept A ostaja vizualna osnova prvega zaslona.

Potrjene značilnosti:

- zelo čist in miren videz,
- močna tipografska hierarhija,
- veliko praznega prostora,
- brez nepotrebne vizualne kompleksnosti,
- jasen enostopenjski izbor začetne poti,
- zaupanje in razumljivost pred dekoracijo.

---

## DR-007 — Calm Intelligence

**Status:** FOUNDER APPROVED

**Odločitev:** Med tremi predstavljenimi brand smermi je bila izbrana:

**1a — Calm Intelligence**

Zavrnjeni kot primarni smeri:

- Human Finance,
- Premium Guidance.

Calm Intelligence mora podpirati Concept A, ne pa ga nadomestiti z novim redesignom.

---

## DR-008 — Direction A+ elementi

**Status:** PROPOSED ONLY

Naslednji elementi so bili predlagani, vendar še niso potrjeni kot celota:

- Northlight barva,
- Certainty Arc,
- sharp-corner rule,
- poseben prikaz decimalnih mest,
- linearni loading indikator,
- underline confirmation feedback.

Ti elementi se ne smejo vključiti v uradni design system brez ločene Founder odločitve in tehnične presoje.

Posebej je Certainty Arc odprt zaradi vprašanja, ali lahko NorthStar zanesljivo in razumljivo prikazuje dejansko stopnjo AI gotovosti.

---

## DR-009 — Razmerje med Product Home in Housing Loan Upload

**Status:** VERIFIED

**Odločitev:** Product Home in Housing Loan Upload Screen 1 nista isti zaslon.

- **Product Home** je splošni prvi zaslon s štirimi primarnimi vstopnimi točkami.
- **Housing Loan Upload Screen 1** je bil ločen zgodovinski design flow za PDF razlago.

Ker PDF flow ni del prve faze, Housing Loan Upload screen trenutno ni del aktivnega first-phase design scopea.

---

## DR-010 — Avtoritativnost zgodovinskih dokumentov

**Status:** FOUNDER APPROVED PRINCIPLE

**Odločitev:** Starejši dokument ali design ne predstavlja avtomatsko veljavnega stanja.

Pri vsaki temi se uporablja naslednja hierarhija:

1. zadnja neposredna Founder odločitev,
2. poznejša dokumentirana sprememba,
3. starejša potrjena odločitev,
4. zgodnji predlog ali ideja.

Kjer zadnje stanje ni dokazljivo, mora dokumentacija uporabljati oznako:

**REQUIRES FOUNDER DECISION**

---

## DR-011 — Arhitektura Affordability

**Status:** FOUNDER APPROVED — CLARIFIED BY DR-013

**Odločitev:** Affordability je skupna arhitekturna capability, ki podpira samostojni produkt prve faze **Koliko kredita si lahko privoščim**.

Produkt **Koliko kredita si lahko privoščim** ima lastno primarno UX-vstopno točko in samostojen uporabniški namen.

Isto affordability logiko lahko uporabljajo tudi:

- Stanovanjski kredit,
- Leasing,
- drugi prihodnji produkti.

Prejšnja formulacija, da Affordability ni samostojen produktni modul, je superseded z [[#DR-013 — Samostojni produkti prve faze in shared capabilities|DR-013]].

---

## DR-012 — Arhitektura Financial Terms

**Status:** FOUNDER APPROVED — CLARIFIED BY DR-013

**Odločitev:** Financial Terms je shared educational capability, ki podpira samostojni produkt prve faze **Pojasni pojme**.

Produkt **Pojasni pojme** ima lastno primarno UX-vstopno točko in samostojen uporabniški namen.

Isti enotni vir finančnih izrazov in razlag lahko uporabljajo tudi:

- Stanovanjski kredit,
- Leasing,
- drugi prihodnji produkti.

Razlage se ne smejo po nepotrebnem podvajati po posameznih produktih, kadar lahko uporabljajo isti skupni vir.

Prejšnja formulacija, da Financial Terms ni samostojen produktni modul, je superseded z [[#DR-013 — Samostojni produkti prve faze in shared capabilities|DR-013]].

---

## DR-013 — Samostojni produkti prve faze in shared capabilities

**Status:** FOUNDER APPROVED

**Odločitev:** NorthStar ima v prvi fazi štiri samostojne produkte:

1. Stanovanjski kredit
2. Leasing
3. Koliko kredita si lahko privoščim
4. Pojasni pojme

Produkta **Koliko kredita si lahko privoščim** in **Pojasni pojme** sta na produktni in UX ravni samostojna produkta prve faze, enakovredna Stanovanjskemu kreditu in Leasingu.

Na tehnični ravni lahko oba uporabljata shared capability oziroma skupno logiko, skupne podatkovne modele ali skupne vsebinske vire. Isto shared logiko lahko uporabljajo tudi drugi produkti — najprej Stanovanjski kredit, pozneje Leasing in prihodnji produkti.

Tehnična ponovna uporaba (shared capability) ne zmanjšuje statusa teh dveh produktov kot samostojnih produktov prve faze.

**Shared capability** in **samostojen produkt** sta ločena pojma:

- Shared capability opisuje tehnično/arhitekturno raven ponovne uporabe logike.
- Samostojen produkt opisuje produktno in UX raven — lastno primarno vstopno točko in samostojen uporabniški namen.

Ta odločitev nadomešča prejšnjo formulacijo v [[#DR-011 — Arhitektura Affordability|DR-011]] in [[#DR-012 — Arhitektura Financial Terms|DR-012]], da Affordability in Financial Terms nista samostojna produktna modula.

---

## DR-014 — Release struktura prve faze

**Status:** FOUNDER APPROVED

**Odločitev:** NorthStar prva faza vsebuje vse štiri samostojne produkte, vendar prvi javni MVP release ne vključuje vseh štirih v enaki globini.

### Prvi javni MVP release

V prvi javni MVP release vstopijo:

1. **Koliko kredita si lahko privoščim**
   - jedrni produkt prvega releasea;
   - MVP scope produkta je določen v [[#DR-016 — MVP scope produkta Koliko kredita si lahko privoščim|DR-016]].

2. **Pojasni pojme**
   - jedrni produkt prvega releasea;

3. **Stanovanjski kredit**
   - omejena začetna različica;
   - brez PDF Offer Explanation oziroma bančne PDF analize;
   - njegov omejeni feature scope za prvi javni MVP release je določen v [[#DR-015 — Omejeni scope Stanovanjskega kredita v prvem javnem MVP releaseu|DR-015]] in ga mora MVP dokument povzeti.

### Naslednji release znotraj prve faze

4. **Leasing**
   - ostane samostojen produkt prve faze;
   - ni del prvega javnega MVP releasea;
   - vstopi v naslednji release znotraj prve faze;
   - pred implementacijo potrebuje podrobno Leasing specifikacijo;
   - stanje Leasing kartice v prvem javnem MVP releaseu je določeno v naslednjem podrazdelku.

### Leasing card state in the first public MVP release

- Leasing ostaja eden od štirih produktov na prvem zaslonu.
- V prvem javnem MVP releaseu njegova kartica še ne odpira produkta.
- Oznaka `Kmalu` mora biti vidna.
- Kartica mora biti vizualno in vedenjsko jasno neaktivna.
- Uporabnik mora razumeti, da produkt prihaja pozneje.
- To ni odstranitev Leasinga iz prve faze.

### Pojasnilo

- `Prva faza` je širši produktni okvir.
- `Prvi javni MVP release` je prvi dejansko objavljeni podnabor te faze.
- Prva faza lahko vsebuje več zaporednih releaseov.
- Odložitev Leasinga v naslednji release ne zmanjšuje njegovega statusa samostojnega produkta prve faze.
- PDF Offer Explanation ostaja izključen skladno z [[#DR-002 — Razlaga bančne ponudbe in PDF flow|DR-002]].

---

## DR-015 — Omejeni scope Stanovanjskega kredita v prvem javnem MVP releaseu

**Status:** FOUNDER APPROVED

**Odločitev:** Produkt **Stanovanjski kredit** je v prvem javnem MVP releaseu prisoten kot omejena začetna različica.

### Vključeno

1. **Learn**
   - kratke, strukturirane in razumljive vsebine o osnovah stanovanjskega kredita;

2. **Monthly Payment Examples**
   - preprosti izobraževalni primeri mesečnega obroka;
   - rezultati so približni;
   - ne predstavljajo bančnega izračuna, ponudbe ali finančnega svetovanja;

3. povezava na samostojni produkt **Koliko kredita si lahko privoščim**;

4. povezava na samostojni produkt **Pojasni pojme**.

### Izključeno iz prvega javnega MVP releasea

- Ask AI;
- PDF Offer Explanation;
- primerjava več ponudb;
- personalizirano učenje;
- priprava na sestanek z banko;
- napredne simulacije;
- uporabniški račun;
- shranjena zgodovina.

### Arhitekturna in produktna meja

- Stanovanjski kredit ne podvaja Affordability ali Financial Terms funkcionalnosti.
- Uporabnika usmeri na samostojna produkta:
  - **Koliko kredita si lahko privoščim**
  - **Pojasni pojme**
- Shared capabilities lahko obstajajo v ozadju, vendar produktni UX ostaja ločen.
- Ta odločitev določa samo prvi javni MVP release in ne predstavlja prihodnjega Roadmapa.

### Trust omejitve

- Monthly Payment Examples morajo biti jasno označeni kot izobraževalni in približni.
- Ne smejo ustvarjati vtisa bančne ponudbe, jamstva ali osebnega finančnega svetovanja.
- PDF analiza in Ask AI nista del tega releasea.

---

## DR-016 — MVP scope produkta Koliko kredita si lahko privoščim

**Status:** FOUNDER APPROVED

**Odločitev:** Produkt **Koliko kredita si lahko privoščim** je jedrni produkt prvega javnega MVP releasea in uporabniku poda previdno, razumljivo oceno varnega mesečnega obroka ter okvirnega razpona kredita.

### Uporabniški vnosi

Potrjeni vnosi:

- mesečni neto prihodek gospodinjstva;
- velikost gospodinjstva;
- obstoječi krediti, leasingi in druge redne mesečne pogodbene obveznosti;
- mesečni življenjski stroški;
- želeni oziroma največji rok kredita;
- okvirna obrestna mera ali jasno prikazan privzeti izobraževalni primer.

### Ocena življenjskih stroškov

- NorthStar predlaga varno minimalno oceno glede na velikost gospodinjstva.
- Uporabnik jo lahko popravi.
- Predlog in uporabljene predpostavke morajo biti jasno prikazani.
- Ta odločitev ne določa še konkretnih številčnih pragov ali državne metodologije.
- Konkretna metodologija zahteva ločeno specifikacijo in validacijo.

### Redne mesečne obveznosti

Vključujejo najmanj:

- obstoječe kreditne obroke;
- leasing obroke;
- relevantna mesečna bremena kartic ali limitov;
- preživnine;
- druge pogodbene mesečne dolgove ali obveznosti.

Priporočena jasna uporabniška oznaka:

`Obstoječi krediti, leasingi in druge redne mesečne obveznosti`

### Rezultat

- Varen razpon mesečnega obroka.
- Okviren razpon možne vrednosti kredita.
- Preostanek denarja po obroku, življenjskih stroških in drugih obveznostih.
- Razumljiva ocena: bolj varno, napeto, previsoko tveganje.
- Prikaz ključnih predpostavk.

Rezultat je razpon; en sam navidezno natančen znesek ni dovoljen kot glavni rezultat.

### Obvezni vizualni prikaz rezultata

- MVP mora poleg številčnega rezultata vključevati preprost in razumljiv vizualni graf.
- Graf ni nova metodologija ali ločen izračun, ampak vizualni prikaz istega potrjenega rezultata.
- Prikazati mora najmanj:
  - varen razpon mesečnega obroka;
  - uporabnikov izbrani ali preizkušeni mesečni obrok;
  - mejo oziroma območje, kjer rezultat postane napet;
  - območje previsokega tveganja.
- Uporabnik mora iz grafa takoj razumeti, kam se njegov izbrani obrok uvršča.
- Vizualizacija mora jasno razlikovati med: bolj varno, napeto, previsoko tveganje.
- Graf ne sme ustvarjati vtisa matematične ali bančne gotovosti.

Drugi obvezni vizualni prikaz oziroma del istega rezultata — razporeditev mesečnega denarja, ki pokaže:

- mesečni neto prihodek gospodinjstva;
- življenjske stroške;
- obstoječe kredite, leasinge in druge obveznosti;
- predvideni novi mesečni obrok;
- preostanek oziroma varnostno rezervo.

Vizualizacija mora ostati zelo preprosta:

- brez kompleksnih krivulj, finančnega žargona ali preveč podatkov;
- namen je razumevanje, ne dekoracija;
- graf mora biti razumljiv uporabniku brez finančnega znanja;
- natančna oblika grafa, barve, pragovi in interakcije še niso določeni;
- te podrobnosti zahtevajo ločeno UX in metodološko specifikacijo.

### Trust omejitve

- Rezultat ni bančna odobritev.
- Ni uradna presoja kreditne sposobnosti.
- Ni osebno finančno svetovanje.
- Ne napoveduje odobritve posamezne banke.
- Mora razkriti uporabljeno obrestno mero, rok, stroške, obveznosti in varnostno rezervo.

### Izključeno

- Povezovanje z bankami.
- Dejansko preverjanje kreditne sposobnosti.
- Avtomatski uvoz bančnih podatkov.
- Uporabniški račun.
- Shranjevanje izračunov.
- AI klepet.
- Priporočanje konkretne banke ali kredita.
- Napoved odobritve.

### Odprta izvedbena vprašanja

Še niso določeni:

- konkretna formula;
- konkretni varnostni pragovi;
- konkretna minimalna ocena življenjskih stroškov;
- državna lokalizacija metodologije;
- validacijski in testni podatki.

Ta vprašanja zahtevajo ločeno specifikacijo in ne smejo biti določena v Decision Registerju brez dodatne presoje.

---

# Resolved Questions

## OQ-001 — Arhitektura Affordability

**Status:** RESOLVED by DR-011 and DR-013

Affordability je shared capability, ki podpira samostojni produkt prve faze **Koliko kredita si lahko privoščim**.

## OQ-002 — Arhitektura Financial Terms

**Status:** RESOLVED by DR-012 and DR-013

Financial Terms je shared educational capability, ki podpira samostojni produkt prve faze **Pojasni pojme**.

---

## Reference / Evidence

- [[Housing Loans Specification]] — `01 Product/Housing Loans Specification.md`
- [[User Journey Specification]] — `01 Product/User Journey Specification.md`
- [[User Flow Specification]] — `01 Product/User Flow Specification.md`
- [[Features]] — `01 Product/Features.md`
- [[Design Bible]] — `02 Design/Design Bible.md`
- Design Decisions — `04 Design Deliverables/Reviews/Design Decisions.md`
- Recommendation — `04 Design Deliverables/Reviews/Recommendation.md`
- Self Critique — `04 Design Deliverables/Reviews/Self Critique.md`
- Session Summary — `04 Design Deliverables/Archive/Session Summary.md`
