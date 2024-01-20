import numpy as np
import matplotlib.pyplot as plt

#input
A=float(input("A:"))
B=float(input("B:"))
qn=int(input("qn:"))

# you code
##########
C = abs(abs(A)-abs(B))
D = A + B
x = np.linspace(0, 10, 1000)
y = np.sin(x+2)*np.cos(2*x-3)
plt.plot(x, y, label=r'$\sin(x+2) + \cos(2x-3)$')
plt.title('Graph of the Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
##########
#output
if qn==1: 
    print(f'{C:.5g}')
elif qn==2: 
    print(f'{D:.5g}')
elif qn==3:
    print(max_no)