import matplotlib.pyplot as plt
import numpy as np
#input q#
qn=int(input())
# your code
plt.axis('equal')
fig , ax = plt.subplots()
ax.set_title("323004895  &  207976382")
ax.set_xlim(-3,3)
ax.set_ylim(-3,3)
ax.set_xlabel('x')
ax.set_ylabel('y')
# setting a range for the fuctions

#setting and drawing the function x^2+y^2=1
A="MAAGAL"
#setting and drawing the function at qn 2

#output
if (qn == 1): 
 theta = np.linspace(0, 2 * np.pi, 1000)
 x = np.cos(theta)
 y = np.sin(theta)
 plt.plot(x, y, label=r'$x^2 + y^2 = 1$')
 plt.title('Circle: $x^2 + y^2 = 1$')
 plt.xlabel('x')
 plt.ylabel('y')
 print(A)
elif (qn == 2):
 x=np.arange(-1,1,0.000001)
 y=np.sqrt(1-x**2)+np.sqrt(x**2)
 y2=-(np.sqrt(1-x**2))+np.sqrt(x**2)
 plt.plot(x, y, color='black')+plt.plot(x,y2,color='black')
 B="LEV"


plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')  # Equal aspect ratio
plt.legend()
plt.show()
plt.show()