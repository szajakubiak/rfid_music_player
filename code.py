import board, busio
from digitalio import DigitalInOut, Direction, Pull
import mfrc522
from DFPlayer import DFPlayer
from time import sleep
from random import randint


btn = DigitalInOut(board.GP3)
btn.direction = Direction.INPUT
btn.pull = Pull.UP


rfid = mfrc522.MFRC522(board.GP14, board.GP15, board.GP12, board.GP10, board.GP13)
rfid.set_antenna_gain(0x07 << 4)


dfplayer_vol = 15
cd = 1
songs_count = {1 : 8}

uart = busio.UART(board.GP16, board.GP17, baudrate=9600)

dfplayer_busy = DigitalInOut(board.GP11)
dfplayer_busy.direction = Direction.INPUT

dfplayer = DFPlayer(uart, volume=dfplayer_vol)


while True:
    (stat, tag_type) = rfid.request(rfid.REQIDL)
    
    if stat == rfid.OK:
        (stat, raw_uid) = rfid.anticoll()
        if stat == rfid.OK:
            uid = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print("uid: ", uid)
            print("")
    elif not btn.value:
        print("Button pressed")

    #song = randint(1, songs_count[cd])
    #dfplayer.play(cd, song)

    #while not dfplayer_busy.value:
    #    pass
    
    #sleep(2)
