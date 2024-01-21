import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def draw_vector_difference(x1, y1, x2, y2):
    x_diff = x1 - x2
    y_diff = y1 - y2

    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_title('Vector Difference')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    arw1 = mpatches.Arrow(0, 0, x1, y1, width=0.2, color='g', label='Vector 1')
    arw2 = mpatches.Arrow(0, 0, x2, y2, width=0.2, color='b', label='Vector 2')

    awr1_array = np.array([x1, y1])
    awr2_array = np.array([x2, y2])

    dot_product = np.dot(awr1_array, awr2_array)
    length1 = np.sqrt(x1**2 + y1**2)
    length2 = np.sqrt(x2**2 + y2**2)

    angle_radians = np.arccos(dot_product / (length1 * length2))
    angle_degrees = np.degrees(angle_radians)
    print('the degrees of two victor: ', angle_degrees)

    if y1 < y2:
        startx = x1
        starty = y1
    else:
        startx = x2
        starty = y2

    arw_diff = mpatches.Arrow(startx, starty, x_diff, y_diff, width=0.4, color='y', label='Vector Difference')
    degree_diff_with_axisy=np.degrees(np.arctan(x_diff/y_diff))
    print('the diff degree: ',degree_diff_with_axisy)

    endx1 = startx + x1
    endy1 = starty + y1
    endx2 = startx + x2
    endy2 = starty + y2

    par1 = mpatches.Arrow(startx, starty, x1, y1, width=0.4, color='r', label='Parallelogram 1')
    par2 = mpatches.Arrow(startx, starty, x2, y2, width=0.4, color='r', label='Parallelogram 2')

    ax.add_patch(arw1)
    ax.add_patch(arw2)
    ax.add_patch(arw_diff)
    ax.add_patch(par1)
    ax.add_patch(par2)

    ax.legend()
    plt.show()

# Example usage
x1 = float(input('Enter x coordinate of the first vector: '))
y1 = float(input('Enter y coordinate of the first vector: '))
x2 = float(input('Enter x coordinate of the second vector: '))
y2 = float(input('Enter y coordinate of the second vector: '))
draw_vector_difference(x1, y1, x2, y2)
