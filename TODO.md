# VoxOne_M1 — TODO / notatnik główny projektu PCB

**Wersja notatnika:** 1.1 — GitHub  
**Utworzono:** 2026-10-17  
**Projekt:** VoxOne_M1 — samodzielna rewizja sprzętowa M1  
**Środowisko:** Windows 10 (laptop), KiCad 10.0.4, lokalny Codex CLI + KiCad Copilot MCP  
**Ostatni etap wykonany przez Codexa:** `PCB-LAYOUT-3` na gałęzi `pcb-layout-3` (wciąż PROVISIONAL; niezatwierdzony do trasowania). `main` jest chronionym punktem odniesienia CAD.  
**Bieżące źródła CAD:** GitHub `pimowo/VoxOnePCB`, `main`, bazowy commit `8d90e6df444f770a445944372fa62b5ebb39af9` (KiCad + biblioteki). Archiwalna kopia ostatniej rewizji pozostaje lokalnie w `%USERPROFILE%\Documents\VoxOne_M1_FOOTPRINT-2`.  
**Kanoniczne dokumenty projektu:** `TODO.md` i `AGENTS.md` w głównym katalogu `pimowo/VoxOnePCB` na gałęzi `main`.  
**Stan:** PCB-LAYOUT-3 jest wariantem roboczym na osobnej gałęzi, a jego rozmieszczenie nie otrzymało zgody na trasowanie. Użytkownik wybrał nowy cel: **PCB prostokątna pozioma (szerokość większa niż wysokość), oba wymiary ≤100 mm**. Najpierw sprawdzić wykonalność mechaniczną — dokładnych wymiarów NIE zatwierdzono. **NIE WOLNO** trasować ani produkować PCB bez kolejnej decyzji.

> **To jest kanoniczna lista decyzji, zadań, ryzyk i wytycznych VoxOne_M1.** Nie mylić z `docs/TODO.md` repozytorium firmware VoxOne — to osobny projekt. Nie wykreślać pomysłów bez decyzji użytkownika. Nie traktować założeń referencyjnych jako pomiarów rzeczywistego sprzętu.
>
> **Nie przygotowywać nowych promptów dla Codexa ani nie uruchamiać kolejnej rewizji/layoutu/trasowania, dopóki użytkownik sam o to nie poprosi.**

## 0. Jak korzystać z notatnika (użytkownik, ChatGPT, Codex)

1. Przed nowym etapem **przeczytaj całe `TODO.md`** oraz odpowiednie raporty z ostatniej rewizji. Plik `AGENTS.md` w tym samym katalogu przypomina Codexowi o tej zasadzie.
2. Po każdej **wyraźnie zatwierdzonej** decyzji dopisz lub zmodyfikuj zadanie, datę, status i ewentualne konsekwencje. Nie nadpisuj ustaleń domysłami.
3. Statusy: `DONE` = wykonane/sprawdzone; `APPROVED` = zatwierdzone wymaganie, niekoniecznie wdrożone; `TODO` = do wykonania; `BLOCKED` = wymaga dowodu/decyzji; `LATER` = dalszy etap; `REJECTED` = odrzucone.
4. **Kanoniczny `TODO.md` i `AGENTS.md` przechowuj w katalogu głównym repozytorium `pimowo/VoxOnePCB` na `main`.** Pracuj na lokalnej kopii tego repozytorium; po zatwierdzonym etapie aktualizuj tylko jej `TODO.md`, wykonaj commit i push za zgodą użytkownika. Starsze katalogi KiCad zachowuj jako archiwa, nie jako kolejne niezależne notatniki.
5. Każda zakończona rewizja ma mieć odrębny katalog, checkpoint/ZIP oraz **pełny raport Codexa zapisany do unikatowego pliku `ETAP_ODPOWIEDZ_CODEX.md`**. Nie nadpisuj poprzednich raportów. Porównuj netlisty i rzeczywiste ERC/DRC, a nie tylko liczby ze starych raportów.
6. Nie wprowadzaj niezatwierdzonych zmian wartości, GPIO, typu złączy, zasilania ani architektury. Nie usuwaj problemów ERC/DRC przez wyłączanie kontroli lub fikcyjne dopasowania.
7. W dokumentach i renderach oddzielaj **wizualizację/koncepcję**, **wstępny projekt KiCad**, **zweryfikowaną mechanikę** i **gotowość produkcyjną**.

## 1. Najważniejsze najnowsze decyzje — obowiązujące

| Status | Decyzja / wymaganie |
|---|---|
| APPROVED | Laminat M1 **maksymalnie 100 × 100 mm**, cztery otwory M3 przy narożnikach. |
| APPROVED — 2026-10-18 | **Wybór prostokątnej PCB poziomej, szerszej niż wyższej**, na wzór wcześniej dostarczonej wizualizacji. Wymiary każdego boku ≤100 mm. **Nie ustalać docelowej długości/wysokości przed analizą wykonalności footprintów, RF, USB, jack, M3, kabli, złącz i możliwości montażu.** |
| PENDING | Konkretne wymiary prostokąta pozostają **niezatwierdzone**. Nie domniemywać 100×75, 100×80 lub 100×90 mm; rozpatrywać je wyłącznie jako warianty kontrolne. Jeżeli kształt wymaga mechanicznych kompromisów, przedstawić je użytkownikowi zamiast ukrywać. |
| APPROVED | **2 warstwy miedzi F.Cu/B.Cu (TOP + BOTTOM)**, dopuszczone przelotki i ścieżki na obu stronach. |
| APPROVED | **WSZYSTKIE elementy wyłącznie po górnej stronie PCB (TOP/F.Cu)**: SMD, THT, podstawki, moduły, złącza, zworki. Brak elementów montowanych po stronie BOTTOM. Nóżki THT są oczywiście lutowane od spodu. |
| APPROVED | **Rozmieszczenie ma nawiązywać do wcześniejszej estetycznej wizualizacji VoxOne_M1** udostępnionej w rozmowie (zielona PCB, moduły MAIN po lewej, DAC u góry, BT po prawej, RTC bliżej środka, uporządkowany dół). To inspiracja, nie gwarantowany układ mechaniczny. |
| REJECTED | **PCB-PREVIEW-1** — obecne położenie elementów *nie jest zatwierdzone*; nie może być podstawą do automatycznego routingu. Zachowujemy jednak sprawdzone połączenia, biblioteki i footprinty jako materiał wejściowy. |
| APPROVED | Przy następnym rozmieszczaniu preferować czytelne bloki, prosty montaż/serwis, łatwy dostęp do USB-C, jacka, goldpinów, zworek i anten. **Nie chować drobnicy pod modułami**, jeżeli utrudnia dostęp, naprawę lub narusza prześwit. |
| APPROVED | Sygnały logiki wyświetlaczy 3,3 V; zworki wybierają **wyłącznie VCC 3,3/5 V**. Magistrala I2C bez BSS138. Nie wolno podciągać SDA/SCL do 5 V także przy zasilaniu modułu 5 V. |
| APPROVED | Pull-up I2C R604/R605 po 4,7 kΩ do 3V3_MAIN, niezależne zworki ON/OFF na JP602 2×2: SDA piny 1–2, SCL 3–4. |
| APPROVED | RTC DS3231 mini: zwykły męski goldpin 1×5/2,54 mm, fabryczne gniazdo modułu i bateria bez zmian; pin 4 = NC. |
| REJECTED | Wyświetlacz ST7920 128×64 — nie dodawać jego obsługi, adapterów ani zmian SPI tylko dla niego. |
| APPROVED | **Na razie bez kolejnego promptu dla Codexa** — użytkownik wskaże, kiedy kontynuować. |

## 2. Rejestr zadań — kolejność wykonywania

### P0 — następna rewizja rozmieszczenia (dopiero na polecenie użytkownika)

- [ ] **M1-P0-01** — Utworzyć nowy katalog rewizji z checkpointem `VoxOne_M1_FOOTPRINT-2`; zachować kopię `TODO.md`, `AGENTS.md` i raport stanu. Nie naruszyć wcześniejszych rewizji.
- [ ] **M1-P0-02** — Zaprojektować od nowa **rozmieszczenie** 100 × 100 mm, wizualnie bliższe zaakceptowanej koncepcji (MAIN lewa/pionowo, DAC górna prawa, BT prawa, RTC środek, rząd złączy u dołu, ARK lewa krawędź). Rozmieszczenie musi wynikać z rzeczywistych padów, obrysów i stref funkcjonalnych, nie z grafiki koncepcyjnej.
- [ ] **M1-P0-03** — Przenieść **wszystkie 11 elementów SMD z BOTTOM na TOP**, zachowując ich wartości, sieci, orientację funkcjonalną i sprawdzając footprinty. Po zakończeniu liczba elementów BOTTOM **0**.
- [ ] **M1-P0-04** — Wszystkie pozostałe elementy sprawdzić po stronie TOP; preferować brak elementów pod gniazdami MAIN, BT i DAC. Jeśli nie da się uniknąć czegoś pod modułem, przedstawić to użytkownikowi do osobnej zgody.
- [ ] **M1-P0-05** — MAIN: zapewnić dostęp do obu gniazd USB-C od krawędzi lub rzeczywistym wolnym korytarzem, możliwość wyjęcia modułu i odpowiednie miejsce dla anteny. Nie akceptować obecnego położenia wyłącznie dlatego, że padami mieści się w PCB.
- [ ] **M1-P0-06** — VoxOneBT: po prawej stronie, **płasko nad PCB**, dwie *wewnętrzne* listwy 1×10, antena z wolną przestrzenią, port USB dostępny, brak zamiany pinów lewej/prawej listwy.
- [ ] **M1-P0-07** — DAC PCM5102A: górna prawa strefa, jack osiągalny z zewnątrz, dostęp do H1–H4, gniazdo audio L/GND/R sensownie położone. Uzgodnić obrys rzeczywistego modułu i wtyczki.
- [ ] **M1-P0-08** — Złącza I2C, SPI, INPUT, AMP i zworki uporządkować i czytelnie oznaczyć na dolnej krawędzi lub w łatwo dostępnej strefie. Wyjście audio i zasilanie w logicznych miejscach.
- [ ] **M1-P0-09** — Uporządkować grupowanie kondensatorów blisko wejść zasilania modułów, rezystory przy właściwych pinach, analogowe AUDIO poza zakłócającymi sekcjami (RF, BL, zasilanie).
- [ ] **M1-P0-10** — Zweryfikować cztery otwory M3, odstępy pod podkładki/łby, strefy anten, USB/jack + obrysy podłączonych wtyków, zworki i dostęp do montażu. Zgłosić wszystkie wyjątki od 100 × 100 mm (np. wystająca antena modułu) użytkownikowi.
- [ ] **M1-P0-11** — Uporządkować silkscreen: sekcje, `VoxOne_M1`, opis zasilania, numerację i funkcje złączy, JP501/JP502, JP601, JP602, logo, czytelny pin1; usunąć kolizje napisów.
- [ ] **M1-P0-12** — Przygotować faktyczny KiCad `.kicad_pcb`, widok 2D z góry, 3D z góry/pod kątem/z dołu (jeśli model dostępny); wyraźnie ujawnić brakujące / tymczasowe modele 3D. Nie przedstawiać grafiki AI jako dowodu technicznego.
- [ ] **M1-P0-13** — Zrobić ERC, DRC, porównanie netlisty oraz osobne zestawienie niepołączeń. Nie deklarować DRC PASS, dopóki płytka nie jest trasowana. **Bez ścieżek i Gerberów do akceptacji rozmieszczenia.**
- [ ] **M1-P0-14** — Pokazać użytkownikowi rezultat i **poczekać na wyraźną akceptację nowego rozmieszczenia** przed trasowaniem. Dotychczasowe PCB-LAYOUT-2/3 nie mają zgody na routing.
- [ ] **M1-P0-15 [APPROVED — WYMAGANA ANALIZA PRZED PROJEKTEM]** — Sprawdzić fizyczną wykonalność PCB **prostokątnej poziomej ≤100×100 mm** według wizualizacji. Zacząć od pełnych obrysów MAIN/BT/DAC/RTC i ANT keepout, złącz, korytarzy wtyków USB/jack, 4×M3, elementów TOP only i miejsca do wyjmowania modułów. Porównać kilka szerokości/wysokości i realne konflikty; dokładny wymiar dopiero po raporcie i zgodzie użytkownika.
- [ ] **M1-P0-16 [PENDING]** — Zatwierdzić konkretny wymiar prostokąta i rozłożenie modułów **dopiero po** niezależnej analizie mechaniki i dostępu. Zachować elektryczną mapę padów, 77 TOP / 0 BOTTOM, 2 warstwy Cu; bez trasowania i Gerberów przed odrębną akceptacją.

### P1 — do zamknięcia przed zamawianiem / produkcją PCB

- [ ] **M1-P1-01 [BLOCKED]** — Potwierdzić dokładny wariant ESP32-S3 DevKitC-1 N16R8 z 44 pinami i 2×USB-C: rozstaw rzędów, raster, obrys, orientacja pin1, wystawanie USB i anteny. Referencja YD 28×57 mm / 25,40 mm jest **prowizoryczna**, nie uniwersalna.
- [ ] **M1-P1-02 [BLOCKED]** — Potwierdzić wewnętrzne rzędy Wemos D1 mini ESP32 2×10 (źródło biblioteczne: 22,86 mm osiowo, raster 2,54 mm), antenę/USB, wysokość nad PCB i elementy od spodu.
- [ ] **M1-P1-03 [BLOCKED]** — Potwierdzić footprint GY-PCM5102A (1×6 + prostopadłe 1×9), obrys, jack, rozmieszczenie H1–H4; zweryfikować **mapę padów** i kierunek gniazda. Model STEP odrzucony w PREVIEW-1 z powodu złej orientacji — wymaga naprawy lub zamiennika.
- [ ] **M1-P1-04** — RTC: zachować goldpin męski 1×5, pin4 NC, fabryczną baterię; oszacować z rzeczywistego wariantu obrys, położenie baterii i wysokość zestawu. Nie projektować dodatkowych adapterów.
- [ ] **M1-P1-05** — Dobrać rzeczywiste listwy żeńskie i długości pinów MAIN/Wemos/DAC; potwierdzić prześwit i możliwość lutowania/wyjęcia. W PREVIEW-1 założenie **8,5 mm** jest *niepotwierdzone*.
- [ ] **M1-P1-06** — Dobór dostępnych 10 µF / 16 V radial THT pasujących do D5/P2 zamiast referencyjnego Nichicon UPW1C100MDD (EOL); nie zmieniać wartości bez zgody.
- [ ] **M1-P1-07** — Dopasować model 3D C101 do faktycznego 470 µF / 16 V (referencyjnie D10/H12,5; podgląd miał H16). Model F101, Wemos, RTC i DAC uzupełnić lub jawnie zaznaczyć brak.
- [ ] **M1-P1-08** — Zweryfikować F101 T3,15 A / napięcie DC i jego współpracę z ograniczającym zasilaczem 5 V / 3 A. Nie udawać gwarantowanego odcięcia zwarcia.
- [ ] **M1-P1-09** — Sprawdzić ochronę D101 SMBJ5.0A (przepięcia impulsowe, nie długotrwałe OVP), termikę i numerację Q101 FDD6685 TO-252 (G1, D2/tab, S3), ciągłość 5V_SYS.
- [ ] **M1-P1-10** — Bilans prądowy 5 V i **3V3_AUX** (AMS1117-3.3, założenie łącznego poboru ≤150 mA wraz z R101/RTC/wyświetlaczem/BL), stabilność z C105 = 22 µF tantal; test termiczny i rozruch.
- [ ] **M1-P1-11** — Potwierdzić dla **konkretnych klonów** obsługę jednoczesnego USB i zasilania ARK (prądy wsteczne, 5 V/VBUS). Nie dodawać diod/muxów bez nowej decyzji użytkownika.
- [ ] **M1-P1-12** — Sprawdzić stany częściowego zasilania przez UART/I2S/I2C/SPI oraz niezamierzone zasilanie nieaktywnego modułu przez sygnały.
- [ ] **M1-P1-13** — W DAC potwierdzić mostki H1 FLT LOW, H2 DEMP LOW, H4 FMT LOW, **oba H3 rozwarte** dla sterowania XSMT z MAIN. Potwierdzić 5V_DAC na wejściu VIN właściwego wariantu modułu; SCK do GND. Bez modyfikacji zworek na M1.
- [ ] **M1-P1-14** — Wybrać konkretne wyświetlacze 3,3/5 V; sprawdzić poziomy logiczne, **brak pull-up I2C do 5 V**, BL jako zasilanie anody (obecny driver), prąd BL, RESET POR/RC i napięcia przy restarcie ESP.
- [ ] **M1-P1-15** — Przed podłączeniem wzmacniacza wybrać konkretny AMP i potwierdzić polaryzację/fail-safe EN/MUTE, dozwolone napięcie i prąd jego wejść dla open-collector.
- [ ] **M1-P1-16** — Sprawdzić i naprawić wszystkie 84 ostrzeżenia silkscreen PREVIEW-1 bez wyłączania DRC. Po zakończeniu trasowania zamknąć niepołączenia i inne rzeczywiste naruszenia DRC.
- [ ] **M1-P1-17** — Zweryfikować nadające się do produkcji geometrie padów, Gerbery, drill, BOM, lokalne biblioteki i zgodność fizycznych części z footprintami; obowiązkowy przegląd końcowy przed zamówieniem.
- [ ] **M1-P1-18** — Sprawdzić licencje i prawa do kopiowania zewnętrznych footprintów oraz modeli 3D; odnotować atrybucje i źródła w projekcie.
- [ ] **M1-P1-19** — Przygotować testy pierwszego fizycznego prototypu: zwarcia/zasilanie, prądy i temperatury, boot MAIN/BT, I2C RTC/display, SPI/BL/reset, UART/I2S audio, XSMT, AMP_EN/MUTE, zgodność USB + 5 V, Wi-Fi/BT, szumy/trzaski.

### P2 — po zaakceptowanym rozmieszczeniu (nie zaczynać samoczynnie)

- [ ] **M1-P2-01** — Opracować reguły szerokości ścieżek/przelotek i rozkładu 5V_SYS/3V3_AUX/GND oraz ciągłej masy dla 2-warstwowej PCB.
- [ ] **M1-P2-02** — Zaplanować przebieg I2S/UART/I2C/SPI, oddalenie anten i przetwornika audio od zakłóceń, termikę i pola miedzi.
- [ ] **M1-P2-03** — Trasowanie TOP+BOTTOM, bez elementów na BOTTOM, kontrola integralności zasilania i sygnałów.
- [ ] **M1-P2-04** — Pełne DRC/ERC, QA 2D/3D, ocena długości kabli/złącz/obudowy.
- [ ] **M1-P2-05** — Gerber/drill/BOM/rysunki montażowe **dopiero po odrębnym zatwierdzeniu użytkownika**.

### P3 — kwestie firmware i przyszłych funkcji (informacyjnie, poza bieżącym PCB)

- [ ] **M1-P3-01 [LATER]** — Dostosować firmware VoxOne do docelowej nowej mapy GPIO M1 i capabilities profilu.
- [ ] **M1-P3-02 [LATER]** — Wsparcie wyświetlaczy I2C/SPI 3,3 V, konfigurowalne zasilanie VCC i sterowanie BL; reset display RC nie jest sterowany przez GPIO.
- [ ] **M1-P3-03 [LATER]** — VoxOneBT: przyszły I2S MAIN→BT i A2DP Source (TX do słuchawek) z walidacją roli master/slave, obecnie tylko przygotowana linia.
- [ ] **M1-P3-04 [LATER]** — Sprawdzić zachowanie TTS, SourceManager RADIO↔BT, MUTE i głośności na sprzęcie M1.
- [ ] **M1-P3-05 [LATER]** — DSPmini i AUX/PCM1808 należą do projektu **L1**, nie dodawać do M1. SPDIF został wycofany z VoxOne.

## 3. Zatwierdzona architektura elektryczna — nie zmieniać bez decyzji

### 3.1 MAIN ESP32-S3, 44 piny, N16R8

- Wymienny moduł 2×22 z dwoma USB-C. Typ klona i mechanika PCB są jeszcze referencyjne. Nazwy pinów schematu: `J1.1...J1.22`, `J3.1...J3.22`.
- Mapa GPIO MAIN:

| GPIO MAIN | Funkcja |
|---|---|
| 1 / 2 | UART MAIN TX → BT RX / MAIN RX ← BT TX |
| 4 / 5 / 6 | DAC I2S BCLK / LRCK / DOUT |
| 7 | DAC XSMT przez R204 = 100 Ω i pulldown R301 = 10 kΩ |
| 8 / 9 | I2C SDA / SCL (RTC + opcjonalny display) |
| 10 / 11 / 12 / 13 | SPI SCK / MOSI / CS / DC (bez MISO) |
| 14 | AMP MUTE OC |
| 15 / 16 / 17 / 18 | BT I2S BCLK / WS / DATA IN / DATA OUT |
| 21 | DISPLAY BL |
| 39 / 40 / 41 | INPUT S1 / S2 / KEY, KEY również Recovery firmware |
| 42 | Reset BT przez Q401 |
| 47 | AMP EN OC |
| 0 | Pull-up R205 10 kΩ do 3V3_MAIN; strap/BOOT |

- Nie przydzielać nowych funkcji GPIO3/45/46 (strap), GPIO35–37 (Octal PSRAM), GPIO19/20 (USB), GPIO43/44 (UART diagnostyczny), GPIO38/48 (RGB) bez odrębnego sprawdzenia i decyzji.
- R201/R202/R203 = 33 Ω na I2S DAC. Zasilanie 5V_SYS do wejścia 5V DevKita; 3V3_MAIN pochodzi z regulatora na module i jest **oddzielone od 3V3_AUX**.

### 3.2 VoxOneBT — Wemos D1 mini ESP32

- Osobny, wymienny moduł klasyczny ESP32, **płasko równolegle do PCB**, tylko dwa *wewnętrzne* rzędy żeńskich gniazd 1×10. Zorientowany anteną do górnej krawędzi, USB w dół — z zachowaniem dostępu.
- J401/J402 po 10 pinów: numeracja od strony anteny do strony USB, **widok od góry M1**, konieczna jawna zgodność z nadrukiem modułu.
- J402.8 = **5V_SYS** (wejście VCC 5 V zatwierdzone). J402.7 = GND. J401.8 = 3.3V modułu **NC na M1**.
- UART: BT GPIO17 TX → MAIN GPIO2 RX; MAIN GPIO1 TX → BT GPIO16 RX.
- I2S BT master: BT GPIO18 BCLK → MAIN15; BT GPIO19 WS → MAIN16; BT GPIO23 DATA → MAIN17. MAIN GPIO18 DATA → BT GPIO26 przygotowane na przyszłość. Nie zmieniać kierunków BCLK/WS bez nowej decyzji.
- Reset BT: MAIN42 → Q401 open collector → BT RST; należy sprawdzić rzeczywiste poziomy start/reset.

### 3.3 Audio PCM5102A

- Wymienny **gotowy fioletowy moduł GY-PCM5102A z własnym jackiem 3,5 mm**. Osobny goldpin L/GND/R umożliwia wyprowadzenie na zewnętrzne RCA/jack; to jedno analogowe wyjście stereo, nie dwa niezależne źródła.
- Piny A1=SCK→GND, A2=BCK, A3=DIN, A4=LCK, A5=GND, A6=VIN→5V_DAC za FB301.
- Piny B1=FLT NC na M1, B2=DEMP NC, B3=XSMT sterowany MAIN, B4=FMT NC, B5=A3V3 NC, B6=AGND, B7=ROUT, B8=AGND, B9=LROUT.
- Mostki użytkownika: H1 FLT=LOW; H2 DEMP=LOW; **H3 do HIGH i LOW rozwarte**; H4 FMT=LOW (I2S). Fizyczne ustawienie mostków wymaga późniejszej kontroli; nie podawać 5 V bez sprawdzenia wejścia modułu.
- Filtr zasilania FB301, kondensatory równolegle C301 100 nF / C302 10 nF / C303 **10 µF 16 V radial THT**.

### 3.4 RTC / wyświetlacze / input / AMP

- RTC DS3231 mini `U601`: 1=3V3_AUX, 2=SDA, 3=SCL, 4=NC, 5=GND; pionowy męski goldpin 1×5 / 2,54 mm; fabryczny moduł/bateria bez ingerencji.
- I2C `J501`: VCC, GND, SDA, SCL; `JP501` 1–2=3,3 V, 2–3=5 V; zawsze logika I2C 3,3 V. R604/R605 po 4,7 kΩ do 3V3_MAIN przez `JP602` 2×2: SDA 1–2, SCL 3–4, ON po założeniu mostka. Przy OFF mogą działać zewnętrzne pull-upy modułu.
- SPI `J502`: VCC, GND, SCK, MOSI, CS, DC, RST, BL; `JP502` analogicznie wybór VCC 3,3/5 V. Bez MISO. RESET to RC + SN74LVC1G17, nie restart programowy ESP. BL Q503/Q504 jako **zasilanie anody**, tylko dla zgodnych modułów, nie ogólnie jako wejście logiczne/kathoda.
- Kondensatory zasilania wyświetlaczy: dla I2C C501=100 nF/C502=10 nF/C503=10 µF radial; dla SPI C504=100 nF/C505=10 nF/C506=10 µF radial.
- INPUT: 1×4 S1/S2/KEY/GND, EC11 albo trzy przyciski do GND; R601/R602/R603 10 kΩ do 3V3_MAIN przez niezależne zworki `JP601` 2×3. Firmware `INPUT` bez wewnętrznych pull-up, sterowanie zunifikowane.
- AMP: `J603` EN_OC, MUTE_OC, GND; Q601/Q602 MMBT3904 open-collector, projektowo sink ≤2 mA / 0…24 V przy zgodnym zewnętrznym pull-up. R606/R608 6,8 kΩ, R607/R609 100 kΩ. Bez gwarancji właściwej polaryzacji dla nieznanego wzmacniacza.

### 3.5 Zasilanie

- Jeden ARK 2-pin `J101` = +5 V / GND, typowo zasilacz **5 V / 3 A**. **Brak osobnego wejścia USB-C na PCB M1**, brak dodatkowych zworek/diodek/muxów do przełączania zasilania na PCB bez zgody użytkownika.
- `J101 → F101 (T3,15 A) → Q101 (FDD6685 DPAK, G1/GND, D2/tab/5V_FUSED, S3/5V_SYS) → 5V_SYS`; D101 SMBJ5.0A TVS, C101 470 µF 16 V + C102 100 nF.
- `U101` AMS1117-3.3 SOT-223 dla 3V3_AUX, wyjściowy C105 **22 µF 16 V solid tantalum**, inne kondensatory wg schematu; R101 300 Ω. Planowany limit poboru AUX do 150 mA *łącznie* (do potwierdzenia).
- Na każdą aktywną grupę zasilania lokalnie 100 nF + 10 nF X7R/1206 i elektrolit THT według zatwierdzonego schematu. Nie dodawać arbitralnie kondensatorów ani nie zmieniać pojemności.
- MAIN oraz BT mają własne regulatory na gotowych modułach; nie łączyć 3V3_MAIN z 3V3_AUX ani wyjścia 3V3 Wemosa z 5V_SYS.

## 4. Aktualny stan projektu — wyniki potwierdzone przez raport Codexa, nie pomiary sprzętowe

| Etap | Rezultat |
|---|---|
| SCHEMATIC R0 | 26 błędów / 67 ostrzeżeń ERC; punkt startowy |
| R1A-2, R1B, R1C | dopracowanie symboli i topologii, jeden arkusz A2 od R1C |
| R1D | VCC BT J402.8 do 5V_SYS; C303/C503/C506 = 10 µF; ERC 10/21 |
| R1E | NC DAC B1/B2/B4 + poprawny model zasilania ERC (PWR_FLAG); ERC 1/21 |
| R1F | usunięte Q501/Q502 BSS138 i R501/R502; I2C bezpośrednie 3,3 V; ERC 1/21 |
| R1G | JP602 z niezależnymi pull-up SDA/SCL; ERC 1/21 |
| FOOTPRINT-1 | 73/77 elementów z footprintami; RTC pin4 NC; ERC 0 błędów, 2 ostrzeżenia |
| FOOTPRINT-2 + PCB-PREVIEW-1 | 77/77 footprintów; schemat 86 sieci i 258 pin–sieć; ERC **0/0**. Pierwsze PCB 100×100 mm, **0 ścieżek**, 4×M3, 173 niepołączenia i 84 ostrzeżenia silkscreen. **Rozmieszczenie odrzucone, nie wolno routować.** |

**Ścieżka dotychczasowego punktu odniesienia CAD (laptop):** `%USERPROFILE%\Documents\VoxOne_M1_FOOTPRINT-2`  
**Projekt KiCad:** `VoxOne_M1.kicad_pro`, `.kicad_sch`, `.kicad_pcb`  
**Kluczowe raporty:** `FOOTPRINT-2_ODPOWIEDZ_CODEX.md`, `PCB-PREVIEW-1_ROZMIESZCZENIE.md`, `PCB-PREVIEW-1_KOLIZJE_I_BLOKADY.md`, `PCB-PREVIEW-1_ERC_DRC.md`  
**Archiwum:** `checkpoints/FOOTPRINT-2_PCB-PREVIEW-1_FINAL.zip`  
**Błąd narzędzia:** KiCad Copilot MCP import PCB raz zwrócił sukces, ale wadliwy plik; poprawny PCB odbudowano natywnym `pcbnew`. Przy kolejnych etapach obowiązkowo `LoadBoard`/native CLI/netlist, bez ufa­nia samemu komunikatowi MCP.

### Dlaczego PCB-PREVIEW-1 odrzucono

- MAIN leży poziomo z anteną wystającą z lewej krawędzi, oba USB po prawej/w głąb; ma być estetycznie i mechanicznie przemyślany układ MAIN po lewej, najlepiej pionowo z USB dostępnymi przy krawędzi.
- BT leży w dolnej części zamiast odpowiadającej wizji części prawej.
- Środkowa lewa strefa jest słabo wykorzystana, prawa przepełniona złączami i drobnicą.
- **11 elementów SMD po stronie BOTTOM** — sprzeczne z nową ostateczną decyzją TOP ONLY.
- Elementy pod modułami przy niepotwierdzonym prześwicie; niedokładne/nieobecne modele 3D BT/RTC/DAC.
- Zbyt dużo kolizji / nieczytelnych opisów; estetyka słabsza niż zaakceptowana wizualizacja koncepcyjna.

## 5. Źródła zewnętrznych bibliotek i ograniczenia

- Referencja ESP32-S3 klon YD (2×22, 25,40 mm osiowo, obrys footprintu 28×57): https://github.com/shkuznetsov/YD-ESP32-S3 — **tylko wariant referencyjny**; inne DevKitC-1 mogą się różnić.
- Referencja Wemos: https://github.com/besi/kicad-esp32-wemos-d1-mini — wewnętrzne rzędy wg biblioteki 22,86 mm / 2,54 mm; nie zamieniać z zewnętrznymi. Zwracać uwagę na licencje modeli 3D.
- Referencja PCM5102A: https://github.com/sstojos/zynthian-miniature — `GY-PCM5102.kicad_mod` z modelem STEP, ale **model 3D wymaga dopasowania orientacji**. Zachować zgodność rzeczywistych 15 padów.
- Dla wszystkich trzech nie ma jeszcze potwierdzenia fizycznego egzemplarza. Footprinty prowizoryczne i oznaczenie `PROVISIONAL / NOT FOR MANUFACTURING` pozostają obowiązkowe.

## 6. Decyzje odrzucone / poza zakresem M1

- **ST7920 LCD** — odrzucony.
- **BSS138 na I2C i pull-up 5 V wyświetlacza** — usunięte w R1F, nie przywracać bez nowej decyzji.
- **DSPmini, wejście AUX PCM1808** — przeniesione do L1, nie M1.
- **SPDIF** — usunięte z projektu VoxOne; nie dodawać z powrotem.
- **Dodatkowe wejście USB-C zasilające PCB, przełączniki/jumpery zasilania MAIN/BT, niezatwierdzone power-path, ekspandery IO** — nie dodawać.
- **Trasowanie obecnego PCB-PREVIEW-1** — zabronione do momentu nowej akceptacji rozmieszczenia.
- **SMD po stronie BOTTOM** — niedopuszczalne.

## 7. GitHub — repozytorium źródłowe

- [x] **M1-GIT-01 [DONE]** — Użytkownik utworzył publiczne repozytorium `https://github.com/pimowo/VoxOnePCB` z gałęzią `main`.
- [x] **M1-GIT-02 [APPROVED]** — Przechowywać również edytowalne źródła KiCad (`.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, biblioteki symboli/footprintów, lokalne dozwolone modele 3D) w tym repozytorium.
- [x] **M1-GIT-03 [DONE]** — Po instalacji ChatGPT Codex Connector zapis do GitHub został potwierdzony. Opublikowano README, TODO, AGENTS i `.gitignore` na `main`; udokumentowanie pełnego importu CAD pozostaje osobnym zadaniem M1-GIT-04.
- [ ] **M1-GIT-04 [IN PROGRESS]** — Sklonowano repo na laptopie, skopiowano aktualne pliki KiCad i biblioteki, otwarto widok 3D, a następnie opublikowano commit `8d90e6d` na `main`. Pozostaje **niezależne ponowne sprawdzenie ERC/DRC/netlist i modeli z czystego klonu**; nie oznaczać kontroli jako wykonanych bez wyników.
- [ ] **M1-GIT-05 [IN PROGRESS]** — Wstępnie sprawdzono licencje i dodano teksty MIT, Apache-2.0, GPL-3.0, KiCad CC-BY-SA z wyjątkiem. Modele `YD-ESP32-S3.step` (autorstwo GrabCAD) oraz `PCM5102-I2S.step` (odłączony, GPL-3.0) wyłączono z publikacji. Przed wydaniem produkcyjnym sprawdzić warunki redystrybucji zmodyfikowanego footprintu DAC i wymagane informacje o autorstwie/zmianach.
- [x] **M1-GIT-06 [DONE]** — Użytkownik wykonał `git diff --cached --check` (brak błędów), commit/push 60 plików, commit `8d90e6d`, a następnie powtórny `git push` potwierdził `Everything up-to-date`. Nie opublikowano checkpointów ZIP ani dwóch wstrzymanych modeli STEP.
- [ ] **M1-GIT-07 [TODO]** — Po imporcie zweryfikować, że Codex startuje w katalogu sklonowanego repo i czyta root `AGENTS.md` oraz `TODO.md`; dalej prowadzić **jeden** kanoniczny rejestr decyzji.
- [ ] **M1-GIT-08 [TODO]** — Osobno ustalić licencję i zasady publikacji własnej dokumentacji/PCB; samo publiczne repozytorium nie przyznaje automatycznie licencji na wykorzystywanie projektu.

## 8. Historia i nowe notatki — dopisywać, nie kasować

| Data | Wpis | Autor / decyzja |
|---|---|---|
| 2026-10-17 | Zakończony schemat R1G, footprinty FP1/FP2, wstępny podgląd PCB. | Raporty Codexa przekazane przez użytkownika |
| 2026-10-17 | Odrzucono układ PCB-PREVIEW-1; docelowy wygląd bliższy wcześniejszej wizualizacji. | Użytkownik |
| 2026-10-17 | Potwierdzono wszystkie elementy **tylko TOP**, ścieżki na **2 warstwach miedzi**. | Użytkownik |
| 2026-10-17 | Założono kanoniczny notatnik `TODO.md` i plik wskazówek `AGENTS.md` dla Codexa; brak zgody na nowy prompt na tym etapie. | Użytkownik / przygotowanie notatnika |
| 2026-10-17 | Utworzono publiczne repozytorium `pimowo/VoxOnePCB`. Pierwszy zapis był blokowany HTTP 403; po instalacji ChatGPT Codex Connector zapis działa. Dokumenty TODO, AGENTS, README i `.gitignore` publikowane na `main`. Źródła KiCad pozostają na laptopie do osobnego importu. | Użytkownik / ChatGPT |
| 2026-10-17 | Użytkownik wykonał pierwszą publikację KiCad na GitHub: 60 plików, commit `8d90e6d`, push do `main`, lokalnie czyste drzewo. Model YD-ESP32-S3.step i PCM5102-I2S.step wyłączono. | Użytkownik / ChatGPT |
| 2026-10-18 | Zatwierdzono **prostokątną poziomą PCB** o wymiarach obu boków nie większych niż 100 mm. Dokładny rozmiar PENDING, wymagana analiza mechanicznej wykonalności wobec modułów, RF, USB/jack i 4×M3. Wizualizacja VoxOne_M1 pozostaje wzorcem kompozycji, a układy PCB-LAYOUT-2/3 nie mają akceptacji do trasowania. | Użytkownik |

### Miejsce na nowe pomysły

- [ ] **M1-IDEA-001:** _Nowy pomysł / decyzja — wpisz datę, szczegóły, status i kryterium zakończenia._

---

**Synchronizacja GitHub:** kanoniczną wersją TODO ma być `https://github.com/pimowo/VoxOnePCB/blob/main/TODO.md`. Repozytorium jest **publiczne**; nie dodawać haseł, tokenów, prywatnych danych i obcych modeli/bibliotek bez przeglądu licencji. Pliki CAD są już zapisane na GitHubie w commicie `8d90e6d`; lokalna kopia historycznej rewizji pozostaje na laptopie. Po zdalnych zmianach w TODO przed dalszą pracą lokalną wymagany jest `git pull --ff-only` na czystym drzewie. Lokalny Codex może pracować na TODO/AGENTS po sklonowaniu repo; aktualizacja GitHub wymaga `commit` oraz `push` i nie dzieje się automatycznie.