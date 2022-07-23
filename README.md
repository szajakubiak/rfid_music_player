# rfid_music_player
 
Music player where song is selected using RFID tag

## Hardware

* [Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
* [DFPlayer Mini](https://wiki.dfrobot.com/DFPlayer_Mini_SKU_DFR0299)
* [MFRC522 RFID reader](https://randomnerdtutorials.com/security-access-using-mfrc522-rfid-reader-with-arduino/)
* [Audio amplifier 2 x 3W PAM8403 with potentiometer](https://electropeak.com/3w-pam8403-fv-stereo-amplifier-module)
* 1 or 2 speakers with power up to 3 W

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
| SDA / CS | GP13              |
| SCK      | GP14              |
| MISO     | GP12              |
| MOSI     | GP15              |
| RST      | GP10              |

## Issues

There is a lot of poor quality or fake MFRC522 modules. Such modules may not work at all or work in unstable manner. To verify if module is good it's adviced to use [CheckFirmware](https://github.com/OSSLibraries/Arduino_MFRC522v2/tree/master/examples/CheckFirmware) sample sketch from [Arduino_MFRC522v2](https://github.com/OSSLibraries/Arduino_MFRC522v2) library. In the time of writing Raspberry Pi Pico is not supported, therefore one of the supported microcontroller boards needs to be used to do the check. It was found that MFRC522 module which passed the test was running more stable than identical one, which failed the test.

## Links

[RC522 RFID Reader Module with Raspberry Pi Pico](https://microcontrollerslab.com/raspberry-pi-pico-rfid-rc522-micropython/)

## TODO

* Add connection table for sound output from DFPlayer Mini