import numpy as np

qn = int(input('enter question number: '))

x_value = np.arange(0, 2, 0.01)
f = np.exp(x_value)
x_slicing1 = x_value[2:] 
x_slicing2 = x_value[:-2]
fdot = [(np.exp(x1) - np.exp(x2)) / (2 * 0.01) for x1, x2 in zip(x_slicing1, x_slicing2)]
np.set_printoptions(precision=8)
if qn==1:
    print(f[0:9])
elif qn==2:
    print(fdot[0:9])
    """
elif qn==3:
    print(fdot2[0:9])
    """
