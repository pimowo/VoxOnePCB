# Import projektu KiCad do VoxOnePCB

**Stan:** GitHub Connector ma potwierdzony odczyt i zapis. Dokumenty README.md, TODO.md, AGENTS.md i .gitignore opublikowano; aktualne pliki CAD wciąż są na laptopie.

## Co trafi do repozytorium

- Edytowalne `VoxOne_M1.kicad_pro`, `VoxOne_M1.kicad_sch`, `VoxOne_M1.kicad_pcb`.
- Projektowa biblioteka `VoxOne_M1.kicad_sym`, `sym-lib-table`, `fp-lib-table`, `footprints/**/*.kicad_mod`.
- Wyłącznie modele `models3d/`, do których istnieje prawo do publikacji, wraz z plikami przypisania i licencjami.
- Dokumentacja kluczowych pomiarów i rewizji w `docs/`. Historyczne ZIP i cache zostają poza Git.

## Import na lokalnym laptopie z Windows 10

1. Zachowaj dotychczasowe rewizje projektu i checkpointy bez zmian.
2. W oddzielnym folderze wykonaj `git clone https://github.com/pimowo/VoxOnePCB.git`.
3. Do klonu skopiuj **kopie** aktualnych plików z `%USERPROFILE%\Documents\VoxOne_M1_FOOTPRINT-2`, zachowując strukturę bibliotek i ścieżki `${KIPRJMOD}`. Nie przenoś ani nie usuwaj źródeł.
4. Przed dodaniem do publicznego repo zweryfikuj licencje zewnętrznych footprintów i modeli 3D, ewentualne dane prywatne oraz rozmiary plików.
5. Otwórz projekt w KiCad 10.0.4. Sprawdź czy schemat, PCB i lokalne biblioteki się otwierają; uruchom prawdziwy ERC/DRC i kontrolę sieci.
6. Zapisz raport porównania. Sprawdź `git status` i `git diff`, a commit/push wykonaj po zatwierdzeniu. Nie używaj `git push --force`.
7. Uruchamiaj Codexa w katalogu klonu, żeby czytał lokalne `AGENTS.md` i `TODO.md`. Aktualizacje wymagają `git commit` i `git push`.

## Obowiązujące ograniczenia

- PCB-PREVIEW-1 nie jest zatwierdzony do trasowania; można go przechować jako stan odniesienia.
- Nowy layout: maksymalnie 100 × 100 mm, wszystkie elementy na górnej stronie TOP, dwie warstwy ścieżek F.Cu/B.Cu, 4 × M3.
- FOOTPRINT-2 używa części prowizorycznych wymiarów modułów; nie publikować jako projektu produkcyjnie zweryfikowanego.
- Bez polecenia użytkownika nie przygotowywać nowego promptu, rozmieszczenia, ścieżek ani Gerberów.
