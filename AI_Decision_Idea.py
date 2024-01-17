from AI_Detection_Traffic_Signs import *

RIGHT = 0
LEFT = 1
BACK = 2
STOP = 3
FORWARD = 4
NO_SIGN = 5

KeyReg0 = NO_SIGN
KeyReg1 = NO_SIGN
KeyReg2 = NO_SIGN

TimeOut = 5
Flag = 0

def move(KeyReg):
    global KeyReg0, KeyReg1, KeyReg2, Flag
    print("State:", KeyReg)
    Flag = 0
def getkey_input(new_state):
    global KeyReg0, KeyReg1, KeyReg2, TimeOut, Flag

    KeyReg2 = KeyReg1
    KeyReg1 = KeyReg0
    KeyReg0 = new_state

    if Flag == 0:
        if KeyReg0 == KeyReg1 == KeyReg2:
            TimeOut -= 1
            if TimeOut == 0:
                TimeOut = 5
                Flag = 1
                move(KeyReg0)
        else:
            TimeOut = 5
            KeyReg1 = KeyReg0
            KeyReg2 = KeyReg0
            Flag = 1
            move(KeyReg0)
