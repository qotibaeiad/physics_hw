import numpy as np

Ax=float(input("Ax: "))
Ay=float(input("Ay: "))
Az=float(input("Az: "))
B=np.array([3,4,-2])
## your code:
sum=0
A=np.array([Ax,Ay,Az])
for i in range (0,3):
    sum+=B[i]*A[i]
len1=np.sqrt(np.sum(B**2))
len2=np.sqrt(Ax**2+Ay**2+Az**2)
alpha = np.arccos(sum/(len1*len2))
alpha=np.degrees(alpha)
##
print(alpha)
