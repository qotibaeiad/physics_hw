import matplotlib.pyplot as plt
import numpy as np

# input q
qn = int(input())

# your code
A = "maagal"  # example
B = "heb"
plt.xlim(-2,2)
plt.ylim(-2,2)
if qn == 1:
    theta = np.linspace(0, 2 * np.pi, 1000)
    x = np.cos(theta)
    y = np.sin(theta)
    
    plt.plot(x, y, label=r'$x^2 + y^2 = 1$')
    plt.title('Circle: $x^2 + y^2 = 1$')
    plt.xlabel('x')
    plt.ylabel('y')

elif qn == 2:
    x = np.linspace(-10, 10, 1000)
    y1 = np.sqrt(1 - x**2) + x**(3/2)
    y2 = -np.sqrt(1 - x**2) + x**(3/2)
    
    plt.plot(x, y1, label=r'$y = \sqrt{1 - x^2} + \frac{x^2}{3}$')
    plt.plot(x, y2, label=r'$y = -\sqrt{1 - x^2} + \frac{x^2}{3}$')
    # plt.title('Curve: $y = \sqrt{1 - x^2} + \frac{x^2}{3}$')
    plt.xlabel('x')
    plt.ylabel('y')

plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')  # Equal aspect ratio

# Display the plot
plt.legend()
plt.show()

# output
if qn == 1:
    print(A)
elif qn == 2:
    print(B)