# Odstępy i ograniczenia

## Niepełne układy diagnostyczne A–D

Poniżej najlepsze testowane miejsce M3 w brakującym narożniku pokazanej diagnostyki. Ujemny margines oznacza naruszenie badanego kryterium, NIE minimalną zmianę wymiaru całej PCB. RF ma18.5 mm odśrodkałba doanteny(15+3.5),moduł3.7 mm(łeb3.5+0.2 rezerwy).

| Wariant | Narożnik1 TL2 TR3 BL4 BR | Pozycja M3 mm | Margines mm | Ograniczenie |
|---|---|---|---|---|
| 100×75 | 2 | (96.5;11.5) | -11.188 | RF BT |
| 100×75 | 4 | (96.5;71.5) | -3.100 | module DAC |
| 100×80 | 2 | (96.5;11.5) | -11.188 | RF BT |
| 100×85 | 2 | (96.5;11.5) | -3.700 | module DAC |
| 100×90 | 2 | (96.5;11.5) | -3.700 | module DAC |

75/80przykłady przenoszą DAC pod BT, tracąc także zgodność z preferowaną górną prawą sekcjąaudio.85/90trzymająDAC przygórze, ale prawy górny M3 przecina jegoobrys. Zmiana miejsca M3 poza badane narożne okno lub nowa organizacja modułów może zmienić wynik; nie uznano tych rozwiązań za zatwierdzone. Dokładne współrzędne w DIAGNOSTIC_LAYOUTS.json; diagramy tych wariantów NIE są kompletnymi PCB77 części.

## Pełny kandydat95

| Kontrola | Wynik |
|---|---|
| Obrysy modułów / inne części / korytarze / łby M3 | 0 wykrytych kolizji referencyjnych XY |
| RTC minimum | 2.175 mm do C602;2.275 mm do C601;2.500 mm do MAIN |
| RF innych części | 15.000 mm |
| RF metalowych łbówØ7 | 15.078 mm |
| M3 vs DAC | 0.500 mm rezerwy górnegoprawegołba do otoczki DAC |
| USBplug vsobrys zwykłejczęści | 0.325 mm |
| INPUTvs BT | 0.900 mm |
| AMPvs BT | 0.650 mm |
| Courtyard JP601–J603 | 0.110 mm po korekcie |
| Trasy/viapours | 0/0/0 |

Odległości są nominalne2D; nie są tolerancjami produkcyjnymi. Rezerwy palców, lutownicy, rozmiaru zespolonych wtyków i Z są **BLOCKED** do pomiarów. Nie utożsamiono courtyard DRC z pełną kontrolą3D. Modelami nie sprawdzono kolizji całychBT/DAC/RTC, ponieważ ichbrak. Nie ma udowodnionych kolizji referencyjnych, lecz nie wszystkie warunki wygody zostały zamknięte.

## Przyszłe ścieżki

To pakowanie mechaniczne, nie finalne rozmieszczenie elektryczne. Dwie USBdrogi i RF dzielą obszary routingu; można rozważyć sygnałyF/B, ale nie wykazano zakończonego prowadzenia wszystkich86 sieci. Nie dodano żadnej ścieżki ani płaszczyzny. Trzeba zachować powrotyI2S/SPI i odpowiednią termikęQ101/U101. Kondensatory DAC mają proste odległości pad1→A6VIN: C301 26.193,C302 24.789,C303 20.694 mm. To jawnie słabe położenia względem odsprzęgania, nie gotowy plan routingu; dokładniejsze grupowanie przed jakimkolwiekroutingiem. Przeniesienie ich pod DAC nie jest dozwolonym rozwiązaniem. MAINbulk C203 także znalazł się wśrodkowejstrefie, nie przywejściu MAIN — wymaga poprawy przy docelowym layoutcie. Niewykonane trasy nie dowodzą ani sukcesu, ani niewykonalności routingu.
