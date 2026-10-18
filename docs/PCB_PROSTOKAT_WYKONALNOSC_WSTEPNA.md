# VoxOne_M1 — wstępna ocena prostokątnej PCB (2026-10-18)

**Status:** analiza danych referencyjnych, NIE weryfikacja rzeczywistych modułów. **Nie jest to zatwierdzenie wymiaru ani polecenie projektu nowego PCB.**

## Zatwierdzenie użytkownika

- PCB w orientacji poziomej: szerokość większa niż wysokość.
- Obie krawędzie laminatu nie większe niż 100 mm.
- Referencja wyglądu: `docs/references/VoxOne_M1_REFERENCJA_LAYOUT.png`.
- Wszystkie części montowane wyłącznie TOP, ścieżki dopuszczone na F.Cu i B.Cu.
- 4 otwory M3, osobne strefy RF, wymienne MAIN/BT/DAC/RTC.
- MAIN lewa strona, antena przy górnej krawędzi i USB na dole; DAC przy górnej/prawej krawędzi i jack na zewnątrz; BT prawa strona; złącza użytkowe łatwo dostępne.
- Przed ustaleniem wymiaru przeprowadzić analizę wykonalności, uwzględnić kable, gniazda, montaż i brak elementów pod modułami.

## Co wynika z aktualnego projektu PCB-LAYOUT-3

Źródło: [MECHANIKA_I_ODSTEPY.md](../PCB-LAYOUT-3/MECHANIKA_I_ODSTEPY.md), [ROZMIESZCZENIE.md](../PCB-LAYOUT-3/ROZMIESZCZENIE.md) z gałęzi `pcb-layout-3`. Wymiary są **biblioteczne/prowizoryczne**.

| Grupa | Referencyjna zajętość / problem |
|---|---|
| MAIN | pełny obrys razem z rezerwą anteny: 28 × 63,4 mm; dodatkowo oba USB i rzeczywiste kable potrzebują korytarza ku dolnej krawędzi |
| DAC | po obrocie z jackiem w prawo: obrys ok. 17,45 × 31,9 mm; sama rezerwa wtyku jacka wychodzi ok. 18 mm poza prawą krawędź |
| BT | obrys ok. 30,48 × 36,83 mm, antena u góry i USB u dołu; własna obudowa USB i wtyk mogą wystawać poza laminat |
| RTC | obrys ~13,4 × 13,4 mm; referencyjnie minimum 2,095 mm odstępu od innych elementów w obecnym projekcie |
| Prawe strefy DAC/BT | w obecnym układzie DAC rozciąga się Y 59,05–90,95, BT Y 108,5–145,33. Łączna wysokość obu z przerwą to **86,28 mm**, nie licząc zewnętrznych kabli |
| M3 | cztery otwory Ø3,2 mm z referencyjną rezerwą łbów Ø7 mm; obecny układ otworów nie tworzy już prostego symetrycznego prostokąta |
| Złącza i drobnica | dolne J501/J502/J601/J603, JP501/JP502/JP601/JP602; obecnie INPUT i obrys BT oddalone tylko o ok. 0,4 mm |

### Wniosek wstępny

1. **Samo przycięcie PCB-LAYOUT-3 do prostokąta nie jest rozwiązaniem.** Trzeba przeprojektować pozycje i korytarze dostępu.
2. Proporcjonalny do wizualizacji wariant około **100 × 75 mm** jest **bardzo wymagający**: obecna pionowa zajętość prawej strony wynosi ok. 86,28 mm. Nie dowodzi to niemożliwości przy nowym rozmieszczeniu, ale obecny układ by się nie zmieścił bez zmian. MAIN z anteną i dostępem do USB także potrzebuje szczególnej uwagi.
3. Warianty testowe do symulacji układu: **100 × 75, 100 × 80, 100 × 85, 100 × 90 mm** — tylko *kandydaci*, żaden niezatwierdzony jako ostateczny. Jeśli trzeba, rozważyć inne szerokości/horyzontalne proporcje ≤100×100.
4. Nie wolno redukować marginesów RF, dostępu do złącz, prześwitu lub miejsca pod M3 tylko dla atrakcyjnego stosunku boków.
5. Ostateczne zatwierdzenie mechaniki i produkcji wymaga identyfikacji konkretnych wariantów MAIN/BT/DAC/RTC, podstawek, USB/jack, wysokości i obudowy. Do tego czasu wynik ma oznaczenie **PROVISIONAL**.

## Brama przed ustaleniem wymiaru

W osobnym, zatwierdzonym przez użytkownika etapie należy wykonać geometrię 2D/3D dla kilku prostokątnych wariantów, na rzeczywistych footprintach i pełnych referencyjnych obrysach, ze wszystkimi 77 komponentami na TOP oraz M3, RF keepout, jackiem/USB, złączami i rezerwą serwisową. Raport ma zawierać odległości, kolizje i decyzję: wykonalny / prowizorycznie wykonalny / niewykonalny. Wybrany wymiar dopiero po ocenie użytkownika.

**Bez nowego promptu Codexa, nowego layoutu, trasowania, Gerberów i zmiany projektu CAD do wyraźnej zgody użytkownika.**
