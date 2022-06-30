import board, busio
from DFPlayer import DFPlayer
from digitalio import DigitalInOut, Direction
from time import sleep
from random import randint

dfplayer_vol = 15
cd = 1
songs_count = {1 : 8}

uart = busio.UART(board.GP16, board.GP17, baudrate=9600)

dfplayer_busy = DigitalInOut(board.GP11)
dfplayer_busy.direction = Direction.INPUT

dfplayer = DFPlayer(uart, volume=dfplayer_vol)


while True:
    song = randint(1, songs_count[cd])
    dfplayer.play(cd, song)

    while not dfplayer_busy.value:
        pass
    
    sleep(2)
