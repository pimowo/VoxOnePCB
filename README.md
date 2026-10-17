# VoxOnePCB — VoxOne_M1

Repozytorium projektu płytki **VoxOne_M1** (KiCad 10.0.4). Oddzielone od firmware VoxOne/VoxOneBT.

## Dokumentacja

- [TODO.md](TODO.md) — **kanoniczny notatnik** zadań, zatwierdzonych wytycznych, blokad i historii.
- [AGENTS.md](AGENTS.md) — zasady pracy lokalnego Codexa.
- [docs/IMPORT_KICAD.md](docs/IMPORT_KICAD.md) — bezpieczne przeniesienie źródeł projektu na GitHub.

## Zatwierdzone wymagania PCB

- Laminat maksymalnie **100 × 100 mm**; cztery otwory M3.
- **2 warstwy miedzi**, ścieżki TOP i BOTTOM.
- **Wszystkie elementy montowane wyłącznie od góry (TOP)** — SMD i THT, moduły, goldpiny, zworki.
- MAIN po lewej, DAC w górnej prawej części, BT po prawej, RTC blisko środka, dolna strefa uporządkowanych złączy: **wytyczna koncepcyjna**, wymagająca mechanicznej kontroli.
- Moduły MAIN/BT/DAC/RTC wymienne.

## Stan projektu

Ostatnia importowana rewizja: **FOOTPRINT-2 + PCB-PREVIEW-1**. Według raportu Codexa: ERC 0 błędów i 0 ostrzeżeń; wstępne PCB 100 × 100 mm bez trasowania. **Rozmieszczenie PREVIEW-1 zostało odrzucone.** Nie tworzyć Gerberów ani nie trasować tej wersji. Geometrie trzech dużych modułów są referencyjne (PROVISIONAL), niepotwierdzone na fizycznych egzemplarzach.

**Źródła projektu KiCad i biblioteki są już opublikowane w repozytorium**, od bazowego commita [`8d90e6d`](https://github.com/pimowo/VoxOnePCB/commit/8d90e6df444f770a445944372fa62b5ebb39af9). W repo znajdują się pliki `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, projektowe biblioteki footprintów/symboli i wybrane modele 3D. Z publikacji wyłączono modele `YD-ESP32-S3.step` i `PCM5102-I2S.step` do dalszej weryfikacji praw. Po imporcie projekt otwarto w KiCad 3D, ale **należy ponownie wykonać ERC/DRC/netlist na czystym klonie**. Wersja jest PROVISIONAL i nie jest zatwierdzona do produkcji.

## Dostęp i prawa

Repozytorium jest **publiczne**. Nie publikować kluczy, haseł, danych prywatnych, ani obcych modeli 3D/bibliotek bez zgodnej licencji. **Licencja własnego projektu nie została jeszcze wybrana** — nie dodawać `LICENSE` automatycznie.