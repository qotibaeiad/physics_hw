import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Function to update the graph when the slider is moved
def update(val):
    x_point = slider.val
    y_point = m * x_point + b
    point.set_data(x_point, y_point)
    fig.canvas.draw_idle()

# Generate some sample data
x = np.linspace(0, 10, 100)
m, b = 2, 1
y = m * x + b

# Create the initial plot
fig, ax = plt.subplots()
line, = ax.plot(x, y, label='Line')
point, = ax.plot(0, 0, 'ro', label='Point')

# Create a slider axes
slider_ax = plt.axes([0.2, 0.01, 0.65, 0.03])
slider = Slider(slider_ax, 'X', 0, 10, valinit=0)

# Register the update function with the slider
slider.on_changed(update)

# Display the plot
plt.legend()
plt.show()
