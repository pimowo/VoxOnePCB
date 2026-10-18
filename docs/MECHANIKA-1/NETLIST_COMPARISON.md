# Niezależne porównanie netlist

Wyeksportowano osobno KiCad CLI `BASELINE.net.xml` ze źródła i `candidates/100x95_PROVISIONAL/NETLIST.xml` ze schematu kandydata. Porównano słownik (oznaczenie, numer pinu) → nazwa sieci, normalizując wyłącznie techniczny zapis `{slash}`. Wynik: **258/258 identycznych par, 86 sieci, 77 elementów**. Niezależnie porównano te same pary z natywnym PCB oraz wszystkie lokalne geometrie i UUID padów. Nie ma nowych zwarć, rozłączeń ani utraty komponentów. Każdy z 79 padów MAIN/BT/DAC ma zachowaną funkcję i sieć; dane w DETAIL_METRICS.json.

Głównego schematu/PCB/projektu ani bibliotek nie edytowano. Kopia A2 i konfiguracja kandydata są bajtowo identyczne ze źródłem; zmieniono pozycje/orientacje elementów, mechaniczne rysunki/keepouty i techniczne względne ścieżki bibliotek/modeli wyłącznie w kandydacie. Nie wykonano routingu.
