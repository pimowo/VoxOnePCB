# PCB-LAYOUT-3 — końcowe kontrole KiCad10.0.4

| Kontrola | Baseline layout2 | Final layout3 |
|---|---:|---:|
| ERC errors/warnings | 0/0 | 0/0 |
| DRC niepołączenia | 173 | 173 |
| Inne błędy DRC | 0 | 0 |
| Silkscreen warnings | 0 | 0 |
| Inne warnings, w tym library mismatch | 0 | 0 |
| Schematic parity | 0 | 0 |
| Ignorowane kontrole / exclusions | 0/0 | 0/0 |
| Elementy elektryczne / footprinty wrazM3 | 77/81 | 77/81 |
| Sieci / ref-pin-net | 86/258 | 86/258 |
| TOP/BOTTOM | 77/0 | 77/0 |
| Ścieżki / przelotki / pola miedzi | 0/0/0 | 0/0/0 |
| OtworyNPTH3,2/M3 | 4 | 4 |
| Warstwy / nominalny laminat | 2/100×100mm | 2/100×100mm |

**DRC nie jest PASS:173 błędy niepołączeń pozostają, zgodnie z zakazem trasowania.** Zostały osobno oddzielone od fizycznych naruszeń; pozostałychDRC i ostrzeżeń0. Rzeczywisty exit codeDRC5, ERC0. --severity-all z kontrolą schematic-parity; żadnych ignorowanych kontroli. Wszystkie raportyJSON/RPT oraz dokładne polecenia i kody zakończenia zapisano obok tego dokumentu.

Po zapisie niezależny natywnyLoadBoard otworzył PCB, sprawdził81 footprintów, czteryM3, wszystkie258 przypisań i geometrię/UUID każdego pada. Biblioteki77 footprintów dostępne i zgodne. Źródła schematu i ustawień projektu zachowane bajtowo; użytoSaveBoard z aSkipSettings=True. Dwiezone są wyłącznie prawdziwymi rule-area anten naF.Cu iB.Cu, bez wypełnień. Nie dodano ścieżek ani przelotek. NOMINALNY obrys100×100; bbox API uwzględniający grubość liniiEdge.Cuts może wskazać100,05mm — nie jest to powiększenie laminatu.

MECHANICAL_CHECK.json:0 kolizji referencyjnych obrysów,RTCminimum2,095mm,inne elementy/moduły≥15,000mm od anten,łbyØ7≥15,078mm. To niezależna kontrola2D, nie pełna kontrola3D rzeczywistych części. Braki modeli i fizycznych wymiarów pozostająBLOCKEDP1.

Wszystkie trzy renderingi1800×1800 pochodzą z natywnego pcb render. PDF iSVG pochodzą z natywnego pcb export. PNG2D i zbliżenia to rasteryzacja/crop tegoPDF przez Windows.Data.Pdf/Pillow, bez generowania elektroniki. Sprawdzono wizualnieTOP/ANGLE/BOTTOM i rysunek2D; brak pełnychBT/DAC/RTC/F101 ujawniony. DodatkowyMECHANICAL.svg zawiera prawdziwe rezerwy wtyków/kabli i śrub naCmts.User.

Raporty ITERATION2_* i MECHANICAL_ITERATION.json są historyczną diagnostyką wcześniejszych iteracji, zawierają już poprawione problemy. Aktualne wyniki to FINAL_* i MECHANICAL_CHECK.json. Dokładne proste odległości padów zasilania DAC i środków zworek: SUPPLY_AND_CONTROL_DISTANCES.json; nie są długościami nieistniejących ścieżek.
