from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

m1 = Motor(Port.E)
m2 = Motor(Port.F)

h = InventorHub()


while True:
    x, y = h.imu.tilt()

    h.display.number(x)

    if abs(m1.angle() - x) > 5:
        m1.run_target(speed=2000, target_angle=x, wait=False)
        m2.run_target(speed=2000, target_angle=-m1.angle(), wait=False)

