# rfid_music_player
 
Music player where song is selected using RFID tag

## Hardware

* [Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
* [DFPlayer Mini](https://wiki.dfrobot.com/DFPlayer_Mini_SKU_DFR0299)
* [MFRC522 RFID reader](https://randomnerdtutorials.com/security-access-using-mfrc522-rfid-reader-with-arduino/)

## Dependencies

* [CircuitPython for Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/)
* [DFPlayer Mini library for CircuitPython](https://github.com/bablokb/circuitpython-dfplayer)
* [MFRC522 library for CircuitPython](https://github.com/domdfcoding/circuitpython-mfrc522)

## Connections

| DFPlayer Mini | Raspberry Pi Pico | Comments              |
| :-----------: | :---------------: | :-------------------: |
| VCC           | VSYS              |                       |
| GND           | GND               | both pins of DFPlayer |
| RX            | GP16              | through 1k resistor   |
| TX            | GP17              | through 1k resistor   |
| BUSY          | GP11              |                       |

| MFRC522  | Raspberry Pi Pico |
| :------: | :---------------: |
| 3.3V     | 3V3               |
| GND      | GND               |
| SDA / CS |                   |
| SCK      |                   |
| MISO     |                   |
| MOSI     |                   |
| RST      |                   |