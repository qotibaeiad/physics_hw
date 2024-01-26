import numpy as np
import matplotlib.pyplot as plt

qn = int(input('enter question number: '))

x_value = np.arange(0, 2, 0.01)
f = np.exp(x_value)
x_valuegradiant = np.arange(0,2,0.01)
x_slicing1 = x_value[2:] 
x_slicing2 = x_value[:-2]
fdot = [(np.exp(x1) - np.exp(x2)) / (2 * 0.01) for x1, x2 in zip(x_slicing1, x_slicing2)]
fdot2 = np.gradient(np.exp(x_valuegradiant))/0.01
plt.plot(x_value, f, label='f')
plt.plot(x_value[2:], fdot, '--', label='fdot')  # Use '--' for dashed line
plt.plot(x_value, fdot2, '-',label='fdot2',color='g')
if qn == 1:
    print(f[:9])
elif qn == 2:
    print(fdot[:9])
elif qn == 3:
    print(fdot2[:9])
    
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
