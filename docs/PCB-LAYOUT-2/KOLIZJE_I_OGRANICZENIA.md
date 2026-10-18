# Kontrola mechaniki i otwarte ograniczenia

## Wynik geometrii referencyjnej

0 wykrytych kolizji element–element, element–pełny obrys modułu, element–rezerwa M3 oraz element–korytarz USB/jack.0 elementów pod modułami.4 otwory NPTH3,2mm i rezerwa7mm pod łby/podkładki. Wszystkie źródłowe środki, rozmiary padów i wiercenia zgodne z bibliotekami. Footprinty nie zmieniły ID ani numeracji.

Najmniejsza odległość obrysu innego elementu do referencyjnego obszaru anten wynosi **15.105mm**. Sprawdzono euklidesową odległość prostokątnych obrysów wszystkich zwykłych komponentów. Własne podstawki i elektronika danego modułu są odrębnym montażem. Odstęp15mm zaczerpnięto z [wytycznych Espressif](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32/pcb-layout-design.html?highlight=antenna), nie z pomiaru klona. To analiza referencyjnego położenia anteny, nie test RF.

Na obu warstwach istnieją dwie prawdziwe strefy zakazu miedzi w projekcjach anten MAIN/BT. Dodatkową przestrzeń15mm zachowano dla innych elementów. PCB w całości nie ma miedzi trasowania/pól. Przed przyszłym prowadzeniem masy trzeba uwzględnić pełny zalecany obszar RF, punkty zasilania anten i własne pady DevKitów; nie wolno automatycznie wypełnić wolnych miejsc polygonemGND.

## Dostęp

MAIN USB1: korytarz(65,50)…(74,53), USB2:(78,50)…(87,53), wtyki wychodzą górą. DAC jack: korytarz(109.5,45)…(118.5,55.55), wychodzi górą. BT USB: (121,141.83)…(131,155), wychodzi dołem. Rezerwy wtyków wychodzą poza laminat: górą5mm dla jacka i dołem5mm dla BT. Są orientacyjnymi rezerwami kabli, nie potwierdzeniem gabarytów ani zgodą na konkretną obudowę. Referencyjne PCB modułów/anteny i obudowy USB mieszczą się w100×100mm. Dopasowanie rzeczywistych klonów może zmienić ten wynik i wymaga wtedy zatwierdzenia wyjątku.

RTC przesunięto nieco powyżej środka, żeby zostawić RF BT. Najmniejsza rezerwa referencyjnego obrysu RTC do C203 jest około0,405mm, a do kolumnySMD około0,625mm. To wąskie miejsca tolerancji i serwisu; nie uznawać wyjmowania płytki palcami za potwierdzone. Pozostałe moduły także wymagają próby wkładania/wyjmowania z rzeczywistymi żeńskimi listwami.

## Nadal BLOCKED przed fizyczną weryfikacją/produkcją

1. MAIN: potwierdzić wariant44-pin N16R8/2×USB-C, raster2,54, rozstaw25,40, rzeczywiste28×57 i rozmiar anteny względem referencyjnego STEP. Rezerwa tu obejmuje dodatkowe6,4mm. Potrzebne zdjęcia góra/dół/bok z suwmiarką, pin1, środki rzędów, USB i elementy spodnie.
2. BT: potwierdzić wewnętrzne2×10,22,86mm, raster2,54, pełny obrys, USB/antenę i wysokości. Zdjęcia i pomiary obu wewnętrznych rzędów, nie zewnętrznych.
3. DAC: współrzędne A1–A6/B1–B9 względem naroży, obrys31,9×16,9, jack/H1–H4 i wtyk. Rysunek footprintu odwrócono jako całość; rzeczywisty klon i błędny STEP nie są zweryfikowane. Model odłączony pozostaje odłączony. Nie zmieniono XSMT/mostków.
4. RTC: potwierdzić13,4×13,4, przesunięcie płytki względem pin1, baterię i wysokość. Pin4NC zatwierdzony elektrycznie, zachowany.
5. Konkretne podstawki, długości pinów, prześwit, całkowita wysokość USB/jack/elementów i łbów M3 oraz obudowa kabli.8,5mm to dawne założenie; ten layout nie wykorzystuje miejsca pod modułami. Brak dowodu pełnej zgodnościZ.
6. Brak dokładnych bryłBT/RTC/DAC/F101. C101 nadal modelH16 zamiast docelowegoH12,5. Natywna wizualizacja przedstawia dostępne prawdziwe modele i gniazda, a nie fikcyjne płytki. Brak bryły nie dowodzi braku kolizji.
7. ModelMAIN STEP dostępny tylko lokalnie, ignorowany przez Git wraz z nieaktywnym DAC STEP. Nie kopiowano ich do publicznego repo. Warunki redystrybucji i atrybucje modeli nadal M1-GIT-05/P1-18; lokalny podglądMAIN zachowuje pochodzenie YD/DavidScambell/GrabCAD. Czysty klon pokaże podstawki bez bryłyMAIN. Pozostałe modele KiCad i licencje są w repo bez zmian.
8. Dostępny zamiennik10µF/16V/D5/P2 dla EOL referencji, obciążenia/termika/USB+5V, mostki DAC, BL i EN/MUTE pozostają wcześniejszymi blokadamiP1. Ten etap nie wykonuje pomiarów ani nie zmienia tych układów.

Część rezystorów i stopień resetuBT odsunięto od modułów z powodu wymagańRF i braku drobnicy pod płytkami. Po akceptacji mechaniki trzeba osobno ocenić docelowe odległości/trasę I2S i rozmieszczenie33Ω względem wyjść MAIN. Nie rozpoczęto routingu i nie potwierdzano jakości przyszłych ścieżek na podstawie samego placementu. Nie jest to zatwierdzenie produkcyjne.

Kontrola courtyard to tylko jedna kontrola2D. Nie wykonano dokładnej analizy brył STEP–STEP dla nieobecnych modeli, termiki, EMC ani rzeczywistego wkładania modułów. Nie ukryto tych ograniczeń.
