import ev3dev.ev3 as ev3
from time import perf_counter
import time
import socket

backWheel = ev3.LargeMotor('outA')
frontWheel = ev3.LargeMotor('outB')

def runOneCycle(new_pos):
    backWheel.run_to_abs_pos(position_sp=new_pos, speed_sp = 200)
    time.sleep(8)
    backWheel.run_to_abs_pos(position_sp=new_pos, speed_sp = 50)
    time.sleep(3)
    return


def runFrontCycle(new_pos):
    frontWheel.run_to_abs_pos(position_sp=new_pos, speed_sp = 50)
    time.sleep(2)
    return

def calibrateMachine():
    position = 0
    print("Starting Calibration...")
    backWheel.run_to_abs_pos(position_sp=position, speed_sp = 1000)
    frontWheel.run_to_abs_pos(position_sp=position, speed_sp = 1000)
    time.sleep(30)
    backWheel.run_to_abs_pos(position_sp=position, speed_sp = 50)
    frontWheel.run_to_abs_pos(position_sp=position, speed_sp = 50)
    time.sleep(30)
    # if threading for calibration would be necessary, move them apart and do this (eventually use ray)
    #Thread(target = calibrateBackMotor(0)).start()
    #Thread(target = calibrateFrontMotor(0)).start()
    print("Calibrated")
    print("Place cards within 20 seconds...")
    time.sleep(10)
    print("Calibration done - starting")
    return

def backMotor(position):
    print("Running One Cycle")
    position = position - 1000
    runOneCycle(position)
    print("Finished the Cycle")
    return 

def frontMotor(position):
    #got a lowtime to run as it must ask the camera if there is a card or not
    print("Running One Cycle")
    print(position)
    #position = position - 60
    runFrontCycle(position)
    print("Finished the Cycle")
    return position

# Sets the READY message, which means that the ev3 is ready to communicate with the PI
msgFromClient = "READY"

# Settings Up
bytesToSend = str.encode(msgFromClient)
bufferSize = 1024
serverAddressPort = ("172.28.210.59", 22222) # IP and Port of the Raspberry PI

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

#calibrateMachine()
#position = 0
#backMotor(position)
#position = position - 1000
#frontMotor(position)
#position = position - 60
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Upcode from the Rasberry Pi {}".format(msgFromServer[0])
print(msg)
time.sleep(15)
if ("card" in msg):
    print("Pushed Piston")
if ("not_card" in msg):
    #frontMotor(position)
    #position = position - 60
    print("NO CARD FOUND")
