# PCB-LAYOUT-2 — wariant A do oceny

Nowe rozmieszczenie zapisano i opublikowano na [gałęzi pcb-layout-2](https://github.com/pimowo/VoxOnePCB/tree/pcb-layout-2).

- Źródło: `main`, commit `1ca3e40e3600f005977bc504b272e34483b30150`.
- Commit projektu CAD i kontroli: `1abc511767069ceb13c87a6e97710187d3907379`. Pełna odpowiedź końcowa jest dodana osobnym commitem tej samej gałęzi.
- **Push: zakończony pomyślnie.** `main` pozostał bez zmian; bez merge i force-push. Aktualny HEAD i potwierdzenie publikacji: [lokalny zapis kontroli](C:/Users/piotrek/.codex/attachments/PCB-LAYOUT-2_CHECKPOINT/PUBLICATION_RECEIPT.json).

## Wyniki kontroli

| Kontrola | Wynik |
|---|---|
| Montaż | **77 TOP / 0 BOTTOM** |
| Laminat | **100 × 100 mm**, F.Cu/B.Cu |
| Otwory | **4 × M3**, NPTH Ø3,2mm; rezerwa pod łby Ø7mm |
| Ścieżki / przelotki routingu / pola miedzi | **0 / 0 / 0** |
| ERC | **0 błędów / 0 ostrzeżeń** |
| DRC | **173 niepołączenia**, **0 pozostałych naruszeń**, **0 ostrzeżeń nadruku** |
| Zgodność elektryczna | **77 elementów, 86 sieci, wszystkie 258 przypisań pin–sieć zachowane** |
| Wykryte kolizje geometrii referencyjnej | **0**, bez drobnicy pod modułami |

Wszystkie kontrole są włączone. **Nie jest to DRC PASS**, ponieważ PCB pozostaje nietrasowane. Schemat A2, wartości, GPIO, UUID, lokalne biblioteki, modele i konfiguracja projektu pozostały niezmienione. Geometrię padów wszystkich77 footprintów porównano z bibliotekami; zapisany PCB otwarto ponownie natywnie.

MAIN jest pionowo po lewej, USB-C skierowane ku górze, antena w dół. DAC jest u góry po prawej, jack skierowany ku górnej krawędzi zgodnie z rysunkiem footprintu. BT leży płasko po prawej, anteną w górę i USB w dół. RTC zajmuje górną część strefy środkowej. Złącza użytkowe są uporządkowane przy dolnej krawędzi, ARK przy lewej. Nie tworzono wariantuB: wariantA przeszedł kontrole geometrii referencyjnej.

Pozostałe komponenty mają minimum **15,105mm** odstępu od referencyjnych obszarów anten. Przyjęto bufor opisany w [wytycznych Espressif](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32/pcb-layout-design.html?highlight=antenna). Nie oznacza to wykonania testówRF.

## Projekt i podglądy

Katalog projektu: `C:\Users\piotrek\Documents\VoxOnePCB`.

- [Edytowalny PCB](C:/Users/piotrek/Documents/VoxOnePCB/VoxOne_M1.kicad_pcb)
- [Widok 2D TOP](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-2/previews/PCB-LAYOUT-2_TOP.png)
- [3D TOP](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-2/previews/PCB-LAYOUT-2_3D_TOP.png), [3D pod kątem](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-2/previews/PCB-LAYOUT-2_3D_ANGLE.png), [3D BOTTOM](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-2/previews/PCB-LAYOUT-2_3D_BOTTOM.png)
- [Raport bazowy](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-2/BASELINE_ERC_DRC.md), [rozmieszczenie wszystkich elementów](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-2/ROZMIESZCZENIE.md), [porównanie netlist i79 padów modułów](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-2/NETLIST_COMPARISON.md)
- [Końcowe ERC/DRC](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-2/FINAL_ERC_DRC.md), [ograniczenia mechaniki](C:/Users/piotrek/Documents/VoxOnePCB/docs/PCB-LAYOUT-2/KOLIZJE_I_OGRANICZENIA.md). Surowe raporty JSON/RPT są w tym samym katalogu.
- [Pełna odpowiedź zapisana w repo](C:/Users/piotrek/Documents/VoxOnePCB/PCB-LAYOUT-2_ODPOWIEDZ_CODEX.md)
- Checkpointy poza Git: [przed zmianami](C:/Users/piotrek/.codex/attachments/PCB-LAYOUT-2_CHECKPOINT/PCB-LAYOUT-2_BEFORE.zip) oraz [końcowy](C:/Users/piotrek/.codex/attachments/PCB-LAYOUT-2_CHECKPOINT/PCB-LAYOUT-2_FINAL.zip). Integralność CRC/SHA-256 sprawdzona; bez zagnieżdżonych ZIP.

Natywny rysunek do przeglądania:

:codex-file-citation{path="C:\Users\piotrek\Documents\VoxOnePCB\docs\PCB-LAYOUT-2\previews\PCB-LAYOUT-2_2D.pdf" purpose="output"}

## Pozostające ograniczenia

- **Geometria MAIN, BT, DAC i RTC nadal PROVISIONAL.** Potrzebne pomiary konkretnych egzemplarzy: rozstawy, pin1, obrysy, anteny, USB/jack, elementy spodnie, bateria RTC oraz zdjęcia góra/dół/bok z suwmiarką.
- Nie potwierdzono wysokości podstawek, wcześniejszego założenia8,5mm, tolerancji i wygody wyjmowania modułów. Przy RTC pozostaje około0,405mm rezerwy do C203 i0,625mm do kolumnySMD; wymagają sprawdzenia. Łby/podkładki większe niż7mm trzeba ocenić ponownie.
- Brakuje pełnych modeliBT, RTC, DAC i F101. Pokazano rzeczywiste podstawki/obrysy; nie tworzono fikcyjnych brył. DAC STEP pozostał odłączony. ModelMAIN działa lokalnie, lecz nie jest publikowany; czysty klon pokaże jego podstawki. ModelC101 maH16 zamiast docelowegoH12,5. Ograniczenia licencji modeli pozostają otwarte.
- Referencyjne moduły mieszczą się w laminacie; rezerwy zewnętrznych wtyków jack/BT wychodzą poza niego odpowiednio górą i dołem. Gabaryty kabli i obudowa wymagają akceptacji po pomiarach. Nie zatwierdzono odstępstwa dla wystającego rzeczywistego modułu.
- BuforyRF wymusiły odsunięcie części drobnicy. Przed trasowaniem trzeba osobno ocenić odległości I2S/rezystorów33Ω, ciągłość przyszłej masy i obszaryRF. Analiza2D i courtyard nie zastępuje kontroli rzeczywistych brył, serwisu ani testówRF.

TODO zostało zaktualizowane; **M1-P0-14 nadal oczekuje na Twoją wyraźną akceptację**. BlokadyP1 pozostały otwarte. Dawnego katalogu FOOTPRINT-2 i firmware nie zmieniano.

**PROTOTYPE / PROVISIONAL — NOT FOR MANUFACTURING. Zakończono na PCB-LAYOUT-2, bez trasowania i Gerberów.**
