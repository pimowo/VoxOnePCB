# Rekomendacja do rozważenia, nie wybór wymiaru

Najbardziej obiecujący jest **100×95 mm**: jedyny zbadany rozmiar, dla którego utworzono i niezależnie sprawdzono pełny kandydat z 77 elementami TOP i 4 otworami M3, zachowane 258 połączeń,2 strefy RF keepout, bez ukrytych części i bez tras. Dla 75–90 nie zamknięto już bramy makrogeometrii; pozostają BLOCKED, nie udowodnione INFEASIBLE.

95 ma status **PROVISIONAL FEASIBLE wyłącznie dla nominalnego pakowania XY**. **Nie ogłaszam pełnego spełnienia wygody serwisu ani gotowości layoutu.** Brama mechaniki/serwisu pozostaje BLOCKED:0.325 mm przy korytarzach USB,0.9 mm INPUT–BT,0.65 mm AMP–BT,0.11 mm courtyard JP601–AMP,nieznane wtyki/Z. Do tego 2.58 mm obudowa USB BT poza FR4 i 20.58 mm do końca konserwatywnego wtyku. To wymaga oceny użytkownika/obudowy, nie automatycznej akceptacji.

Kompozycja zachowuje MAIN po lewej z anteną w górę, DAC u góry po prawej z jackiem na zewnątrz, BT po prawej, RTC między modułami i POWER po lewej. Proporcja100:95 jest mało wydłużona i wizualnie odbiega od PNG. AMP jest na bocznym dolnym brzegu; nie uzyskano jednego rzędu wszystkich złączy. Odległe odsprzęganie DAC/MAIN i JP602 nie są poprawą gotowego projektu. Ten kandydat dowodzi upakowania footprintów, a nie dobrego finalnego produktu.

## Co trzeba dostarczyć / zdecydować

1. Pomiary suwmiarką i zdjęcia góra/dół/bok MAIN:25.40 mm rzędów, pełny obrys z anteną, oba czoła USB i ich rozstaw, pin1, elementy spodnie. Nie wystarcza nazwa DevKitC-1.
2. BT:22.86 mm wewnętrznych rzędów,30.48×36.83 obrys, faktyczne wystawanie USB, antena i prześwit.
3. DAC:prostopadłe A1–A6 i B1–B9, raster, całość z jackiem, czoło jacka oraz H1–H4 i miejsce do zdjęcia modułu. Wyjaśnić rozbieżność 18.5 versus 17.45 mm z fizycznym egzemplarzem.
4. RTC:13.4×13.4 wraz z baterią i położenie gniazda 1×5 względem obrysu; wysokość zestawu.
5. Konkretne gniazda żeńskie MAIN/BT/DAC: producent/typ, wysokość dystansu, długości pinów i elementy od spodu. Nie potwierdzono 8.5 mm.
6. Oba wtyki USB-C i USB Wemosa: szerokość, wysokość, długość obudowy i odgiętki, średnica/promień gięcia kabla; zdjęcia suwmiarką. Także jack 3.5 mm i wtyki/wiązki I2C/SPI/INPUT/AMP oraz shunty.
7. Obudowa: czy pozwala na występ BT 2.58 mm i kable poza PCB, asymetryczny H901 y11.5, łby/podkładkiØ7, pionowe chwytanie modułów i śrubokręt ARK. Większe podkładki wymagają przeliczenia.
8. Dopiero po ocenie raportu użytkownik zatwierdza wymiar (M1-P0-16 PENDING). Jeśli oczekiwany jest wyraźnie szerszy wygląd 75–85 mm, potrzebna dalsza analiza innej organizacji/M3; nie wolno bez decyzji redukować RF ani montować pod modułami.

Żadnego głównego CAD nie przebudowano. Nie rozpoczęto produkcyjnego layoutu prostokąta, trasowania, Gerberów ani kolejnego etapu.

## Konkretna alternatywa dla dalszej decyzji o M3

Można rozważyć osobne badanie 100×90 mm z MAIN X17, DAC top0.5 i BT X60/top48 oraz RTC (48;19.6)…(61.4;33.0) mm. Te cztery obrysy mieszczą się przy zachowaniu buforów RF. Prawy górny otwór trzeba wtedy odsunąć z naroża np. do (77.5;3.5) mm: aż22.5 mm od prawej krawędzi. Odległość łba Ø7 od lewej krawędzi DAC wyniosłaby0.5 mm. To wykracza poza przyjęte narożne okno11.5 mm i wymaga decyzji o obudowie oraz dalszego badania wszystkich77części. **Nie jest to zatwierdzony ani zweryfikowany pełny wariant PCB.** Nie twierdzę, że90 mm wymaga właśnie tego rozwiązania lub że77części na pewno się w nim zmieści. Przykład pokazuje, dlaczego nie wolno globalnie nazwać90 mm INFEASIBLE na podstawie bieżącej siatki.
