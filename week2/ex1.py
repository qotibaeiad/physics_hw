import numpy as np

qn = int(input())


A=np.arange(0.0, 10.0, 1.0)
B=np.power(10.0, np.arange(10.0))-1.0
C=np.diff(B)
D=np.flip(C)
E=np.cumsum(D)
x=np.arange(0.0, 6.29, 0.01)
f=np.power(np.sin(x),2.0)
I=np.sum(np.power(np.sin(x),2.0) * 0.01)
range=np.arange(0,6.28,0.01)
w=np.sin(range)
F=f**2

if qn == 1:
    print(A)
elif qn == 2:
    print(B)
elif qn == 3:
    print(C)
elif qn==4:
    print(D)
elif qn==5:
    print(E)
elif qn==6:
    print(f)
elif qn==7:
    print(I)
elif qn==8:
    x=np.arange(0.0,6.28,0.01)
    y = np.power(np.sin(x),2.0)