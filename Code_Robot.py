import math
from yolobit import *
import machine
from i2c_motors_driver import DCMotor
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
import music
import time
from mqtt import *
from mecanum import *

# Mô tả hàm này...
def PID_Controller():
  global PID_Value, RIGHT, Flag, KeyReg2, P, Position, LEFT, KeyReg0, KeyReg1, I, Previous_Position, BACK, AI_Check, D, K_p, STOP, th_C3_B4ng_tin, K_i, FOWARD, K_d, NO_SIGN, TimeOut
  Position_Robot()
  P = Position
  I = I + Position
  D = Position - Previous_Position
  PID_Value = P * K_p + I * K_i
  PID_Value = (PID_Value if isinstance(PID_Value, (int, float)) else 0) + D * K_d
  PID_Value = round(PID_Value)
  Previous_Position = Position

driver = DCMotor(machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000))

# Mô tả hàm này...
def Stop():
  global PID_Value, RIGHT, Flag, KeyReg2, P, Position, LEFT, KeyReg0, KeyReg1, I, Previous_Position, BACK, AI_Check, D, K_p, STOP, th_C3_B4ng_tin, K_i, FOWARD, K_d, NO_SIGN, TimeOut
  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)
  display.show(Image.YES)

# Mô tả hàm này...
def Initialize_Values():
  global PID_Value, RIGHT, Flag, KeyReg2, P, Position, LEFT, KeyReg0, KeyReg1, I, Previous_Position, BACK, AI_Check, D, K_p, STOP, th_C3_B4ng_tin, K_i, FOWARD, K_d, NO_SIGN, TimeOut
  PID_Value = 0
  Position = 0
  Previous_Position = 0
  P = 0
  I = 0
  D = 0

# Mô tả hàm này...
def Forward():
  global PID_Value, RIGHT, Flag, KeyReg2, P, Position, LEFT, KeyReg0, KeyReg1, I, Previous_Position, BACK, AI_Check, D, K_p, STOP, th_C3_B4ng_tin, K_i, FOWARD, K_d, NO_SIGN, TimeOut
  Initialize_Values()
  while not ((mecanum.read_line_sensors() == (1, 1, 1, 1)) or (mecanum.read_line_sensors() == (0, 1, 1, 1)) or (mecanum.read_line_sensors() == (1, 1, 1, 0))):
    Line_Forward()
  driver.setSpeed(0,20)
  driver.setSpeed(1,20)
  driver.setSpeed(2,20)
  driver.setSpeed(3,20)
  time.sleep_ms(50)
  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)

# Mô tả hàm này...
def Connect_Wifi():
  global PID_Value, RIGHT, Flag, KeyReg2, P, Position, LEFT, KeyReg0, KeyReg1, I, Previous_Position, BACK, AI_Check, D, K_p, STOP, th_C3_B4ng_tin, K_i, FOWARD, K_d, NO_SIGN, TimeOut
  mqtt.connect_wifi('Thien1506', '150620032003')
  mqtt.connect_broker(server='io.adafruit.com', port=1883, username='QuangThien', password='aio_pqUA10vengG3dxJkWFbaAqSK4WEu')

# Mô tả hàm này...
def Define_AI_Values():
  global PID_Value, RIGHT, Flag, KeyReg2, P, Position, LEFT, KeyReg0, KeyReg1, I, Previous_Position, BACK, AI_Check, D, K_p, STOP, th_C3_B4ng_tin, K_i, FOWARD, K_d, NO_SIGN, TimeOut
  RIGHT = 0
  LEFT = 1
  BACK = 2
  STOP = 3
  FOWARD = 4
  NO_SIGN = 5
  KeyReg0 = NO_SIGN
  KeyReg1 = NO_SIGN
  KeyReg2 = NO_SIGN
  TimeOut = 1
  Flag = 0
  AI_Check = ''

# Mô tả hàm này...
def Controller():
  global PID_Value, RIGHT, Flag, KeyReg2, P, Position, LEFT, KeyReg0, KeyReg1, I, Previous_Position, BACK, AI_Check, D, K_p, STOP, th_C3_B4ng_tin, K_i, FOWARD, K_d, NO_SIGN, TimeOut
  Flag = 1
  music.play(music.POWER_DOWN, wait=True)
  if KeyReg0 == 0:
    display.show(Image.YES)
    Right()
    Forward()
  elif KeyReg0 == 1:
    display.show(Image.YES)
    Left()
    Forward()
  elif KeyReg0 == 2:
    display.show(Image.YES)
    Left()
    Forward()
    Left()
    Forward()
  elif KeyReg0 == 3:
    Stop()
  elif KeyReg0 == 4:
    display.show(Image.YES)
    Forward()
  else:
    display.show(Image.NO)
  Flag = 0

# Mô tả hàm này...
def Left():
  global PID_Value, RIGHT, Flag, KeyReg2, P, Position, LEFT, KeyReg0, KeyReg1, I, Previous_Position, BACK, AI_Check, D, K_p, STOP, th_C3_B4ng_tin, K_i, FOWARD, K_d, NO_SIGN, TimeOut
  Initialize_Values()
  driver.setSpeed(0,30)
  driver.setSpeed(1,(-30))
  driver.setSpeed(2,(-30))
  driver.setSpeed(3,30)
  time.sleep_ms(200)
  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)
  while not ((mecanum.read_line_sensors(1)) or (mecanum.read_line_sensors(1)) and (mecanum.read_line_sensors(2))):
    driver.setSpeed(0,20)
    driver.setSpeed(1,(-20))
    driver.setSpeed(2,(-20))
    driver.setSpeed(3,20)
  while not ((mecanum.read_line_sensors(2)) and (mecanum.read_line_sensors(3)) or (mecanum.read_line_sensors(3))):
    Line_Left_and_Right()
  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)

# Mô tả hàm này...
def Position_Robot():
  global PID_Value, RIGHT, Flag, KeyReg2, P, Position, LEFT, KeyReg0, KeyReg1, I, Previous_Position, BACK, AI_Check, D, K_p, STOP, th_C3_B4ng_tin, K_i, FOWARD, K_d, NO_SIGN, TimeOut
  if mecanum.read_line_sensors() == (0, 0, 0, 0):
    Position = -3
  elif mecanum.read_line_sensors() == (0, 0, 0, 1):
    Position = -2
  elif (mecanum.read_line_sensors() == (0, 0, 1, 1)) or (mecanum.read_line_sensors() == (0, 0, 1, 0)):
    Position = -1
  elif mecanum.read_line_sensors() == (1, 0, 0, 0):
    Position = 2
  elif (mecanum.read_line_sensors() == (1, 1, 0, 0)) or (mecanum.read_line_sensors() == (0, 1, 0, 0)):
    Position = 1
  else:
    Position = 0

# Mô tả hàm này...
def Check_AI_Detection():
  global PID_Value, RIGHT, Flag, KeyReg2, P, Position, LEFT, KeyReg0, KeyReg1, I, Previous_Position, BACK, AI_Check, D, K_p, STOP, th_C3_B4ng_tin, K_i, FOWARD, K_d, NO_SIGN, TimeOut
  if AI_Check == '0':
    KeyReg0 = 0
  elif AI_Check == '1':
    KeyReg0 = 1
  elif AI_Check == '2':
    KeyReg0 = 2
  elif AI_Check == '3':
    KeyReg0 = 3
  elif AI_Check == '4':
    KeyReg0 = 4
  else:
    KeyReg0 = 5

# Mô tả hàm này...
def Right():
  global PID_Value, RIGHT, Flag, KeyReg2, P, Position, LEFT, KeyReg0, KeyReg1, I, Previous_Position, BACK, AI_Check, D, K_p, STOP, th_C3_B4ng_tin, K_i, FOWARD, K_d, NO_SIGN, TimeOut
  Initialize_Values()
  driver.setSpeed(0,(-30))
  driver.setSpeed(1,30)
  driver.setSpeed(2,30)
  driver.setSpeed(3,(-30))
  time.sleep_ms(200)
  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)
  while not ((mecanum.read_line_sensors(3)) or (mecanum.read_line_sensors(3)) and (mecanum.read_line_sensors(4))):
    driver.setSpeed(0,(-20))
    driver.setSpeed(1,20)
    driver.setSpeed(2,20)
    driver.setSpeed(3,(-20))
  while not ((mecanum.read_line_sensors(3)) and (mecanum.read_line_sensors(2)) or (mecanum.read_line_sensors(2))):
    Line_Left_and_Right()
  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)

def on_mqtt_message_receive_callback__ai_(th_C3_B4ng_tin):
  global PID_Value, RIGHT, Flag, KeyReg2, P, Position, LEFT, KeyReg0, KeyReg1, I, Previous_Position, BACK, AI_Check, D, K_p, STOP, K_i, FOWARD, K_d, NO_SIGN, TimeOut
  music.play(music.POWER_DOWN, wait=True)
  AI_Check = th_C3_B4ng_tin
  Check_AI_Detection()

# Mô tả hàm này...
def AI_Detection():
  global PID_Value, RIGHT, Flag, KeyReg2, P, Position, LEFT, KeyReg0, KeyReg1, I, Previous_Position, BACK, AI_Check, D, K_p, STOP, th_C3_B4ng_tin, K_i, FOWARD, K_d, NO_SIGN, TimeOut
  KeyReg2 = KeyReg1
  KeyReg1 = KeyReg0
  KeyReg0 = KeyReg0
  mqtt.on_receive_message('ai', on_mqtt_message_receive_callback__ai_)
  if Flag == 0:
    if KeyReg1 == KeyReg0 and KeyReg1 == KeyReg2:
      TimeOut = (TimeOut if isinstance(TimeOut, (int, float)) else 0) + -1
      if TimeOut == 0:
        TimeOut = 5
        Controller()
    else:
      TimeOut = 5
      Controller()

# Mô tả hàm này...
def Line_Forward():
  global PID_Value, RIGHT, Flag, KeyReg2, P, Position, LEFT, KeyReg0, KeyReg1, I, Previous_Position, BACK, AI_Check, D, K_p, STOP, th_C3_B4ng_tin, K_i, FOWARD, K_d, NO_SIGN, TimeOut
  PID_Controller()
  if Position == 2:
    driver.setSpeed(0,(40 + PID_Value))
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,(40 + PID_Value))
  elif Position == 1:
    driver.setSpeed(0,(30 + PID_Value))
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,(30 + PID_Value))
  elif Position == 0:
    driver.setSpeed(0,20)
    driver.setSpeed(1,20)
    driver.setSpeed(2,20)
    driver.setSpeed(3,20)
  elif Position == -1:
    driver.setSpeed(0,0)
    driver.setSpeed(1,(30 - PID_Value))
    driver.setSpeed(2,(30 - PID_Value))
    driver.setSpeed(3,0)
  elif Position == -2:
    driver.setSpeed(0,0)
    driver.setSpeed(1,(40 - PID_Value))
    driver.setSpeed(2,(40 - PID_Value))
    driver.setSpeed(3,0)
  else:
    driver.setSpeed(0,(-20))
    driver.setSpeed(1,(-20))
    driver.setSpeed(2,(-20))
    driver.setSpeed(3,(-20))

# Mô tả hàm này...
def Line_Left_and_Right():
  global PID_Value, RIGHT, Flag, KeyReg2, P, Position, LEFT, KeyReg0, KeyReg1, I, Previous_Position, BACK, AI_Check, D, K_p, STOP, th_C3_B4ng_tin, K_i, FOWARD, K_d, NO_SIGN, TimeOut
  PID_Controller()
  if Position == 2 or Position == 1:
    driver.setSpeed(0,(30 + PID_Value))
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,(30 + PID_Value))
  elif Position == -2 or Position == -1:
    driver.setSpeed(0,0)
    driver.setSpeed(1,(30 - PID_Value))
    driver.setSpeed(2,(30 - PID_Value))
    driver.setSpeed(3,0)

if True:
  display.show(Image.HAPPY)
  music.play(music.POWER_UP, wait=False)
  time.sleep_ms(1000)
  K_p = 0.6
  K_i = 0.2
  K_d = 0.2
  Connect_Wifi()
  Initialize_Values()
  Define_AI_Values()
  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)

while True:
  mqtt.check_message()
  AI_Detection()
