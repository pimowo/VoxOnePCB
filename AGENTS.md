# VoxOne_M1 — zasady pracy Codexa (lokalny projekt KiCad)

## Kanoniczny notatnik

**Przy każdym zadaniu najpierw przeczytaj cały `TODO.md` z katalogu głównego sklonowanego repozytorium `pimowo/VoxOnePCB`.** Jest kanoniczną listą decyzji, zadań, blokad, historii i wymaganych kontroli. Jeśli go brakuje, zgłoś to; nie zastępuj zgadywaną listą.

Klon repozytorium zawiera jedno kanoniczne `TODO.md` i `AGENTS.md`; nie rób konkurencyjnych notatników w katalogach rewizji. Starsze katalogi i checkpointy CAD pozostają niezmienionymi archiwami. Przed modyfikacją sprawdź `git status` i aktualność `main`, a po zatwierdzonym etapie aktualizuj TODO oraz wykonaj commit/push zgodnie z decyzją użytkownika. Nie nadpisuj cudzych lub lokalnych niezatwierdzonych zmian.

## Aktualne twarde wytyczne

- PCB VoxOne_M1 maksymalnie **100 × 100 mm**, **2 warstwy miedzi (F.Cu/B.Cu)**.
- **Wszystkie elementy wyłącznie po stronie TOP**. Zero elementów montowanych na BOTTOM. Pady/nóżki THT mogą być lutowane od spodu.
- Wzorem estetycznym jest **wcześniejsza wizualizacja VoxOne_M1**; obecne rozmieszczenie `PCB-PREVIEW-1` **nie zostało zaakceptowane**. W pierwszej kolejności należy przeprojektować rozmieszczenie, nie prowadzić ścieżek.
- Moduły MAIN, BT, PCM5102A i RTC mają być wymienne. Nie zgaduj ich mechaniki i rozstawu pinów; dane biblioteczne to warianty referencyjne.
- Nie zmieniaj zatwierdzonej mapy GPIO, schematu, wartości, zasilania ani połączeń bez wyraźnego polecenia.
- **Aktualnie użytkownik nie ma dostępu do laptopa i nie chce nowego promptu/prac nad PCB, dopóki sam o to nie poprosi.** Ten plik nie upoważnia do samodzielnego rozpoczęcia etapu.

## Zasady jakości i raportowania

- Pracuj na **Windows 10 / lokalnym KiCad 10.0.4**, bez używania serwera DEV.
- Przed modyfikacją kopia projektu i checkpoint; po modyfikacji netlisty, rzeczywiste ERC/DRC, przegląd 2D/3D i brak fałszywego `PASS`.
- Nie maskuj błędów ERC/DRC, nie przypisuj niezgodnych footprintów dla samego usunięcia ostrzeżeń.
- Nie eksportuj Gerberów ani nie zlecaj produkcji bez odrębnej zgody użytkownika.
- **Zapisz pełną końcową odpowiedź w nowym pliku `NAZWA_ETAPU_ODPOWIEDZ_CODEX.md`**, również gdy podsumowanie zostało pokazane w terminalu. Dodaj wyniki, blokady, raporty, kontrolę checkpointu i dokładne ścieżki.
- Po ukończonym zatwierdzonym etapie uaktualnij status odpowiednich punktów `TODO.md` oraz dopisz datowany wpis historii. Nie zmieniaj `APPROVED` na `DONE` bez rzeczywistego wykonania i weryfikacji.

Ostatnie raporty: `FOOTPRINT-2_ODPOWIEDZ_CODEX.md`, `PCB-PREVIEW-1_ROZMIESZCZENIE.md`, `PCB-PREVIEW-1_KOLIZJE_I_BLOKADY.md`.

## Zasady repozytorium GitHub

- Repozytorium: `https://github.com/pimowo/VoxOnePCB`, gałąź `main`, **publiczne**. Nie mylić z repozytoriami firmware `VoxOne` i `VoxOneBT`.
- Do repo mają trafić źródła KiCad, lokalne biblioteki i tylko modele/footprinty dopuszczone do redystrybucji; bez prywatnych sekretów i zbędnych archiwów ZIP.
- Obecna lokalna referencja projektu CAD to `%USERPROFILE%\Documents\VoxOne_M1_FOOTPRINT-2`; to projekt `PROVISIONAL` z odrzuconym rozmieszczeniem. **Nie importuj projektu CAD z tego katalogu bez polecenia i weryfikacji**.
- Prowadź dalszą pracę na laptopie z Windows/KiCad, nie na serwerze DEV. Przed publikacją/commit sprawdzaj licencje obcych modeli 3D, poufne dane i rozmiary plików.
- Użytkownik nie zatwierdził trasowania, Gerberów ani kolejnego rozmieszczenia.