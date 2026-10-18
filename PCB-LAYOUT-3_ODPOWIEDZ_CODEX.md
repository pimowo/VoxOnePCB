# PCB-LAYOUT-3 — propozycja do oceny

Zapisano rzeczywisty, edytowalny layout i opublikowano [gałąź pcb-layout-3](https://github.com/pimowo/VoxOnePCB/tree/pcb-layout-3). Referencję PNG otwarto przed projektowaniem. MAIN ma teraz antenę u góry i oba USB-C na dole; DAC ma jack na prawej krawędzi. Przełożono pozostałe grupy i dolne złącza.

**To propozycja na danych referencyjnych. Nie uznaję wszystkich preferencji bliskości ani mechaniki rzeczywistych klonów za domknięte. Akceptacja wyglądu i kompromisów pozostaje PENDING.**

## Git i zabezpieczenie

- Źródło: `origin/pcb-layout-2`, commit `1d2da877b73ca1ea3dc309bd2993f96a8883545e`.
- Wynik CAD i raportów: `pcb-layout-3`, commit `baa8feee4b8d983e1eefc482abe113b7bbd6a955`.
- **Push propozycji: wykonany.** Pełna odpowiedź jest dodana osobnym commitem tej samej gałęzi; końcowy HEAD i zgodność z GitHubem zapisano w [potwierdzeniu publikacji](C:/Users/piotrek/.codex/attachments/PCB-LAYOUT-3_CHECKPOINT/PUBLICATION_RECEIPT.json).
- `main` i `pcb-layout-2` pozostały bez zmian. Nie wykonano merge ani force-push. Historycznych projektów i firmware nie zmieniano.

## Wyniki kontroli

| Kontrola | Wynik |
|---|---|
| Elementy elektryczne / footprinty z otworami | **77 / 81** |
| Montaż TOP / BOTTOM | **77 / 0** |
| PCB / warstwy | **100 × 100 mm / F.Cu + B.Cu** |
| Otwory | **4 × M3, NPTH Ø3,2 mm** |
| Ścieżki / przelotki / wypełnienia miedzi | **0 / 0 / 0** |
| ERC przed → po | **0/0 → 0/0** błędów/ostrzeżeń |
| DRC przed → po | **173 → 173 niepołączenia; 0 pozostałych naruszeń i 0 ostrzeżeń** |
| Netlista | **86 sieci; 258/258 przypisań pin–sieć identycznych** |
| Geometria referencyjna | **0 wykrytych kolizji części, pełnych obrysów modułów, rezerw śrub i kabli** |

**Nie jest to DRC PASS** — niepołączenia pozostają, ponieważ PCB nie jest trasowane. Wykonano rzeczywisty KiCad CLI 10.0.4 i niezależny odczyt przez pcbnew po zapisie. Sprawdzono wszystkie 77 bibliotek, geometrię padów, ich UUID i 79 wyprowadzeń MAIN/BT/DAC. Schemat A2, wartości, GPIO, biblioteki, modele oraz ustawienia projektu zachowano; pliki schematu i konfiguracji są bajtowo identyczne ze źródłem. Nie dodano wykluczeń ani nie osłabiono reguł.

## Najważniejsze zmiany względem layoutu 2

Odległości poniżej dotyczą geometrii bibliotecznej, nie pomiaru fizycznych modułów.

| Parametr | PCB-LAYOUT-2 | PCB-LAYOUT-3 |
|---|---|---|
| MAIN | Antena w dół, USB w górę | **Antena w górę, USB w dół**, obrót całego footprintu o 180° |
| Antena MAIN do górnej krawędzi | 60 mm | **0,5 mm** |
| USB MAIN | Około 3 mm od górnej krawędzi | **36,1 mm do dolnej krawędzi**, dwa osobne wolne korytarze |
| Jack DAC | W górę, 4 mm od krawędzi | **W prawo, czoło na krawędzi: 0 mm** |
| Minimalny odstęp RTC | Około 0,405 mm | **2,095 mm**, do R205 |

BT pozostaje płasko po prawej, anteną w górę. RTC jest między MAIN a BT, poniżej sekcji audio. Dolna kolejność to **I2C → SPI → INPUT → AMP**. JP602 zachowuje poziome pary **1–2 SDA / 3–4 SCL**; nadruk pokazuje SDA, SCL i ON/OFF. POWER jest pogrupowany przy lewej krawędzi. Nie ma drobnicy pod modułami.

Inne części i moduły mają minimum **15,000 mm** od referencyjnych obszarów anten; łby M3 Ø7 mm minimum **15,078 mm**. Oba keepouty przeniesiono razem z modułami i zachowano na obu warstwach. Nie jest to pomiar skuteczności RF ani potwierdzenie pełnej zgodności montażu anten z [wytycznymi Espressif](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/pcb-layout-design.html#general-principles-of-pcb-layout-for-modules-positioning-a-module-on-a-base-board).

Pozycje M3: H901 **(53,5; 61,5)**, H902 **(145; 55)**, H903 **(55; 145)**, H904 **(146,5; 141,5)** mm. H901 i H904 przesunięto dla RF oraz dolnych złączy; ten wzór otworów wymaga oceny z docelową obudową.

## Pozostające kompromisy i blokady

- **Bliskość elementów nie jest w pełni domknięta:** JP601–J601 ma **31,754 mm** między środkami. Proste odległości padów zasilania do VIN DAC: C301 **3,918 mm**, C302 **20,660 mm**, C303 **20,449 mm**. Nie są to długości ścieżek. Raport opisuje alternatywy wymagające innej organizacji dolnych złączy lub ponownego przesunięcia BT; nie przedstawiono niezweryfikowanego wariantu B jako poprawnego PCB.
- USB MAIN wymaga sprawdzenia rzeczywistych wtyków w rezerwach **9 × 18 mm** i kabli **Ø4 mm**. USB Wemosa referencyjnie wystaje **1,68 mm** poza laminat; zewnętrzne wtyki także wystają. Nominalny odstęp INPUT od pełnego obrysu BT to **0,400 mm**. Dostęp i tolerancje wymagają fizycznej próby.
- **MAIN, BT, DAC i RTC nadal PROVISIONAL.** Potrzebne pomiary rozstawów rzędów, pin1, obrysów, położenia anten/USB/jacka/H1–H4, baterii RTC, elementów spodnich i wysokości podstawek. Zdjęcia góra/dół/bok z suwmiarką pozwolą zamknąć te sprawy. Nie potwierdzono wcześniejszego prześwitu 8,5 mm.
- Anteny nadal znajdują się nad laminatem M1; nie wykonano wycięć FR4, testów RF ani projektu docelowej masy. Obudowa, podkładki większe niż Ø7 mm i rzeczywiste kable wymagają ponownej kontroli.
- Brakuje pełnych brył **BT, DAC, RTC i F101**. Pokazano rzeczywiste podstawki i obrysy. MAIN STEP działa lokalnie, lecz nie jest publikowany; czysty klon nie pokaże tej bryły. DAC STEP pozostał odłączony. C101 nadal ma model H16 zamiast docelowego H12,5. Nie publikowano wstrzymanych modeli STEP.
- Referencje **D101, R101, C105, U101, C401, C402, R602** są zachowane na **F.Fab**, a nie na nadruku TOP. To jawne ograniczenie tej propozycji. Wszystkie części są w tabeli montażowej.
- Wcześniejsze blokady P1, w tym zgodność USB z zasilaniem zewnętrznym, rzeczywiste mostki DAC, termika i dobór konkretnych części, pozostają otwarte.

Układ jest bliższy referencji w kierunkach MAIN/DAC, podziale funkcji i dolnych złączach. Nie skopiowano z obrazu JST, proporcji modułów ani dodatkowych pinów. Rzeczywisty footprint wymusza pionowy DAC przy jacku skierowanym w prawo. Brakujące modele nie zostały zastąpione fikcyjnymi bryłami.

## Projekt, widoki i raporty

Katalog: `C:\Users\piotrek\Documents\VoxOnePCB`.

- [Edytowalny PCB](C:/Users/piotrek/Documents/VoxOnePCB/VoxOne_M1.kicad_pcb), [projekt KiCad](C:/Users/piotrek/Documents/VoxOnePCB/VoxOne_M1.kicad_pro), [schemat A2](C:/Users/piotrek/Documents/VoxOnePCB/VoxOne_M1.kicad_sch).
- [2D TOP](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/previews/PCB-LAYOUT-3_TOP.png), [3D TOP](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/previews/PCB-LAYOUT-3_3D_TOP.png), [3D pod kątem](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/previews/PCB-LAYOUT-3_3D_ANGLE.png), [3D BOTTOM](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/previews/PCB-LAYOUT-3_3D_BOTTOM.png).
- Zbliżenia: [MAIN/antena](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/previews/PCB-LAYOUT-3_MAIN_ANTENNA.png), [DAC](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/previews/PCB-LAYOUT-3_DAC.png), [dolne złącza](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/previews/PCB-LAYOUT-3_DOLNE_ZLACZA.png), [RTC](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/previews/PCB-LAYOUT-3_RTC_ODSTEPY.png).
- [Rysunek mechaniczny z rezerwami kabli](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/previews/PCB-LAYOUT-3_MECHANICAL.svg).
- [Porównanie layoutów](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/PCB-LAYOUT-2_vs_3.md), [pełna tabela rozmieszczenia](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/ROZMIESZCZENIE.md), [mechanika i odstępy](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/MECHANIKA_I_ODSTEPY.md), [kolizje i blokady](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/KOLIZJE_I_BLOKADY.md).
- [Netlista i mapa pin–pad](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/NETLIST_COMPARISON.md), [wyniki ERC/DRC](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/FINAL_ERC_DRC.md), [pełny wykaz plików](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-3/WYKAZ_PLIKOW.md). Surowe JSON/RPT, netlisty i polecenia CLI są w tym samym katalogu.
- [Pełna odpowiedź zapisana w repo](C:/Users/piotrek/Documents/VoxOnePCB/PCB-LAYOUT-3_ODPOWIEDZ_CODEX.md).

Natywny rysunek do przeglądania:

:codex-file-citation{path="C:\Users\piotrek\Documents\VoxOnePCB\docs\PCB-LAYOUT-3\previews\PCB-LAYOUT-3_2D.pdf" purpose="output"}

Zmieniono PCB i kanoniczny TODO; dodano raporty, podglądy oraz dostarczoną referencję. Poprzednich raportów nie nadpisano. `git diff --check`, kontrola zakresu zmian, bibliotek, licencji i wzorców sekretów zakończyły się poprawnie. Zadania z fizycznymi blokadami nie zostały oznaczone DONE; M1-P0-14 pozostaje PENDING.

Checkpointy poza Git: [pełne wejście](C:/Users/piotrek/.codex/attachments/PCB-LAYOUT-3_CHECKPOINT/PCB-LAYOUT-2_BEFORE.zip) i [końcowy projekt](C:/Users/piotrek/.codex/attachments/PCB-LAYOUT-3_CHECKPOINT/PCB-LAYOUT-3_FINAL.zip). Integralność CRC i SHA-256 sprawdzona, bez zagnieżdżonych ZIP. Dokładne hashe, końcowy HEAD i status publikacji są w wskazanym wyżej potwierdzeniu. Checkpoint MCP pliku PCB: `mvdn4pe8-6557bbb1`.

**Zakończono na PCB-LAYOUT-3. Bez trasowania, przelotek routingu, Gerberów i zamawiania PCB. Czekam na ocenę wyglądu oraz decyzję o opisanych kompromisach.**
