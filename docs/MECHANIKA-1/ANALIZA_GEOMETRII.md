# MECHANIKA-1 — metoda i granice wniosku

2026-10-18. PROVISIONAL / NOT FOR MANUFACTURING. Analiza lokalna Windows10 / KiCad10.0.4. Głównego CAD nie zmieniono. Wymiary pozostają PENDING.

## Materiały i aktualność

Przeczytano całe AGENTS/TODO, raport końcowy layout3, MECHANIKA_I_ODSTEPY, ROZMIESZCZENIE i KOLIZJE_I_BLOKADY. PNG referencji otwarto i obejrzano. Pobrano origin; źródło CAD: `8ed4cac3a92b1daa9433e69b296bed1a4cbf3cc8`; nowsze decyzje prostokąta/TODO i dokument wstępny odczytano bezpośrednio z origin/main `fb697a86297372d1b7ff51638d4cad441b283bcf`. TODO na gałęzi roboczej uzgodniono z obiema historiami bez merge i bez cofania najnowszej decyzji.

Referencja potwierdza MAIN lewa/antenaUP, DAC górna prawa, BT prawa, RTC środek, POWER lewa, strefę złączy niżej. Obraz nie jest rysunkiem wymiarowym. Nie skopiowano JST, dodatkowych pinów ARK ani koncepcyjnych proporcji modułów. Rzeczywisty DAC musi być obrócony o90° z powodu jego prostopadłych rzędów i jacka.

## Etap A — jawna rodzina przeszukiwania

Sprawdzono100×75/80/85/90/95mm. Wszystkie moduły mają stałe dopuszczone orientacje; MAIN0°, DAC90°, BT0°, RTC0°. Przesuwano MAIN X=[12,14,16,16.5,17,18,20], BT X=[46,48,50,52,54,56,58,59.5,60,62,64,66,68], DAC top co0.5 mm, BT top co1 mm. Sprawdzano zarówno stos DAC/BT, jak i układy boczne/staggered. Odstęp innych części od obu anten≥15 mm — zachowane konserwatywne kryterium layout3, nie nowy pomiar RF.

M3 badano z okrągłymi łbamiØ7 w narożnych oknach: odsunięcia3.5/5/7/9/11.5mm. Jest to jawna operacyjna interpretacja „przy narożnikach”, a nie zatwierdzony wzór otworów obudowy. Nie przeszukano kontinuum wszystkich położeń. Dla RTC szukano13.4×13.4 mm centralnie X42..75,Y18..H−15, z≥2 mm do modułów i≥15 mm RF. Korytarze dwóch wtyków MAIN9×18, kabliØ4 do krawędzi, BT housing+plug oraz jacka sprawdzano w XY. Zewnętrzne wtyki mogą wystawać; nie wymagano bezpodstawnie, aby całe wtyki były na FR4.

`MACRO_SEARCH.json` zawiera wyniki i diagnostyczne układy. Brak rozwiązania w tej rodzinie jest **BLOCKED**, nie globalnym dowodem INFEASIBLE. Przykłady odrzuconych pozycji pokazują konkretne konflikty, ale nie dowodzą, że inna konstrukcja nie może istnieć. Nie obliczono matematycznego globalnego minimum wysokości.

## Etap B

Tylko95 mm przeszło tę bramę obrysów; utworzono jeden pełny niezależny kandydat, zamiast sztucznie tworzyć2–3 niepoprawne PCB. Rozmieszczono77/77 istniejących części i4 otwory, bez drobnicy pod modułami. Pierwsza iteracja miała1 nakładanie courtyard JP601/J603; zachowano wynik ITERATION1_DRC.json i poprawiono pozycje, nie reguły. Wykonano odczyt po zapisie przez pcbnew, wszystkie biblioteki/pady/nety, rzeczywisty ERC i DRC z parity, SVG i render3D KiCad.

## Znaczenie statusu

100×95 jest **PROVISIONAL FEASIBLE dla referencyjnego pakowania XY**. Nie oznacza potwierdzonej wygody serwisu, wysokości, wszystkich rzeczywistych wtyków ani routowalności. Pełna brama mechaniki pozostaje **BLOCKED** przez tolerancje i ciasne korytarze opisane osobno. Nie zatwierdzono wymiaru. Dla 75–90 pozostaje BLOCKED; nie wpisano INFEASIBLE tylko z powodu braku wyniku siatkowego.
