# PCB-LAYOUT-2: niezależny punkt odniesienia

Data: 2026-10-18. Lokalny Windows 10, natywny KiCad CLI/pcbnew 10.0.4, repozytorium pimowo/VoxOnePCB. Przeczytano w całości AGENTS.md i TODO.md. Drzewo main było czyste; git pull --ff-only: Already up to date. Źródłowy HEAD main/origin/main: `1ca3e40e3600f005977bc504b272e34483b30150`. Utworzono nową gałąź pcb-layout-2. Dawna informacja AGENTS/TODO o oczekiwaniu na polecenie została zastąpiona wyraźną autoryzacją tego etapu przez użytkownika; zakaz trasowania pozostaje.

77 elementów elektrycznych, 81 footprintów wraz z 4 board-only M3, 86 sieci, 258 przypisań pin–sieć. TOP66 / BOTTOM11. Obrys100×100, dwie warstwy F.Cu/B.Cu, zero ścieżek, przelotek i pól miedzi. Dwie istniejące strefy to zakazy miedzi przy antenach.

ERC: 0 błędów / 0 ostrzeżeń. DRC: 173 niepołączenia error, 84 ostrzeżenia nadruku, 0 rozbieżności schemat–PCB. Ignorowanych kontroli: 0. Nie jest to gotowość produkcyjna ani DRC PASS.

Wszystkie77 lokalnych footprintów otwarto natywnie, sprawdzono pełne zbiory numerów padów i wartości. Porównanie XML schematu z odczytem PCB: pełna zgodność258 par. Stan źródłowy, manifest SHA-256 i kopia wszystkich plików projektu/bibliotek/dokumentów znajdują się poza Git: `C:\Users\piotrek\.codex\attachments\PCB-LAYOUT-2_CHECKPOINT\PCB-LAYOUT-2_BEFORE.zip`. Archiwum68 plików, CRC i indywidualne SHA-256 sprawdzone; bez .git/.history/cache. HEAD i hash ZIP: BASELINE_MANIFEST.json.

Oryginalny katalog VoxOne_M1_FOOTPRINT-2 nie był modyfikowany ani ponownie importowany. Nie znaleziono obrazu wcześniejszej koncepcji w repo; wykorzystano opis TODO, nie deklarowano obejrzenia nieistniejącego pliku.

## Modele i przenośność

| Model aktywny | Dostępny lokalnie | Śledzony przez Git |
|---|---|---|
| ${KIPRJMOD}/models3d/Capacitor_THT__CP_Radial_D10.0mm_P5.00mm.step | True | True |
| ${KIPRJMOD}/models3d/Capacitor_SMD__C_1206_3216Metric.step | True | True |
| ${KIPRJMOD}/models3d/Capacitor_THT__CP_Radial_D5.0mm_P2.00mm.step | True | True |
| ${KIPRJMOD}/models3d/Capacitor_Tantalum_SMD__CP_EIA-7343-31_Kemet-D.step | True | True |
| ${KIPRJMOD}/models3d/Diode_SMD__D_SMB.step | True | True |
| ${KIPRJMOD}/models3d/Diode_SMD__D_SOD-123.step | True | True |
| ${KIPRJMOD}/models3d/Inductor_SMD__L_1206_3216Metric.step | True | True |
| ${KIPRJMOD}/models3d/TerminalBlock_Phoenix__TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal.step | True | True |
| ${KIPRJMOD}/models3d/Connector_PinHeader_2.54mm__PinHeader_1x03_P2.54mm_Vertical.step | True | True |
| ${KIPRJMOD}/models3d/Connector_PinSocket_2.54mm__PinSocket_1x10_P2.54mm_Vertical.step | True | True |
| ${KIPRJMOD}/models3d/Connector_PinHeader_2.54mm__PinHeader_1x04_P2.54mm_Vertical.step | True | True |
| ${KIPRJMOD}/models3d/Connector_PinHeader_2.54mm__PinHeader_1x08_P2.54mm_Vertical.step | True | True |
| ${KIPRJMOD}/models3d/Connector_PinHeader_2.54mm__PinHeader_2x03_P2.54mm_Vertical.step | True | True |
| ${KIPRJMOD}/models3d/Connector_PinHeader_2.54mm__PinHeader_2x02_P2.54mm_Vertical.step | True | True |
| ${KIPRJMOD}/models3d/Package_TO_SOT_SMD__TO-252-2.step | True | True |
| ${KIPRJMOD}/models3d/Package_TO_SOT_SMD__SOT-23.step | True | True |
| ${KIPRJMOD}/models3d/Resistor_SMD__R_1206_3216Metric.step | True | True |
| ${KIPRJMOD}/models3d/Package_TO_SOT_SMD__SOT-223.step | True | True |
| ${KIPRJMOD}/models3d/YD-ESP32-S3.step | True | False |
| ${KIPRJMOD}/models3d/Connector_PinSocket_2.54mm__PinSocket_1x22_P2.54mm_Vertical.step | True | True |
| ${KIPRJMOD}/models3d/Connector_PinSocket_2.54mm__PinSocket_1x06_P2.54mm_Vertical.step | True | True |
| ${KIPRJMOD}/models3d/Connector_PinSocket_2.54mm__PinSocket_1x09_P2.54mm_Vertical.step | True | True |
| ${KIPRJMOD}/models3d/Package_TO_SOT_SMD__SOT-23-5.step | True | True |
| ${KIPRJMOD}/models3d/Connector_PinHeader_2.54mm__PinHeader_1x05_P2.54mm_Vertical.step | True | True |

MAIN STEP jest dostępny lokalnie, lecz wyłączony z publikacji; czysty klon ma brak tej bryły. DAC STEP jest lokalnie zachowany, nieaktywny i również niepublikowany. Wemos/RTC/F101 bez pełnych brył; widoczne standardowe modele złączy. Nie dodawano obcych modeli ani nie zmieniano licencji.
