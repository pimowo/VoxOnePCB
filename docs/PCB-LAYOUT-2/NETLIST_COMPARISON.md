# Porównanie netlist main → pcb-layout-2

| Parametr | main baseline | PCB-LAYOUT-2 |
|---|---:|---:|
| Elementy elektryczne | 77 | 77 |
| Footprinty z otworami M3 | 81 | 81 |
| Sieci z samotnymi NC | 86 | 86 |
| Przypisania ref/pin/net | 258 | 258 |
| Rzeczywiste zmiany połączeń | - | 0 |
| Wartości / GPIO / numery pinów / UUID footprintów | zachowane | zachowane |

Wyeksportowano niezależnie BASELINE.net.xml i FINAL.net.xml przez rzeczywisty KiCad CLI. Porównano każdą z258 par oznaczenie/pin z nazwą sieci oraz pady odczytane natywnie z PCB. Identyczność pełnych map, nie tylko liczebności. Schemat, biblioteka symboli, projekt, fp-lib-table/sym-lib-table oraz wszystkie lokalne footprinty i modele mają identyczne SHA-256 jak przed etapem. Geometryczne środki, rozmiary padów i wiercenia każdego footprintu PCB porównano z lokalną biblioteką: identyczne, z uwzględnieniem obrotu/strony montażu. Nie dodano ani nie usunięto żadnego elementu.

Techniczny zapis nazwy samotnego NC J402.9 `TD0/TDO` w XML i `TD0{slash}TDO` w natywnym PCB znormalizowano wyłącznie przy porównaniu. Żadne piny nie zostały z tego powodu połączone. Końcowy schematic-parity: 0 rozbieżności. J402.8 pozostaje /5V_SYS, J401.8 pozostaje niepodłączonym3V3 Wemosa, U601.4 NC.

## Pełna mapa79 wyprowadzeń modułów

Lokalne numery padów są dokładnymi numerami pinów symbolu M1. Kolumna źródłowa to zatwierdzone odwzorowanie oryginalnej numeracji globalnej bibliotek, nie obudowy scalaka. MAIN J1.n→n, J3.n→45−n; J401→2,4,…20; J402→21,23,…39; DAC A1…6→1…6, B1…9→15…7. Zweryfikowano fizyczne współrzędne lokalnych padów i wszystkie funkcje/sieci. Konkretne klony nadal wymagają pomiarów P1.

| Ref | Pin symbolu = pad M1 | Numer źródłowy | Funkcja | Sieć | XY lokalne mm |
|---|---|---|---|---|---|
| U301 | A1 | 1 | SCK_A1 | /GND | [-14.305, -6.35] |
| U301 | A2 | 2 | BCK_A2 | /DAC_BCLK | [-14.305, -3.81] |
| U301 | A3 | 3 | DIN_A3 | /DAC_DOUT | [-14.305, -1.27] |
| U301 | A4 | 4 | LCK_A4 | /DAC_LRCK | [-14.305, 1.27] |
| U301 | A5 | 5 | GND_A5 | /GND | [-14.305, 3.81] |
| U301 | A6 | 6 | VIN_A6 | /5V_DAC | [-14.305, 6.35] |
| U301 | B1 | 15 | FLT_B1 | unconnected-(U301-FLT-PadB1) | [-7.955, -6.985] |
| U301 | B2 | 14 | DEMP_B2 | unconnected-(U301-DEMP-PadB2) | [-5.415, -6.985] |
| U301 | B3 | 13 | XSMT_B3 | /DAC_XSMT | [-2.875, -6.985] |
| U301 | B4 | 12 | FMT_B4 | unconnected-(U301-FMT-PadB4) | [-0.335, -6.985] |
| U301 | B5 | 11 | A3V3_B5 | unconnected-(U301-A3V3-PadB5) | [2.205, -6.985] |
| U301 | B6 | 10 | AGND_B6 | /GND | [4.745, -6.985] |
| U301 | B7 | 9 | ROUT_B7 | /AUDIO_R | [7.285, -6.985] |
| U301 | B8 | 8 | AGND_B8 | /GND | [9.825, -6.985] |
| U301 | B9 | 7 | LROUT_B9 | /AUDIO_L | [12.365, -6.985] |
| J402 | 1 | 21 | TXD_1 | unconnected-(J402-TXD-Pad1) | [11.43, -11.43] |
| J402 | 2 | 23 | RXD_2 | unconnected-(J402-RXD-Pad2) | [11.43, -8.89] |
| J402 | 3 | 25 | IO22_3 | unconnected-(J402-IO22-Pad3) | [11.43, -6.35] |
| J402 | 4 | 27 | IO21_4 | unconnected-(J402-IO21-Pad4) | [11.43, -3.81] |
| J402 | 5 | 29 | IO17_5 | /BT_UART_RX | [11.43, -1.27] |
| J402 | 6 | 31 | IO16_6 | /BT_UART_TX | [11.43, 1.27] |
| J402 | 7 | 33 | GND_7 | /GND | [11.43, 3.81] |
| J402 | 8 | 35 | VCC_8 | /5V_SYS | [11.43, 6.35] |
| J402 | 9 | 37 | TD0/TDO_9 | unconnected-(J402-TD0{slash}TDO-Pad9) | [11.43, 8.89] |
| J402 | 10 | 39 | SD0_10 | unconnected-(J402-SD0-Pad10) | [11.43, 11.43] |
| J401 | 1 | 2 | RST_1 | /BT_RST_N | [-11.43, -11.43] |
| J401 | 2 | 4 | SVP_2 | unconnected-(J401-SVP-Pad2) | [-11.43, -8.89] |
| J401 | 3 | 6 | IO26_3 | /BT_I2S_DATA_OUT | [-11.43, -6.35] |
| J401 | 4 | 8 | IO18_4 | /BT_I2S_BCLK | [-11.43, -3.81] |
| J401 | 5 | 10 | IO19_5 | /BT_I2S_WS | [-11.43, -1.27] |
| J401 | 6 | 12 | IO23_6 | /BT_I2S_DATA_IN | [-11.43, 1.27] |
| J401 | 7 | 14 | IO5_7 | unconnected-(J401-IO5-Pad7) | [-11.43, 3.81] |
| J401 | 8 | 16 | 3.3V_8 | unconnected-(J401-3.3V-Pad8) | [-11.43, 6.35] |
| J401 | 9 | 18 | TCK_9 | unconnected-(J401-TCK-Pad9) | [-11.43, 8.89] |
| J401 | 10 | 20 | SD3_10 | unconnected-(J401-SD3-Pad10) | [-11.43, 11.43] |
| U201 | J1.1 | 1 | 3V3_J1.1 | /3V3_MAIN | [1.3, 1.91] |
| U201 | J1.2 | 2 | 3V3_J1.2 | /3V3_MAIN | [1.3, 4.45] |
| U201 | J1.3 | 3 | EN_J1.3 | unconnected-(U201-EN-PadJ1.3) | [1.3, 6.99] |
| U201 | J1.4 | 4 | GPIO4_J1.4 | /DAC_BCLK_CPU | [1.3, 9.53] |
| U201 | J1.5 | 5 | GPIO5_J1.5 | /DAC_LRCK_CPU | [1.3, 12.07] |
| U201 | J1.6 | 6 | GPIO6_J1.6 | /DAC_DOUT_CPU | [1.3, 14.61] |
| U201 | J1.7 | 7 | GPIO7_J1.7 | /DAC_XSMT_CPU | [1.3, 17.15] |
| U201 | J1.8 | 8 | GPIO15_J1.8 | /BT_I2S_BCLK | [1.3, 19.69] |
| U201 | J1.9 | 9 | GPIO16_J1.9 | /BT_I2S_WS | [1.3, 22.23] |
| U201 | J1.10 | 10 | GPIO17_J1.10 | /BT_I2S_DATA_IN | [1.3, 24.77] |
| U201 | J1.11 | 11 | GPIO18_J1.11 | /BT_I2S_DATA_OUT | [1.3, 27.31] |
| U201 | J1.12 | 12 | GPIO8_J1.12 | /I2C_SDA | [1.3, 29.85] |
| U201 | J1.13 | 13 | GPIO3_J1.13 | unconnected-(U201-GPIO3-PadJ1.13) | [1.3, 32.39] |
| U201 | J1.14 | 14 | GPIO46_J1.14 | unconnected-(U201-GPIO46-PadJ1.14) | [1.3, 34.93] |
| U201 | J1.15 | 15 | GPIO9_J1.15 | /I2C_SCL | [1.3, 37.47] |
| U201 | J1.16 | 16 | GPIO10_J1.16 | /SPI_SCK | [1.3, 40.01] |
| U201 | J1.17 | 17 | GPIO11_J1.17 | /SPI_MOSI | [1.3, 42.55] |
| U201 | J1.18 | 18 | GPIO12_J1.18 | /SPI_CS | [1.3, 45.09] |
| U201 | J1.19 | 19 | GPIO13_J1.19 | /SPI_DC | [1.3, 47.63] |
| U201 | J1.20 | 20 | GPIO14_J1.20 | /AMP_MUTE | [1.29632, 50.16728] |
| U201 | J1.21 | 21 | 5V_J1.21 | /5V_SYS | [1.29632, 52.70728] |
| U201 | J1.22 | 22 | GND_J1.22 | /GND | [1.29632, 55.24728] |
| U201 | J3.1 | 44 | GND_J3.1 | /GND | [26.7, 1.91] |
| U201 | J3.2 | 43 | GPIO43_J3.2 | unconnected-(U201-GPIO43-PadJ3.2) | [26.7, 4.45] |
| U201 | J3.3 | 42 | GPIO44_J3.3 | unconnected-(U201-GPIO44-PadJ3.3) | [26.7, 6.99] |
| U201 | J3.4 | 41 | GPIO1_J3.4 | /BT_UART_TX | [26.7, 9.53] |
| U201 | J3.5 | 40 | GPIO2_J3.5 | /BT_UART_RX | [26.7, 12.07] |
| U201 | J3.6 | 39 | GPIO42_J3.6 | /BT_RESET | [26.7, 14.61] |
| U201 | J3.7 | 38 | GPIO41_J3.7 | /INPUT_KEY | [26.7, 17.15] |
| U201 | J3.8 | 37 | GPIO40_J3.8 | /INPUT_S2 | [26.7, 19.69] |
| U201 | J3.9 | 36 | GPIO39_J3.9 | /INPUT_S1 | [26.7, 22.23] |
| U201 | J3.10 | 35 | GPIO38_J3.10 | unconnected-(U201-GPIO38-PadJ3.10) | [26.7, 24.77] |
| U201 | J3.11 | 34 | GPIO37_J3.11 | unconnected-(U201-GPIO37-PadJ3.11) | [26.7, 27.31] |
| U201 | J3.12 | 33 | GPIO36_J3.12 | unconnected-(U201-GPIO36-PadJ3.12) | [26.7, 29.85] |
| U201 | J3.13 | 32 | GPIO35_J3.13 | unconnected-(U201-GPIO35-PadJ3.13) | [26.7, 32.39] |
| U201 | J3.14 | 31 | GPIO0_J3.14 | /MAIN_BOOT0 | [26.7, 34.93] |
| U201 | J3.15 | 30 | GPIO45_J3.15 | unconnected-(U201-GPIO45-PadJ3.15) | [26.7, 37.47] |
| U201 | J3.16 | 29 | GPIO48_J3.16 | unconnected-(U201-GPIO48-PadJ3.16) | [26.7, 40.01] |
| U201 | J3.17 | 28 | GPIO47_J3.17 | /AMP_EN | [26.7, 42.55] |
| U201 | J3.18 | 27 | GPIO21_J3.18 | /DISPLAY_BL | [26.7, 45.09] |
| U201 | J3.19 | 26 | GPIO20_J3.19 | unconnected-(U201-GPIO20-PadJ3.19) | [26.7, 47.63] |
| U201 | J3.20 | 25 | GPIO19_J3.20 | unconnected-(U201-GPIO19-PadJ3.20) | [26.7, 50.17] |
| U201 | J3.21 | 24 | GND_J3.21 | /GND | [26.7, 52.71] |
| U201 | J3.22 | 23 | GND_J3.22 | /GND | [26.7, 55.25] |

Dane maszynowe wszystkich258 przypisań: BASELINE_STATE.json i FINAL_STATE.json, geometria79: MECHANICAL_CHECK.json. ERC i DRC nie wykluczają żadnych kontroli.
