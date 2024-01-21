import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

## input
x1=float(input('enter x coordinate of the first vector: '))
y1=float(input('enter y coordinate of the first vector: '))
x2=float(input('enter x coordinate of the second vector: '))
y2=float(input('enter y coordinate of the second vector: '))
qn=int(input('enter question number to answer: '))

## your code
fig, ax = plt.subplots()
ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.set_title('Vector Addition and Subtraction\n323004895  &  207976382')
ax.set_xlabel('x')
ax.set_ylabel('y')
arw1 = mpatches.Arrow(0, 0, x1, y1, width = 0.1,color='black')
ax.add_patch(arw1)
arw1 = mpatches.Arrow(0, 0, x2, y2, width = 0.1,color='black')
ax.add_patch(arw1)
arw1 = mpatches.Arrow(x1, y1, x2, y2, width = 0.1,color='black')
ax.add_patch(arw1)
arw1 = mpatches.Arrow(x2, y2, x1, y1, width = 0.1,color='black')
ax.add_patch(arw1)
arw1 = mpatches.Arrow(0, 0, x1+x2, y1+y2, width = 0.1,color='red')
ax.add_patch(arw1)
arw1 = mpatches.Arrow(x1, y1, -x1+x2, -y1+y2, width = 0.1,color='green')
ax.add_patch(arw1)

##degrees
dx = np.abs(x2 - x1)
dy= np.abs(y2 - y1)
rad = np.arctan2(dx ,dy)
alpha = np.degrees(rad)

##squared meters
v1 = np.array([x1, y1])
v2 = np.array([x2,y2])
cross = np.cross(v1, v2)
S = np.abs(cross)

##checking if the parallelogram is a rectangle
m=x1*y1+x2*y2
noma1=np.sqrt(x1*2+y1*2)
noma2=np.sqrt(x2*2+y2*2)
if ((m/(noma1*noma2))>1):
    rect = 0
else: 
    rect=np.arccos(m/(noma1*noma2))
rect=np.degrees(rect)
if (rect == 90.0):
    rect = 1
else:
    rect = 0


## output
if qn==1:
    print(f'{alpha:.5g} degrees')
if qn==2:
    print(f'{S:.5g} squared meters')
if qn==3:
    print(rect)

plt.show()