# USB, jack, złącza i serwis — PROVISIONAL

## MAIN

Antena przygórze0.5 mm, USBdownface Y63.9, dofrontu FR4 31.1 mm. Dwa rezerwowane wtyki9×18 mm zajmują X21.5..30.5 oraz34.5..43.5,Y63.9..81.9. KableØ4 mają oddzielne drogi do dolnej krawędzi. Nie prowadzono kabli nad drobnicą. Na75/80część wtyków wychodziłaby6.9/1.9mm poza FR4 — samo to nie jest zakazanym zwiększeniem laminatu.

Najmniejszy odstęp zarezerwowanego wtyku od natywnego obrysu zwykłej części wynosi0.325 mm: C103 przy USB1, C402/C502przyUSB2. Dla SMD jest to większa otoczka courtyard/Fab, a nie wyłącznie bryła ceramiczna. **Nie uznaje się tego za potwierdzenie wygody wkładania, palców, tolerancji i każdej odgiętki.** Potrzebny pomiar konkretnych2 wtyków oraz test jednoczesnego wkładania. Wysokości Z nie są znane.

## BT / DAC

Płytka BT kończy się Y91.23; źródłowy obrys obudowa USB sięga Y97.58, czyli2.58 mm poza95 mm FR4. Wtyk18 mm liczono od czoła tej obudowy, a nie od końca PCBmodułu: korytarz kończy się Y115.58,20.58 mm poza FR4. To konserwatywna korekta dawnego sposobu pokazywania rezerwy, bez zmiany modułu. Obudowa urządzenia musi uwzględniać ten występ.

Jack DACface X100,Y12.90..17.60, na prawej krawędzi; wtyk18×9 mm poza PCB. Rysunek obrysu i rezerwy nie dowodzi dokładnej pozycji gniazda w realnym klonie. H1–H4 dostęp odgóry; dokładnych współrzędnych oraz wysokości nie potwierdzono. AUDIOJ301 przysekcji, ale odbiega od koncepcyjnego skrajnieprawego wyjścia zreferencji.

## Złącza / zworki

I2C/SPI/INPUT przydolnej krawędzi;AMP na prawym dolnym boku, nie w jednym poziomym szeregu. Typy goldpinów bez zmian. Nie utożsamiać ich nominalnego plastiku2.54 mm z dowolną wiązką kablową. Pełne wtyki zespolone, ich szerokość, wyprowadzenie przewodów w Z i miejsce na chwyt są niepotwierdzone. J601–BT ma0.900 mm odstępu nominalnych obrysów;J603–BT0.650 mm. JP601–J603 courtyard mają0.110 mm bez nakładania; to mała rezerwa, nie gwarancja wygody zakładania zworek.

| Zworka | Odległość origin do właściwego złącza mm | Ocena |
|---|---|---|
| JP501 | 13.065 | nie jest oceną palców/Z |
| JP502 | 9.867 | nie jest oceną palców/Z |
| JP601 | 19.092 | nie jest oceną palców/Z |
| JP602 | 21.662 | nie jest oceną palców/Z |

JP602 zachowuje1–2SDA,3–4SCL;JP6011–2S1,3–4S2,5–6KEY. JP501/502wybierająwyłącznieVCC. Bezpodstawnie nie zmieniano podciągania/połączeń. Samego istniejącego nadruku nie przebudowywano na docelowy produkt; referencje kandydata umieszczono na F.Fab dla analizy, pełna tabela montażowa jest w ROZMIESZCZENIE_77.md.

ARK przy lewej krawędzi, przewód wchodzi odlewej. TorF101/Q101/TVS/C101/U101w lewym pasie, dostęp śrubokrętem odgóry. Narzędzie, promieńgięcia kabla, wysokość elektrolitów i obudowa wymagają fizycznej weryfikacji. Nie przyjęto prowadzenia kabli lub lutownicy przez obrys MAIN.
