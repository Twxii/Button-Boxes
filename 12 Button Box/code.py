import board
import digitalio
import usb_hid
import time

from btnBoxTwelve import BtnBox

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

btnBox = BtnBox()

btnBoxBtns = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

col_pins = [board.GP19, board.GP18, board.GP17, board.GP16]
row_pins = [board.GP8, board.GP7, board.GP21]

colOne = digitalio.DigitalInOut(col_pins[0])
colOne.direction = digitalio.Direction.OUTPUT

colTwo = digitalio.DigitalInOut(col_pins[1])
colTwo.direction = digitalio.Direction.OUTPUT

colThree = digitalio.DigitalInOut(col_pins[2])
colThree.direction = digitalio.Direction.OUTPUT

colFour = digitalio.DigitalInOut(col_pins[3])
colFour.direction = digitalio.Direction.OUTPUT

rowOne = digitalio.DigitalInOut(row_pins[0])
rowOne.direction = digitalio.Direction.INPUT
rowOne.pull = digitalio.Pull.DOWN

rowTwo = digitalio.DigitalInOut(row_pins[1])
rowTwo.direction = digitalio.Direction.INPUT
rowTwo.pull = digitalio.Pull.DOWN

rowThree = digitalio.DigitalInOut(row_pins[2])
rowThree.direction = digitalio.Direction.INPUT
rowThree.pull = digitalio.Pull.DOWN

btn_cols = [colOne, colTwo, colThree, colFour]
btn_rows = [rowOne, rowTwo, rowThree]

def scanBtns():
    for col in range(4):
        for row in range(3):
            btn_cols[col].value = True
        
            if btn_rows[row].value:
                btnBox.press_buttons(btnBoxBtns[row][col])
                #time.sleep(0.1)
            else:
                btnBox.release_buttons(btnBoxBtns[row][col])
                
        btn_cols[col].value = False

while True:
    led.value = True
    scanBtns()
