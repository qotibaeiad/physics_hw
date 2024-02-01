#imports
import numpy as np


# input 
v0x=float(input())
v0y=float(input())
qn=int(input())

## your code
G = -9.8

t = np.linspace(0, np.abs(2*v0y/G), 300)
t_size = len(t)
t_step = t[1]

ax = np.zeros(t_size)
ay = np.ones(t_size) * G

vx = np.ones(t_size) * v0x
vy = np.cumsum(ay) * t_step + v0y

x = np.cumsum(vx) * t_step
y = np.cumsum(vy) * t_step


vertical_offset = (t[-1] + t_step) * v0x

##

# output
if qn==1:
    #output example, fill in the rest
    print(ay[0:10])
elif qn==2:
    print(vx[0:10])
elif qn==3:
    print(vy[0:10])
elif qn==4:
    print(x[0:10])
elif qn==5:
    print(y[0:10])
elif qn==6:
    print(vertical_offset)
elif qn==7:
    print(0.5*G/(v0x ** 2))