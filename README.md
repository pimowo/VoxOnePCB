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

Ostatnia lokalna rewizja: **FOOTPRINT-2 + PCB-PREVIEW-1**. Według raportu Codexa: ERC 0 błędów i 0 ostrzeżeń; wstępne PCB 100 × 100 mm bez trasowania. **Rozmieszczenie PREVIEW-1 zostało odrzucone.** Nie tworzyć Gerberów ani nie trasować tej wersji. Geometrie trzech dużych modułów są referencyjne (PROVISIONAL), niepotwierdzone na fizycznych egzemplarzach.

**Pliki źródłowe `.kicad_pro`, `.kicad_sch`, `.kicad_pcb` i lokalne biblioteki są na razie wyłącznie na laptopie użytkownika, nie w tym pakiecie dokumentacyjnym.** Ich import jest osobnym etapem po powrocie do laptopa i sprawdzeniu licencji.

## Dostęp i prawa

Repozytorium jest **publiczne**. Nie publikować kluczy, haseł, danych prywatnych, ani obcych modeli 3D/bibliotek bez zgodnej licencji. **Licencja własnego projektu nie została jeszcze wybrana** — nie dodawać `LICENSE` automatycznie.