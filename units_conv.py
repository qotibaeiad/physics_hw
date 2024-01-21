import numpy as np


def OneToTwo(speed):
    return 0.621371*(1/3600)*speed
def OneToThree(speed):
    return (1/1.852)*speed
def TwoToOne(speed):
    return speed*1.60934*3600
def TwoTaoThree(speed):
    return speed*1.15078
def ThreeToOne(speed):
    return speed*1.852
def ThreeToTwo(speed):
    return speed*(1/3600)*1.15078

v = float(input('enter speed: '))
unit = float(input('enter num of the unit 1-3: '))
outputunit = float(input('output ubit 1-3: '))

if(unit==1 and outputunit==2):
    print("the speed:- ",OneToTwo(v))
elif(unit==1 and outputunit==3):
    print("the speed:- ",OneToThree(v))
elif(unit==2 and outputunit==1):
    print("the speed:- ",TwoToOne(v))
elif(unit==2 and outputunit==3):
    print("the speed:- ",TwoTaoThree(v))
elif(unit==3 and outputunit==1):
    print("the speed:- ",ThreeToOne(v))
elif(unit==3 and outputunit==2):
    print("the speed:- ",ThreeToTwo(v))