import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

## input
x1 = float(input('enter x coordinate of the first vector: '))
y1 = float(input('enter y coordinate of the first vector: '))
x2 = float(input('enter x coordinate of the second vector: '))
y2 = float(input('enter y coordinate of the second vector: '))

qn = int(input('enter question number to answer: '))

## Calculate vectors, parallelogram, and diagonals
v1 = np.array([x1, y1])
v2 = np.array([x2, y2])
v_sum = v1 + v2
v_diff = v1 - v2
parallelogram_points = np.array([[0, 0], v1, v1 + v2, v2, [0, 0]])
diagonal_sum_points = np.array([v1, v1 + v2])
diagonal_diff_points = np.array([v1, v1 - v2])

## Calculate angle between the difference vector and the y-axis in degrees
angle_diff_y_axis = np.degrees(np.arctan2(v_diff[1], v_diff[0]))

## Calculate area of the parallelogram
parallelogram_area = np.abs(np.cross(v1, v2))

## Check if the parallelogram is a rectangle
rectangular = np.isclose(np.dot(v1, v2), 0)

## Plotting
fig, ax = plt.subplots()
ax.plot(parallelogram_points[:, 0], parallelogram_points[:, 1], 'b-')
ax.plot(diagonal_sum_points[:, 0], diagonal_sum_points[:, 1], 'r-')
ax.plot(diagonal_diff_points[:, 0], diagonal_diff_points[:, 1], 'g-')

## Highlight the vertices of the parallelogram
ax.plot(parallelogram_points[:, 0], parallelogram_points[:, 1], 'bo')

## Annotate vectors
ax.annotate('v1', xy=v1, xytext=(v1 + v2) / 2, arrowprops=dict(facecolor='black', shrink=0.05))

ax.annotate('v2', xy=v2, xytext=(v1 + v2) / 2, arrowprops=dict(facecolor='black', shrink=0.05))

## Set axis limits
ax.set_xlim(min(0, v1[0], v2[0], v1[0] + v2[0]), max(0, v1[0], v2[0], v1[0] + v2[0]))
ax.set_ylim(min(0, v1[1], v2[1], v1[1] + v2[1]), max(0, v1[1], v2[1], v1[1] + v2[1]))

## output
if qn == 1:
    print(f'{angle_diff_y_axis:.5g} degrees')
if qn == 2:
    print(f'{parallelogram_area:.5g} squared meters')
if qn == 3:
    print(int(rectangular))

plt.show()
