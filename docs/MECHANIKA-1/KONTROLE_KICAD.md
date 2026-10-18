# Kontrole rzeczywistym KiCad10.0.4

| Kontrola | Źródło layout3 | Kandydat 100×95 |
|---|---|---|
| ERC: błędy/ostrzeżenia | 0/0 | 0/0 |
| DRC: niepołączenia | 173 | 173 |
| Inne naruszenia DRC | 0 | 0 |
| Zgodność schematu i PCB | 0 | 0 |
| Wykluczenia kontroli | 0 | 0 |
| Elementy elektryczne TOP/BOTTOM | 77/0 | 77/0 |
| Footprinty z otworami | 81 | 81 |
| Sieci | 86 | 86 |
| Pin–sieć | 258 | 258 identyczne |
| M3Ø3.2 | 4 | 4 |
| Cu layers | 2 | 2 |
| Nominalne FR4 mm | 100×100 | 100×95 |
| Ścieżki/via/copperfills | 0/0/0 | 0/0/0 |

Nie jest to DRC PASS:173 niepołączenia są rzeczywistym wynikiem braku trasowania. Bez wykluczeń i bez wyłączania kontroli. Końcowe ERC/DRC JSON/RPT i pełne polecenia CLI są w candidates/100x95_PROVISIONAL; bazowe w tym katalogu. Natywny LoadBoard po zapisie i geometryczny test wszystkich 81 footprintów, w tym 77 bibliotek, wykonano niezależnie od wcześniejszych raportów. Zachowano wszystkie UUID, pady, funkcje i wartości oraz 79 mapowań modułów.

Schemat kandydata jest identyczną kopią źródła A2;pro jest identyczne bajtowo — SaveBoard używa aSkipSettings=True. Główne CAD, biblioteki, symbole i modele pozostały identyczne, co sprawdzono SHA-256. W kandydacie technicznie zmieniono jedynie względne ścieżki do współdzielonych bibliotek/modeli: `${KIPRJMOD}/../../../../...`; lokalne footprinty i ich pady są oryginalne. Nie dublowano bibliotek STEP ani nie publikowano wstrzymanych plików.

Kandydat nie ma opracowanego produkcyjnego nadruku. Referencje są na F.Fab;0 ostrzeżeń nadruku nie jest deklaracją kompletności nadruku. Własne opisy geometryczne i korytarze są na Dwgs/Cmts;2 keepouty są prawdziwymi ruleareas obu Cu, nie tylko rysunkiem.

3D jest natywnym renderem KiCad: dostępne rzeczywiste modele dyskretne/podstawki i lokalny MAIN. Nie pokazuje pełnych BT/DAC/RTC/F101; nie udaje ich zastępczymi bryłami. C101 ma wcześniejszy model H16. Obraz 3D nie potwierdza rzeczywistych wysokości ani kompletnego wykrywania kolizji.
