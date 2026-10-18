# MECHANIKA-1 — wynik analizy

**Najbardziej obiecujący jest 100 × 95 mm. Nie wybrałem go jako wymiaru docelowego.** Pełny kandydat mieści wszystkie elementy według referencyjnej geometrii XY, lecz wygoda serwisu, tolerancje i wysokości pozostają **BLOCKED** do pomiarów. Główny PCB, schemat, konfiguracja i biblioteki pozostały bajtowo niezmienione.

## Porównanie wariantów

| Wymiar | Wynik |
|---|---|
| 100 × 75 mm | **BLOCKED** — badane układy mają konflikty prawych M3 z RF/obrysem DAC. |
| 100 × 80 mm | **BLOCKED** — nie zamknięto równocześnie czterech narożnych M3, RF i kompozycji modułów. |
| 100 × 85 mm | **BLOCKED** — przykładowy stos modułów mieści się, ale koliduje z prawym górnym M3. |
| 100 × 90 mm | **BLOCKED** — podobny konflikt M3; opisano alternatywę wymagającą jego znacznego odsunięcia od naroża. |
| 100 × 95 mm | **PROVISIONAL FEASIBLE dla pakowania XY** — sprawdzono pełny kandydat 77 elementów. Brama serwisu/Z nadal **BLOCKED**. |

Sprawdzono nowe układy stosowe i boczne, nie samo przycięcie layoutu 3. Przeszukiwanie było dyskretne, dlatego dla 75–90 mm **nie ogłaszam globalnego INFEASIBLE**. Jedynie 95 mm przeszło badaną bramę obrysów; pozostałe nie otrzymały pozornych kompletnych PCB.

## Kontrole pełnego kandydata 100 × 95 mm

- **77 TOP / 0 BOTTOM**, 81 footprintów razem z **4 × M3 Ø3,2 mm**, rezerwy łbów Ø7 mm; dwie warstwy Cu.
- **86 sieci, 258/258 identycznych przypisań pin–sieć**. Zachowano wartości, oznaczenia, UUID oraz geometrie padów wszystkich bibliotek, w tym 79 wyprowadzeń MAIN/BT/DAC.
- Rzeczywisty KiCad CLI 10.0.4: **ERC przed i po 0 błędów / 0 ostrzeżeń**.
- **DRC przed i po: 173 niepołączenia, 0 innych naruszeń, 0 ostrzeżeń, 0 wykluczeń.** To nie jest DRC PASS — płytka nie jest trasowana.
- **0 ścieżek, 0 przelotek, 0 wypełnień miedzi**; dwa przeniesione z modułami antenowe keepouty na obu warstwach. Po zapisie wykonano natywny odczyt przez pcbnew i niezależne porównanie eksportów netlist.
- Pierwsza iteracja wykazała nakładanie courtyard JP601/J603. Poprawiono pozycje i ponowiono kontrolę, zachowując pierwotny raport. Reguł nie zmieniano.

## Odległości i ograniczenia

- **MAIN:** antena 0,5 mm od górnej krawędzi, USB w dół; referencyjne czoła USB 31,1 mm od dolnej krawędzi. Uwzględniono dwa wtyki 9 × 18 mm i oddzielne kable Ø4 mm.
- **DAC:** jack na prawej krawędzi — odległość czoła **0 mm**; rezerwa wtyku 18 mm poza PCB. Pełna otoczka z jackiem wynika z footprintu jako **18,5 × 31,9 mm**, zamiast wcześniejszego przybliżenia 17,45 mm. Nie pomniejszano obrysu. Do prawego górnego łba M3 pozostaje **0,5 mm**.
- **BT:** płasko po prawej, antena w górę, USB w dół. Referencyjna obudowa USB wystaje **2,58 mm**, a rezerwa końca wtyku **20,58 mm** poza laminat.
- **RTC:** minimum **2,175 mm do C602**, **2,5 mm do MAIN**. Inne części mają minimum **15 mm od anten**, metalowe łby M3 minimum **15,078 mm**.
- M3 lokalnie względem lewego górnego naroża: **(3,5;11,5), (96,5;3,5), (3,5;91,5), (96,5;91,5) mm**. Wzór wymaga sprawdzenia z obudową.
- Ciasne miejsca: **0,325 mm** między rezerwami USB a sąsiednimi obrysami, **0,9 mm INPUT–BT**, **0,65 mm AMP–BT**, **0,11 mm między courtyard JP601 i AMP**. To nominalne odstępy, nie potwierdzona wygoda palców ani tolerancje produkcyjne.
- Kondensatory DAC są **20,694–26,193 mm od VIN**; bulk MAIN również wymaga lepszego docelowego położenia. Upakowanie nie dowodzi dobrego odsprzęgania ani możliwości poprowadzenia wszystkich ścieżek.

Kompozycja zachowuje MAIN lewa, DAC górna prawa, BT prawa, RTC między modułami i POWER lewa. Proporcja 100:95 odbiega od szerokiej referencji; AMP jest na dolnym prawym boku, a nie we wspólnym szeregu dolnych złączy. Referencje kandydata są na F.Fab — nie opracowano produkcyjnego nadruku.

Pozostają potrzebne pomiary rzeczywistych klonów MAIN/BT/DAC/RTC, rozstawów rzędów, anten, USB/jacka, H1–H4, baterii, elementów spodnich i wysokości podstawek. Należy też zmierzyć konkretne wtyki, odgiętki, wiązki goldpinowe, shunty oraz obudowę. Nie potwierdzono wcześniejszego założenia 8,5 mm prześwitu. Pełnych modeli BT/DAC/RTC/F101 brak; MAIN jest dostępny lokalnie, bez publikacji STEP. Natywny render nie zastępuje pełnej kontroli 3D ani pomiarów RF.

## Pliki

Repozytorium: `C:\Users\piotrek\Documents\VoxOnePCB`.

- [Pełna odpowiedź](C:/Users/piotrek/Documents/VoxOnePCB/MECHANIKA-1_ODPOWIEDZ_CODEX.md) i [wykaz wszystkich plików](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/WYKAZ_PLIKOW.md).
- [Porównanie wymiarów](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/POROWNANIE_WYMIAROW.md), [metoda i granice analizy](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/ANALIZA_GEOMETRII.md), [rekomendacja i wymagane pomiary](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/REKOMENDACJA_WARIANTU.md).
- [Moduły i RF](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/MODULY_I_STREFY_RF.md), [USB, jack i złącza](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/USB_JACK_ZLACZA.md), [odstępy i kolizje](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/ODSTEPY_I_KOLIZJE.md).
- [Wymiarowy diagram 100×95](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/previews/100x95_GEOMETRIA_PROVISIONAL.png), [SVG z buforami RF](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/previews/100x95_GEOMETRIA_PROVISIONAL.svg), [natywny KiCad 2D](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/previews/100x95_KICAD_TOP.svg), [natywny KiCad 3D](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/previews/100x95_KICAD_3D_TOP.png). Diagramy 75/80/85/90 mm są w tym samym folderze i wyraźnie oznaczone jako niepełna diagnostyka.
- [Edytowalny kandydat PCB](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/candidates/100x95_PROVISIONAL/VoxOne_M1.kicad_pcb) i [jego projekt KiCad](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/candidates/100x95_PROVISIONAL/VoxOne_M1.kicad_pro).
- [Kontrole ERC/DRC](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/KONTROLE_KICAD.md), [porównanie netlist](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/NETLIST_COMPARISON.md), [ERC RPT](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/candidates/100x95_PROVISIONAL/ERC.rpt), [DRC RPT](C:/Users/piotrek/Documents/VoxOnePCB/docs/MECHANIKA-1/candidates/100x95_PROVISIONAL/DRC.rpt). JSON, polecenia CLI, tabela 77 części i potwierdzenie SHA-256 znajdują się obok.
- Checkpointy poza Git: [pełne wejście](C:/Users/piotrek/.codex/attachments/MECHANIKA-1_CHECKPOINT/LAYOUT-3_BEFORE.zip) i [pełny wynik](C:/Users/piotrek/.codex/attachments/MECHANIKA-1_CHECKPOINT/MECHANIKA-1_FINAL.zip). Integralność CRC i SHA-256 sprawdzona; bez zagnieżdżonych ZIP. [Potwierdzenie publikacji, końcowy HEAD i hashe](C:/Users/piotrek/.codex/attachments/MECHANIKA-1_CHECKPOINT/PUBLICATION_RECEIPT.json).

## Git i dalsza decyzja

- Źródło CAD: `origin/pcb-layout-3`, **8ed4cac3a92b1daa9433e69b296bed1a4cbf3cc8**.
- Nowsze decyzje odczytano z `origin/main`, **fb697a86297372d1b7ff51638d4cad441b283bcf**; zachowano historię layoutów 2/3 w jednym TODO.
- Wynik analizy: [pcb-feasibility-1](https://github.com/pimowo/VoxOnePCB/tree/pcb-feasibility-1), commit **0a079279ae359042c0c0c011b534def3775b7b89**. **Push wykonany.** Pełna odpowiedź i wykaz plików są dodane osobnym commitem tej samej gałęzi; końcowy lokalny/zdalny HEAD zapisano w potwierdzeniu publikacji powyżej.
- `main` i `pcb-layout-3` pozostały bez zmian. Bez merge i force-push; bez publikacji ZIP, nowych STEP i sekretów. `git diff --check` oraz kontrola zakresu zmian zakończyły się poprawnie.
- **M1-P0-15:** analiza referencyjna wykonana, brama serwisu/pomiarów BLOCKED. **M1-P0-16: PENDING** — wymiar wymaga Twojej decyzji.

Do rozważenia: 100×95 mm wraz z opisanymi ograniczeniami albo osobne dalsze badanie 90 mm z innym wzorem M3. W raporcie pokazano przykład przesunięcia prawego górnego M3 do (77,5;3,5) mm; nie jest to zweryfikowane rozmieszczenie 77 części.

**Kończę na MECHANIKA-1. Nie zmieniono głównego PCB, nie rozpoczęto produkcyjnego layoutu, trasowania ani Gerberów. Czekam na decyzję użytkownika.**
