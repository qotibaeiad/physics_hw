import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider



def update(val):
    x_point = v0x*(val)
    y_point = ((v0y*x_point)/v0x)+((1/2)*G*((x_point**2)/(v0x**2)))
    point.set_data(x_point, y_point)


    vector_scale = 0.01 
    vector_dx = v0x*vector_scale
    vector_dy = v0y-G*val*vector_scale
    vector.set_offsets(np.array([[x_point, y_point]]))
    vector.set_UVC(vector_dx, vector_dy)

    fig.canvas.draw_idle()



# input
v0x = float(input())
v0y = float(input())
qn = int(input())

## your code
G = -9.8

t = np.linspace(0, np.abs(2 * v0y / G), 300)
t_size = len(t)
t_step = t[1]

ax = np.zeros(t_size)
ay = np.ones(t_size) * G

vx = np.ones(t_size) * v0x
vy = np.cumsum(ay) * t_step + v0y

x = np.cumsum(vx) * t_step
y = np.cumsum(vy) * t_step
print(x, y)

vertical_offset = (t[-1] + t_step) * v0x

xt=v0x*t
yfunc=((v0y*xt)/v0x)+((1/2)*G*((xt**2)/(v0x**2)))


fig, ax = plt.subplots()
line, = ax.plot(xt, yfunc, label='line')
point, = ax.plot(x[0], y[0], 'bo', label='Point')  # Initial position of the point

vector = ax.quiver(0, 0, v0x, v0y-G*0, angles='xy', scale_units='xy', scale=1, color='r', label='Vector')


slider_ax = plt.axes([0.2, 0.01, 0.65, 0.03])
slider = Slider(slider_ax, 'Time', t[0], t[-1], valinit=t[0], valstep=t_step)

slider.on_changed(update)
plt.legend()
plt.show()

# output
if qn == 1:
    print(ay[0:10])
elif qn == 2:
    print(vx[0:10])
elif qn == 3:
    print(vy[0:10])
elif qn == 4:
    print(x[0:10])
elif qn == 5:
    print(y[0:10])
elif qn == 6:
    print(vertical_offset)
elif qn == 7:
    print(0.5 * G / (v0x ** 2))



""""
def update(val):
    x_point = x[int(val / t_step)]
    y_point = y[int(val / t_step)]
    point.set_data(x_point, y_point)
    fig.canvas.draw_idle()

# input
v0x = float(input())
v0y = float(input())
qn = int(input())

## your code
G = -9.8

t = np.linspace(0, np.abs(2 * v0y / G), 300)
t_size = len(t)
t_step = t[1]

ax = np.zeros(t_size)
ay = np.ones(t_size) * G

vx = np.ones(t_size) * v0x
vy = np.cumsum(ay) * t_step + v0y

x = np.cumsum(vx) * t_step
y = np.cumsum(vy) * t_step
print(x, y)

vertical_offset = (t[-1] + t_step) * v0x



fig, ax = plt.subplots()
line, = ax.plot(x, y, label='line')
point, = ax.plot(x[0], y[0], 'bo', label='Point')  # Initial position of the point

slider_ax = plt.axes([0.2, 0.01, 0.65, 0.03])
slider = Slider(slider_ax, 'Time', t[0], t[-1], valinit=t[0], valstep=t_step)

slider.on_changed(update)
plt.legend()
plt.show()

# output
if qn == 1:
    print(ay[0:10])
elif qn == 2:
    print(vx[0:10])
elif qn == 3:
    print(vy[0:10])
elif qn == 4:
    print(x[0:10])
elif qn == 5:
    print(y[0:10])
elif qn == 6:
    print(vertical_offset)
elif qn == 7:
    print(0.5 * G / (v0x ** 2))
"""