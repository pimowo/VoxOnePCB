# PCB-LAYOUT-3 — niezależny baseline

Data2026-10-18; lokalny Windows10, KiCad CLI/pcbnew10.0.4. Przeczytano całe AGENTS.md, TODO.md i cztery wymagane raporty PCB-LAYOUT-2. Nowe polecenie użytkownika upoważnia do layout3, zastępując historyczne oczekiwanie na polecenie, lecz nie zatwierdza routingu.

Źródło `origin/pcb-layout-2`, commit `1d2da877b73ca1ea3dc309bd2993f96a8883545e`, zgodne z lokalną pcb-layout-2 po `git fetch origin --prune` i `git ls-remote`. Nie było gałęzi pcb-layout-3 ani lokalnie, ani zdalnie. Jedyna nieśledzona zmiana: oczekiwana referencja PNG. Utworzono osobną gałąź od origin/pcb-layout-2. Main pozostał `1ca3e40e3600f005977bc504b272e34483b30150`. Nie modyfikowano katalogów FOOTPRINT-1/2 ani firmware i nie używano DEV.

| Kontrola wykonana przed zmianą | Wynik |
|---|---:|
| Elektryczne / footprinty z4M3 | 77 / 81 |
| TOP / BOTTOM | 77 / 0 |
| Sieci / ref-pin-net | 86 / 258 |
| ERC errors / warnings | 0 / 0 |
| DRC niepołączenia / inne naruszenia | 173 / 0 |
| Schematic parity / ignorowane kontrole | 0 / 0 |
| PCB / warstwy | 100×100mm / 2 |
| Ścieżki / przelotki / wypełnienia miedzi | 0 / 0 / 0 |

KiCad Copilot MCP get_project_info potwierdził wersję10.0.4, projekt i pojedynczy arkusz A2. Natywne otwarcie PCB, wszystkich lokalnych bibliotek i porównanie wszystkich258 par ze schematem potwierdzone w BASELINE_STATE.json. Nie używano wadliwego importu PCB MCP; operacje geometrii i zapis wykonywano przez pcbnew, SaveBoard(...,aSkipSettings=True).

Checkpoint pełnego wejścia poza Git: `C:\Users\piotrek\.codex\attachments\PCB-LAYOUT-3_CHECKPOINT\PCB-LAYOUT-2_BEFORE.zip`. 113 plików, test CRC i SHA-256 każdego pliku poprawny. SHA-256 ZIP `1c7d30e65e5a9143f03839df993fa00fe9fb87b13fd54b71ee47b24a69a1d35a`. Bez zagnieżdżonych ZIP, .git i cache; lokalne wstrzymane modele zachowane tylko w prywatnym checkpointcie. Manifest źródeł: BASELINE_MANIFEST.json oraz `C:\Users\piotrek\.codex\attachments\PCB-LAYOUT-3_CHECKPOINT\SOURCE_SHA256.json`.

## Modele wejściowe

Model MAIN działa lokalnie, lecz jest ignorowany przez Git (nierozstrzygnięte prawa GrabCAD). DAC STEP nieaktywny i niepublikowany. Nie ma pełnych bryłBT/RTC/F101. C101 modelH16 zamiast docelowegoH12,5. Każdy aktywny plik modelu lokalnie istnieje; czysty klon nie ma bryłyMAIN. Biblioteki i licencje zachowano bez zmian. Szczegóły wszystkich ścieżek w BASELINE_STATE.json/model_status.
