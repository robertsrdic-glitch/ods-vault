# NorthStar MVP

Version: 0.1
Status: Draft
Founder: Robert
Product: NorthStar
Last updated: 2026-07-20

Related Documents:
- [[Decision Register]]
- [[Features]]
- [[Housing Loans Specification]]
- [[User Journey Specification]]
- [[User Flow Specification]]
- [[Product Bible]]
- [[Design Bible]]

---

## 1. Namen dokumenta

Ta dokument definira prvi javni NorthStar MVP release, izključno na podlagi že Founder-approved odločitev v [[Decision Register]] (DR-013, DR-014, DR-015, DR-016) in v [[Features]]. Dokument ne uvaja novih produktnih odločitev — kjer odločitev še ni bila sprejeta, je to izrecno označeno kot `REQUIRES FOUNDER DECISION`.

Trije pojmi se v tem dokumentu dosledno razlikujejo:

- **Prva faza** — širši produktni okvir, ki vsebuje vse štiri samostojne produkte (DR-013).
- **Prvi javni MVP release** — prvi dejansko objavljeni podnabor prve faze (DR-014); ne vključuje vseh štirih produktov v enaki globini.
- **Naslednji releasi znotraj prve faze** — poznejši releasi, ki dokončajo obseg prve faze (npr. aktivacija Leasinga).

---

## 2. MVP cilj

MVP mora uporabniku pomagati:

- bolje razumeti finančno odločitev, preden jo sprejme;
- oceniti varen okvir mesečnega obroka;
- razumeti osnovne finančne pojme brez žargona;
- razumeti osnovne elemente stanovanjskega kredita;
- preprečiti lažno gotovost in preobremenitev z informacijami.

MVP je usklajen z naslednjimi vodilnimi principi:

- **Trust before Profit** — noben element MVP-ja ne sme delovati kot prodajni ali monetizacijski pritisk na račun uporabnikovega zaupanja.
- **Clarity before Complexity** — vsak rezultat, razlaga ali graf mora biti razumljiv brez finančnega predznanja.
- **Education before Recommendation** — NorthStar razlaga in ocenjuje, ne priporoča konkretnih bank ali kreditov (DR-015, DR-016).
- **Privacy First** — MVP ne zahteva računa, ne shranjuje podatkov in ne uvaža bančnih podatkov (razdelek 6).

---

## 3. Produktna struktura prve faze

Per [[Decision Register]] DR-013, NorthStar ima v prvi fazi štiri samostojne produkte:

1. **Stanovanjski kredit**
2. **Leasing**
3. **Koliko kredita si lahko privoščim**
4. **Pojasni pojme**

Vsi štirje so na produktni in UX ravni samostojni produkti prve faze — enakovredni, z lastno primarno vstopno točko na prvem zaslonu (DR-001). To ostaja ločeno od tehnične ravni: produkta *Koliko kredita si lahko privoščim* in *Pojasni pojme* lahko v ozadju uporabljata shared capabilities (Affordability, Financial Terms), ki jih lahko sčasoma uporabljajo tudi drugi produkti. Shared capability je tehnični/arhitekturni pojem; samostojen produkt je produktni/UX pojem — ta dva se ne mešata (DR-013).

---

## 4. Prvi javni MVP release

Per DR-014, prvi javni MVP release vsebuje **Koliko kredita si lahko privoščim** in **Pojasni pojme** kot jedrna produkta, ter **Stanovanjski kredit** kot omejeno začetno različico. **Leasing** ni del tega releasea (glej 4.4).

### 4.1 Koliko kredita si lahko privoščim

Jedrni produkt prvega javnega MVP releasea (DR-016).

#### Uporabniški vnosi

- mesečni neto prihodek gospodinjstva;
- velikost gospodinjstva;
- obstoječi krediti, leasingi in druge redne mesečne pogodbene obveznosti;
- mesečni življenjski stroški;
- želeni oziroma največji rok kredita;
- okvirna obrestna mera ali jasno prikazan privzeti izobraževalni primer.

#### Predlagana ocena življenjskih stroškov

- NorthStar predlaga varno minimalno oceno glede na velikost gospodinjstva.
- Uporabnik jo lahko popravi.
- Predlog in uporabljene predpostavke morajo biti transparentno prikazani.
- Konkretna metodologija ocene (formula, pragovi, državna lokalizacija) ni del tega dokumenta — glej razdelek 8.

#### Rezultat

- varen razpon mesečnega obroka;
- okviren razpon možne vrednosti kredita;
- preostanek denarja po obroku, življenjskih stroških in drugih obveznostih;
- razumljiva ocena: bolj varno / napeto / previsoko tveganje;
- prikaz ključnih predpostavk.

Rezultat je razpon; en sam navidezno natančen znesek ni dovoljen kot glavni rezultat (DR-016).

#### Obvezna vizualizacija

MVP mora poleg številčnega rezultata vključevati preprost, obvezen vizualni prikaz istega rezultata — ne novo metodologijo ali ločen izračun:

- graf varnega razpona mesečnega obroka;
- uporabnikov izbrani ali preizkušeni obrok;
- območje bolj varno;
- območje napeto;
- območje previsoko tveganje.

Drug obvezni del istega prikaza — razporeditev mesečnega denarja:

- prihodek;
- življenjski stroški;
- obstoječe obveznosti;
- novi obrok;
- preostanek oziroma varnostna rezerva.

Vizualizacija mora ostati preprosta in razumljiva uporabniku brez finančnega znanja, brez kompleksnih krivulj ali finančnega žargona. Konkretna oblika grafa, barve, pragovi in interakcije še niso določeni — glej razdelek 8.

#### Trust omejitve

- rezultat ni bančna odobritev;
- ni uradna presoja kreditne sposobnosti;
- ni osebno finančno svetovanje;
- ne napoveduje odobritve posamezne banke;
- ne priporoča konkretne banke ali kredita.

### 4.2 Pojasni pojme

Jedrni produkt prvega javnega MVP releasea, s potrjenim namenom in produktnim statusom (DR-004, DR-012, DR-013). Osnovni namen: preproste razlage finančnih pojmov brez žargona, ki jih lahko sčasoma uporabljajo tudi drugi produkti (shared Financial Terms capability). MVP scope in country content model produkta sta določena v DR-017.

#### Tržni in vsebinski obseg

- Prvi javni MVP podpira samo Slovenijo.
- Uporablja `Slovenia Country Content Pack`.
- Vsebuje približno 30–50 kuriranih, visoko prioritetnih finančnih pojmov.
- Natančen, Founder-potrjen seznam pojmov še ni določen.

#### Osnovna funkcionalnost

- iskalno polje;
- preproste kategorije;
- dostop do posamezne razlage pojma;
- povezave med sorodnimi pojmi.

#### Struktura posamezne razlage

Vsaka razlaga mora vsebovati najmanj:

1. kratko razlago v preprostem jeziku;
2. konkreten primer;
3. pojasnilo, zakaj je pojem pomemben;
4. povezane pojme.

#### Country Content Pack model

- Vsebine so organizirane po državnih paketih.
- Nekateri pojmi imajo skupno konceptualno osnovo, vendar imajo lahko državne pravne, regulativne, davčne, bančne ali potrošniške posebnosti.
- Vsebin za novo državo ni dovoljeno ustvariti samo z avtomatskim prevodom obstoječega paketa.
- Vsak prihodnji country pack zahteva lokalno raziskavo, lokalizacijo, preverjanje in odobritev.
- Arhitekturna pripravljenost za prihodnje države ne pomeni, da so te države del prvega javnega MVP scopea.

#### Vloga AI

AI lahko pomaga pri:

- raziskovanju;
- iskanju in primerjavi uradnih oziroma avtoritativnih virov;
- pripravi osnutkov;
- poenostavitvi razlage;
- pripravi primerov;
- zaznavanju možnih državno-specifičnih razlik.

AI ne sme:

- samodejno objaviti vsebine;
- sam potrditi pravne ali finančne pravilnosti;
- nadomestiti uredniškega pregleda;
- ustvarjati sprotnih generativnih razlag uporabnikom v MVP produktu.

#### Obvezna publishing in validacijska pregrada

Pred objavo mora proces vključevati:

1. raziskavo;
2. evidentiranje virov;
3. preverjanje virov;
4. vsebinski oziroma uredniški pregled;
5. odobritev;
6. evidentiran datum zadnje validacije.

#### Shared capability meja

- Ista kurirana zbirka pojmov se lahko ponovno uporabi znotraj produkta Stanovanjski kredit kot shared Financial Terms capability.
- Ta ponovna uporaba ne spreminja statusa Pojasni pojme kot samostojnega produkta prve faze.

#### Izključeno iz prvega javnega MVP releasea

- AI klepet;
- avtomatsko generiranje odgovorov ali razlag za uporabnika;
- avtomatska AI objava;
- uporabniški račun;
- shranjeni priljubljeni pojmi;
- personalizirane razlage;
- uporabniško ustvarjene vsebine;
- country packi zunaj Slovenije;
- avtomatsko prevajanje kot nadomestilo za lokalno raziskavo in validacijo.

#### Odprta vprašanja

`REQUIRES FOUNDER DECISION`

Naslednje podrobnosti ostajajo odprte in jih ta dokument ne sme sam določiti:

- natančen seznam približno 30–50 pojmov;
- konkretne kategorije;
- kriteriji za prioritizacijo pojmov;
- natančni uradni viri za posamezni pojem;
- uredniški in review proces;
- odgovornost za končno odobritev vsebine;
- natančen UX iskanja in navigacije;
- tehnični format country packa;
- accessibility zahteve;
- način rednega ponovnega preverjanja zastarelih vsebin.

### 4.3 Stanovanjski kredit

Omejena začetna različica v prvem javnem MVP releaseu (DR-015).

**Vključeno:**

- **Learn** — kratke, strukturirane in razumljive vsebine o osnovah stanovanjskega kredita. *(Candidate pending MVP confirmation — glej [[Features]].)*
- **Monthly Payment Examples** — preprosti izobraževalni primeri mesečnega obroka; rezultati so približni in ne predstavljajo bančnega izračuna, ponudbe ali finančnega svetovanja. *(Candidate pending MVP confirmation — glej [[Features]].)*
- Povezava na samostojni produkt **Koliko kredita si lahko privoščim**.
- Povezava na samostojni produkt **Pojasni pojme**.

Stanovanjski kredit ne podvaja Affordability ali Financial Terms funkcionalnosti — uporablja ju prek povezave na oba samostojna produkta (DR-015).

**Izključeno iz prvega javnega MVP releasea:**

- Ask AI;
- PDF Offer Explanation oziroma bančna PDF analiza;
- primerjava več ponudb;
- personalizirano učenje;
- priprava na sestanek z banko;
- napredne simulacije;
- uporabniški račun;
- shranjena zgodovina.

**Trust omejitve za Monthly Payment Examples:**

- morajo biti jasno označeni kot izobraževalni in približni;
- ne smejo ustvarjati vtisa bančne ponudbe, jamstva ali osebnega finančnega svetovanja.

### 4.4 Leasing

- Samostojen produkt prve faze (DR-013).
- Ni aktiven v prvem javnem MVP releaseu (DR-014).
- Kartica ostane vidna na prvem zaslonu, med štirimi primarnimi vstopnimi točkami.
- Kartica ima oznako `Kmalu`.
- Kartica je vizualno in vedenjsko jasno neaktivna — ne sme delovati kot pokvarjen ali nedelujoč gumb.
- Uporabnik mora razumeti, da produkt prihaja pozneje; to ni odstranitev Leasinga iz prve faze.
- Aktivacija sledi v naslednjem releaseu znotraj prve faze, po pripravi podrobne Leasing specifikacije, ki še ne obstaja.

---

## 5. Izključeno iz prvega javnega MVP releasea

Konsolidiran seznam potrjeno izključenih funkcij:

- PDF Offer Explanation oziroma bančna PDF analiza (DR-002, DR-015, DR-016);
- Ask AI (DR-015, DR-016);
- bančne integracije oziroma povezovanje z bankami (DR-016);
- avtomatski uvoz bančnih podatkov (DR-016);
- uradno oziroma dejansko preverjanje kreditne sposobnosti (DR-016);
- priporočanje konkretne banke ali kredita (DR-015, DR-016);
- napoved bančne odobritve (DR-016);
- uporabniški računi (DR-015, DR-016);
- shranjena zgodovina (DR-015);
- shranjevanje izračunov (DR-016);
- primerjava ponudb (DR-015);
- napredne simulacije (DR-015);
- personalizirano učenje (DR-015);
- priprava na sestanek z banko (DR-015);
- Leasing kot aktiven produkt (DR-014, glej 4.4).

---

## 6. Privacy in podatkovne meje

Prvi javni MVP release deluje brez:

- uporabniških računov;
- shranjene zgodovine;
- shranjevanja izračunov;
- avtomatskega uvoza bančnih podatkov;
- povezovanja z bankami.

Konkretna tehnična privacy arhitektura (npr. kako in kje se podatki obdelujejo med sejo) ni del tega dokumenta in zahteva ločeno inženirsko specifikacijo.

---

## 7. MVP uspeh

Kvalitativni kriteriji uspeha, izpeljani iz NorthStar principov (razdelek 2):

- uporabnik razume prikazani rezultat;
- uporabnik razume, zakaj je določen obrok bolj varen, napet ali previsoko tvegan;
- uporabnik razume uporabljene predpostavke (prihodek, stroški, obveznosti, obrestna mera);
- rezultat ne ustvarja lažne gotovosti (razpon, ne en sam navidezno natančen znesek);
- uporabnik brez finančnega znanja lahko samostojno dokonča glavni flow (vnos → rezultat → graf).

Številčni KPI-ji (npr. konverzija, čas na strani, število zaključenih sej):

`REQUIRES FOUNDER DECISION`

---

## 8. Odprte odločitve pred implementacijo

### Affordability metodologija

- konkretna formula za izračun varnega razpona;
- konkretni varnostni pragovi (kaj šteje za "bolj varno" / "napeto" / "previsoko tveganje");
- konkretna minimalna ocena življenjskih stroškov;
- državna lokalizacija metodologije;
- validacijski in testni podatki.

### Pojasni pojme

- točen MVP obseg;
- začetni nabor pojmov;
- način iskanja in navigacije;
- ali gre samo za kurirane vsebine ali tudi za dodatno funkcionalnost.

### Vizualizacija

- natančna oblika grafa (tip vizualizacije);
- konkretni pragovi za prehode med območji;
- barve;
- interakcije;
- accessibility zahteve.

### Monetizacija

`REQUIRES FOUNDER DECISION`

Monetizacija (vključno z AdSense ali drugimi modeli) ni formalno potrjena v nobenem trenutnem avtoritativnem dokumentu ([[Decision Register]], [[Features]]) in zato ni del tega MVP obsega. O njej mora odločiti Founder ločeno.

---

## 9. MVP Definition of Done

MVP je vsebinsko pripravljen za implementacijsko načrtovanje šele, ko:

- je scope vseh aktivnih produktov (Koliko kredita si lahko privoščim, Pojasni pojme, Stanovanjski kredit) dokončno določen;
- je affordability metodologija ločeno specificirana in validirana;
- je MVP scope produkta Pojasni pojme Founder-approved;
- je UX flow za vse aktivne produkte dokumentiran;
- so trust opozorila za vsak produkt definirana;
- je vizualizacija (oblika, pragovi, barve, interakcije, accessibility) specificirana;
- so odprte pravne in privacy zahteve pregledane;
- ni nerešenih kritičnih Founder odločitev iz razdelka 8.

Dokler karkoli od zgornjega ostaja odprto, MVP **ni** pripravljen za implementacijo.

---

## 10. Reference

- [[Decision Register]] — `01 Product/Decision Register.md`
- [[Features]] — `01 Product/Features.md`
- [[Housing Loans Specification]] — `01 Product/Housing Loans Specification.md`
- [[User Journey Specification]] — `01 Product/User Journey Specification.md`
- [[User Flow Specification]] — `01 Product/User Flow Specification.md`
- [[Product Bible]] — `01 Product/Product Bible.md`
- [[Design Bible]] — `02 Design/Design Bible.md`
