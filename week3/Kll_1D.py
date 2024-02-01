import numpy as np

v0=float(input('enter start speed: '))
gama=float(input('enter gama: '))
qn=int(input('enter question num: '))


t=np.arange(0,7,0.01)
v = v0*np.exp(t*(-gama))*np.cos(10*gama*t)

if qn==1:
    print(t[:10])
if qn==2:
    print(v[:10])