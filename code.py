import board, busio
from digitalio import DigitalInOut, Direction, Pull
import mfrc522
from DFPlayer import DFPlayer


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

songs_uid = {"0x79aae7a3" : 1, "0x397358c1" : 2, "0x69bb5ec2" : 3}

while True:
    if dfplayer_busy.value:
        (stat, tag_type) = rfid.request(rfid.REQIDL)
        
        if stat == rfid.OK:
            (stat, raw_uid) = rfid.anticoll()
            if stat == rfid.OK:
                uid = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                print("uid: ", uid)
                if uid in songs_uid.keys():
                    dfplayer.play(cd, songs_uid[uid])
                    print("Playing song ", songs_uid[uid])
                print("")
    elif not btn.value:
        print("Button pressed")
        dfplayer.stop()
