from motors import Motors
from time import time, sleep

# Create an instance of the Motors class used in SDP
def move_forward():
    speed = -25
    run_time = 1
    mc.move_motor(motor_id,speed)
    start_time = time()
    try:
        while time()<start_time+run_time:
		sleep(0.2)
    except:
	  mc.stop_motors()
def move_backward():
    speed = 30
    run_time = 1.4
    mc.move_motor(motor_id,speed)
    start_time = time()
    try:
        while time()<start_time+run_time:
                sleep(0.2)
    except:
          mc.stop_motors()


mc = Motors()

motor_id = 0        #         # number of seconds to run motors

move_forward()
mc.stop_motors()
sleep(10)
move_backward()
mc.stop_motors()
