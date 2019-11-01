import ev3dev.ev3 as ev3
from time import perf_counter
import time

backWheel = ev3.LargeMotor('outA')
frontWheel = ev3.LargeMotor('outB')

def runOneCycle(new_pos):
    backWheel.run_to_abs_pos(position_sp=new_pos, speed_sp = 200)
    time.sleep(8)
    backWheel.run_to_abs_pos(position_sp=new_pos, speed_sp = 50)
    time.sleep(3)
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
    time.sleep(15)
    print("Calibration done - starting")
    return

def backMotor():
    position = 0
    for i in range(3):
        print("Running One Cycle")
        position = position - 1500
        runOneCycle(position)
        print("Finished the Cycle")
    return

calibrateMachine()
