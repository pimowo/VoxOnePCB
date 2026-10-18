# PCB-LAYOUT-2: końcowe ERC/DRC

KiCad10.0.4 CLI, raporty Errors/Warnings/Exclusions, bez wykluczania kontroli. Schemat A2 zachowany bajtowo.

| Kontrola | Baseline | WariantA |
|---|---:|---:|
| ERC błędy / ostrzeżenia | 0/0 | 0/0 |
| DRC niepołączenia error | 173 | 173 |
| Ostrzeżenia silkscreen | 84 | 0 |
| Inne błędy DRC | 0 | 0 |
| Schematic-parity | 0 | 0 |
| Ignorowane kontrole | 0 | 0 |
| TOP / BOTTOM elektryczne | 66/11 | 77/0 |
| M3 / ścieżki / przelotki / pola miedzi | 4/0/0/0 | 4/0/0/0 |

DRC exit5 z powodu173 niepołączeń, które pozostają błędami; nie deklaruje się DRC PASS. Liczba173 oznacza wskazania łączności DRC, nie liczbę sieci.86 sieci i258 przypisań pin–sieć zachowane. Fizyczne wymiary i modele mają ograniczenia w KOLIZJE_I_OGRANICZENIA.md.

Odczytano zapisany PCB ponownie natywnym pcbnew, sprawdzono wszystkie77 footprintów i padów, porównano netlistę z XML oraz bazowym stanem Git. Rozmiar100×100mm, dwie warstwy. ZERO elementów montowanych na BOTTOM; THT ma poprawne pady na obu warstwach. Nie utworzono ścieżek, przelotek ani polygonów. Dwie zone w pliku są wyłącznie keepoutami anten.

W trakcie pracy wykryto, że pcbnew.SaveBoard z domyślnym zapisem ustawień zastępował pięć warningów DRC ustawieniami ignore oraz listę arkuszy projektu. Przywrócono dokładny plik.kicad_pro z checkpointu; narzędzie używa teraz aSkipSettings=True. Końcowy DRC powtórzono na oryginalnej konfiguracji, ignored_checks=[], a hash.pro jest identyczny z baseline. Nie pozostawiono osłabionych kontroli.

Wyniki surowe: FINAL_ERC.json/.rpt i FINAL_DRC.json/.rpt, pełne polecenia w plikach *_command.json. Geometryczne kontrole własne: MECHANICAL_CHECK.json; wszystkie258 przypisań: FINAL_STATE.json. Dokumentacja bibliotek i licencji w ../FOOTPRINT-2_ZRODLA_I_LICENCJE.md i ../../licenses. Nie dodano nowego obcego modelu ani footprintu.
