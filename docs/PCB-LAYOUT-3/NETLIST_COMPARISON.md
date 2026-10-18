# Porównanie netlist PCB-LAYOUT-2 → PCB-LAYOUT-3

Niezależne eksporty prawdziwym KiCad CLI: BASELINE.net.xml i FINAL.net.xml. Odczyt PCB przez pcbnew po zapisie, niezależne porównanie wszystkich par(ref,pin)→net. Wynik: identyczne77 części,86 sieci,258 przypisań pin–sieć. Nie dodano/usunięto/zmieniono żadnego połączenia. Wszystkie wartości, numery padów, funkcje pinów, UUID footprintów i padów zachowane. Każdy pad ma taki sam lokalny środek, rozmiar i wiercenie jak w źródle i bibliotece; zmieniono tylko globalne pozycje i orientacje.

SchematA2, projekt.kicad_pro, biblioteka.kicad_sym, fp-lib-table, sym-lib-table, wszystkie bibliotekifootprintów, modele i licencje mają identyczne SHA-256 z wejściem. Nie zmieniono ERC/DRC/rules/ignored_checks. Netlisty i pełne mapy258 są w BASELINE_STATE.json / FINAL_STATE.json. Nie polegano na samej liczbie połączeń. Schematic-parity0.

J402.8=/5V_SYS; J401.8 pozostaje izolowanymNC3V3;U601.4NC. Jedyna techniczna normalizacja porównania: zapis izolowanegoTD0/TDO jako{slash}w plikuPCB. Nie powoduje to elektrycznego połączenia.

## Wszystkie79 wyprowadzeń głównych modułów

NumerM1=symbol pin=padPCB. Oryginalne numery z bibliotek internetowych są tylko informacją kontrolną, nie zostały użyte zamiast zatwierdzonych oznaczeń. MAIN J1.n→n, J3.n→45−n; J401.n→2n, J402.n→19+2n; DAC A.n→n,B.n→16−n.

| Ref | Pin/pad M1 | Oryginalny pad biblioteki | Funkcja | Sieć | Xglob | Yglob |
|---|---|---|---|---|---|---|
| U301 | A1 | 1 | SCK_A1 | /GND | 133.65 | 89.305 |
| U301 | A2 | 2 | BCK_A2 | /DAC_BCLK | 136.19 | 89.305 |
| U301 | A3 | 3 | DIN_A3 | /DAC_DOUT | 138.73 | 89.305 |
| U301 | A4 | 4 | LCK_A4 | /DAC_LRCK | 141.27 | 89.305 |
| U301 | A5 | 5 | GND_A5 | /GND | 143.81 | 89.305 |
| U301 | A6 | 6 | VIN_A6 | /5V_DAC | 146.35 | 89.305 |
| U301 | B1 | 15 | FLT_B1 | unconnected-(U301-FLT-PadB1) | 133.015 | 82.955 |
| U301 | B2 | 14 | DEMP_B2 | unconnected-(U301-DEMP-PadB2) | 133.015 | 80.415 |
| U301 | B3 | 13 | XSMT_B3 | /DAC_XSMT | 133.015 | 77.875 |
| U301 | B4 | 12 | FMT_B4 | unconnected-(U301-FMT-PadB4) | 133.015 | 75.335 |
| U301 | B5 | 11 | A3V3_B5 | unconnected-(U301-A3V3-PadB5) | 133.015 | 72.795 |
| U301 | B6 | 10 | AGND_B6 | /GND | 133.015 | 70.255 |
| U301 | B7 | 9 | ROUT_B7 | /AUDIO_R | 133.015 | 67.715 |
| U301 | B8 | 8 | AGND_B8 | /GND | 133.015 | 65.175 |
| U301 | B9 | 7 | LROUT_B9 | /AUDIO_L | 133.015 | 62.635 |
| J402 | 1 | 21 | TXD_1 | unconnected-(J402-TXD-Pad1) | 136.17 | 116.12 |
| J402 | 2 | 23 | RXD_2 | unconnected-(J402-RXD-Pad2) | 136.17 | 118.66 |
| J402 | 3 | 25 | IO22_3 | unconnected-(J402-IO22-Pad3) | 136.17 | 121.2 |
| J402 | 4 | 27 | IO21_4 | unconnected-(J402-IO21-Pad4) | 136.17 | 123.74 |
| J402 | 5 | 29 | IO17_5 | /BT_UART_RX | 136.17 | 126.28 |
| J402 | 6 | 31 | IO16_6 | /BT_UART_TX | 136.17 | 128.82 |
| J402 | 7 | 33 | GND_7 | /GND | 136.17 | 131.36 |
| J402 | 8 | 35 | VCC_8 | /5V_SYS | 136.17 | 133.9 |
| J402 | 9 | 37 | TD0/TDO_9 | unconnected-(J402-TD0{slash}TDO-Pad9) | 136.17 | 136.44 |
| J402 | 10 | 39 | SD0_10 | unconnected-(J402-SD0-Pad10) | 136.17 | 138.98 |
| J401 | 1 | 2 | RST_1 | /BT_RST_N | 113.31 | 116.12 |
| J401 | 2 | 4 | SVP_2 | unconnected-(J401-SVP-Pad2) | 113.31 | 118.66 |
| J401 | 3 | 6 | IO26_3 | /BT_I2S_DATA_OUT | 113.31 | 121.2 |
| J401 | 4 | 8 | IO18_4 | /BT_I2S_BCLK | 113.31 | 123.74 |
| J401 | 5 | 10 | IO19_5 | /BT_I2S_WS | 113.31 | 126.28 |
| J401 | 6 | 12 | IO23_6 | /BT_I2S_DATA_IN | 113.31 | 128.82 |
| J401 | 7 | 14 | IO5_7 | unconnected-(J401-IO5-Pad7) | 113.31 | 131.36 |
| J401 | 8 | 16 | 3.3V_8 | unconnected-(J401-3.3V-Pad8) | 113.31 | 133.9 |
| J401 | 9 | 18 | TCK_9 | unconnected-(J401-TCK-Pad9) | 113.31 | 136.44 |
| J401 | 10 | 20 | SD3_10 | unconnected-(J401-SD3-Pad10) | 113.31 | 138.98 |
| U201 | J1.1 | 1 | 3V3_J1.1 | /3V3_MAIN | 67.8 | 58.81 |
| U201 | J1.2 | 2 | 3V3_J1.2 | /3V3_MAIN | 67.8 | 61.35 |
| U201 | J1.3 | 3 | EN_J1.3 | unconnected-(U201-EN-PadJ1.3) | 67.8 | 63.89 |
| U201 | J1.4 | 4 | GPIO4_J1.4 | /DAC_BCLK_CPU | 67.8 | 66.43 |
| U201 | J1.5 | 5 | GPIO5_J1.5 | /DAC_LRCK_CPU | 67.8 | 68.97 |
| U201 | J1.6 | 6 | GPIO6_J1.6 | /DAC_DOUT_CPU | 67.8 | 71.51 |
| U201 | J1.7 | 7 | GPIO7_J1.7 | /DAC_XSMT_CPU | 67.8 | 74.05 |
| U201 | J1.8 | 8 | GPIO15_J1.8 | /BT_I2S_BCLK | 67.8 | 76.59 |
| U201 | J1.9 | 9 | GPIO16_J1.9 | /BT_I2S_WS | 67.8 | 79.13 |
| U201 | J1.10 | 10 | GPIO17_J1.10 | /BT_I2S_DATA_IN | 67.8 | 81.67 |
| U201 | J1.11 | 11 | GPIO18_J1.11 | /BT_I2S_DATA_OUT | 67.8 | 84.21 |
| U201 | J1.12 | 12 | GPIO8_J1.12 | /I2C_SDA | 67.8 | 86.75 |
| U201 | J1.13 | 13 | GPIO3_J1.13 | unconnected-(U201-GPIO3-PadJ1.13) | 67.8 | 89.29 |
| U201 | J1.14 | 14 | GPIO46_J1.14 | unconnected-(U201-GPIO46-PadJ1.14) | 67.8 | 91.83 |
| U201 | J1.15 | 15 | GPIO9_J1.15 | /I2C_SCL | 67.8 | 94.37 |
| U201 | J1.16 | 16 | GPIO10_J1.16 | /SPI_SCK | 67.8 | 96.91 |
| U201 | J1.17 | 17 | GPIO11_J1.17 | /SPI_MOSI | 67.8 | 99.45 |
| U201 | J1.18 | 18 | GPIO12_J1.18 | /SPI_CS | 67.8 | 101.99 |
| U201 | J1.19 | 19 | GPIO13_J1.19 | /SPI_DC | 67.8 | 104.53 |
| U201 | J1.20 | 20 | GPIO14_J1.20 | /AMP_MUTE | 67.79632 | 107.06728 |
| U201 | J1.21 | 21 | 5V_J1.21 | /5V_SYS | 67.79632 | 109.60728 |
| U201 | J1.22 | 22 | GND_J1.22 | /GND | 67.79632 | 112.14728 |
| U201 | J3.1 | 44 | GND_J3.1 | /GND | 93.2 | 58.81 |
| U201 | J3.2 | 43 | GPIO43_J3.2 | unconnected-(U201-GPIO43-PadJ3.2) | 93.2 | 61.35 |
| U201 | J3.3 | 42 | GPIO44_J3.3 | unconnected-(U201-GPIO44-PadJ3.3) | 93.2 | 63.89 |
| U201 | J3.4 | 41 | GPIO1_J3.4 | /BT_UART_TX | 93.2 | 66.43 |
| U201 | J3.5 | 40 | GPIO2_J3.5 | /BT_UART_RX | 93.2 | 68.97 |
| U201 | J3.6 | 39 | GPIO42_J3.6 | /BT_RESET | 93.2 | 71.51 |
| U201 | J3.7 | 38 | GPIO41_J3.7 | /INPUT_KEY | 93.2 | 74.05 |
| U201 | J3.8 | 37 | GPIO40_J3.8 | /INPUT_S2 | 93.2 | 76.59 |
| U201 | J3.9 | 36 | GPIO39_J3.9 | /INPUT_S1 | 93.2 | 79.13 |
| U201 | J3.10 | 35 | GPIO38_J3.10 | unconnected-(U201-GPIO38-PadJ3.10) | 93.2 | 81.67 |
| U201 | J3.11 | 34 | GPIO37_J3.11 | unconnected-(U201-GPIO37-PadJ3.11) | 93.2 | 84.21 |
| U201 | J3.12 | 33 | GPIO36_J3.12 | unconnected-(U201-GPIO36-PadJ3.12) | 93.2 | 86.75 |
| U201 | J3.13 | 32 | GPIO35_J3.13 | unconnected-(U201-GPIO35-PadJ3.13) | 93.2 | 89.29 |
| U201 | J3.14 | 31 | GPIO0_J3.14 | /MAIN_BOOT0 | 93.2 | 91.83 |
| U201 | J3.15 | 30 | GPIO45_J3.15 | unconnected-(U201-GPIO45-PadJ3.15) | 93.2 | 94.37 |
| U201 | J3.16 | 29 | GPIO48_J3.16 | unconnected-(U201-GPIO48-PadJ3.16) | 93.2 | 96.91 |
| U201 | J3.17 | 28 | GPIO47_J3.17 | /AMP_EN | 93.2 | 99.45 |
| U201 | J3.18 | 27 | GPIO21_J3.18 | /DISPLAY_BL | 93.2 | 101.99 |
| U201 | J3.19 | 26 | GPIO20_J3.19 | unconnected-(U201-GPIO20-PadJ3.19) | 93.2 | 104.53 |
| U201 | J3.20 | 25 | GPIO19_J3.20 | unconnected-(U201-GPIO19-PadJ3.20) | 93.2 | 107.07 |
| U201 | J3.21 | 24 | GND_J3.21 | /GND | 93.2 | 109.61 |
| U201 | J3.22 | 23 | GND_J3.22 | /GND | 93.2 | 112.15 |
