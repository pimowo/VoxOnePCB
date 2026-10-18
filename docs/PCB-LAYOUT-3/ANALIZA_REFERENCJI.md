# Analiza rzeczywiście obejrzanej referencji

Plik `C:\Users\piotrek\Documents\VoxOnePCB\docs\references\VoxOne_M1_REFERENCJA_LAYOUT.png` istnieje; 2531803 bajtów, rozmiar (1448, 1086), SHA-256 `cc7487bfb90f6f175aa9f644b957fa6ebec3a36b1cc95b1be0d12bb4cf1ce081`. Otwarty i obejrzany przed projektowaniem. Materiał dostarczony przez użytkownika jako wzorzec kompozycji, publikowany zgodnie z poleceniem w repo projektu. Nie przypisano obrazowi odrębnej otwartej licencji ani praw do dalszego rozpowszechniania poza tym poleceniem.

## Odczyt kompozycji

- Zielona płytka, duży MAIN w lewej części, pionowo, anteną ku górze, USB u dołu. Zasilanie w wąskim pasie po lewej; czytelna sekwencja wejście–zabezpieczenia–regulator.
- DAC w górnej prawej strefie z AUDIO obok. BT płasko po prawej, anteną w górę, USB w dół. RTC pomiędzy MAIN a BT, poniżej sekcji DAC, z własną rezerwą.
- U dołu osobne sekcje I2C DISPLAY, SPI DISPLAY, CONTROL, PULL-UP, AMP CONTROL. Zworki przyporządkowane funkcjom. Wyraźne ramki, nazwy, pin1 i napięcia.
- Cztery otwory w strefach narożnych; nadruk VoxOne_M1 i funkcje urządzenia. Inspiracją jest kompozycja i dostęp, nie ścieżki narysowane w koncepcji.

## Co przeniesiono do prawdziwego KiCad

MAIN anteną ku górnej krawędzi, oba USB w dół; uporządkowany lewy pas POWER; DAC u góry po prawej z jackiem na prawej krawędzi zgodnie z najnowszym poleceniem; osobny obrys BT i RTC; dolna kolejność I2C–SPI–INPUT–AMP; grupy zworek i oznaczenia 3V3/VCC/5V, SDA/SCL, ON/OFF. Nadruk i obrysy są rzeczywistymi obiektami PCB. Bez obrazów AI jako wyniku technicznego.

## Różnice koncepcji i footprintów

1. Referencja nie podaje skali, jej proporcji nie użyto jako wymiarów. Prawdziwa PCB jest kwadratem100×100mm.
2. MAIN ma rzeczywiście dwa USB-C i podstawkę2×22/25,40mm; obraz pokazuje przede wszystkim jeden port. Zarezerwowano dwa osobne wtyki i kable.
3. DAC w koncepcji jest szeroki i poziomy; wygląd gniazda nie dowodzi jego osi. W bibliotece jack przy0° jest skierowany w dół. Aby spełnić zatwierdzone RIGHT, cały footprint obrócono90°, co daje wąski pionowy obrys16,9×31,9mm. Nie obracano samych pinów ani nie wymyślano nowego modułu.
4. Złącza JST/kostki widoczne na obrazie zastąpiono wyłącznie istniejącymi goldpinami projektu. Nie dodano żadnego złącza ani pinu ARK.
5. RTC ma pięć pozycji z pin4NC, a nie cztery styki sugerowane samymi podpisami obrazu. Wemos to rzeczywiste wewnętrzne2×10, nie dowolne listwy narysowane w koncepcji.
6. Brak modeli pełnych BT/DAC/RTC uniemożliwia identyczny z referencją pełny render. Pokazano legalne istniejące podstawki i prawdziwe obrysy, nie fikcyjne bryły.
7. Zachowano wolne obszary RF/kabli i odstępy serwisowe, zamiast zapełniać je elementami. Dłuższa rezerwa kabli MAIN i JP601 oddalony od J601 są rzeczywistymi kompromisami opisanymi w KOLIZJE_I_BLOKADY.md.
