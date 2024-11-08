import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# Step 1: Read the CSV file
data = pd.read_csv('data2.csv', parse_dates=['timestamp'], index_col='timestamp')

# Step 2: Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(data.index.min(), data.index.max())
ax.set_ylim(data['value'].min() - 5, data['value'].max() + 5)
line, = ax.plot([], [], lw=2)
ax.set_xlabel('Timestamp')
ax.set_ylabel('Value')
ax.set_title('Time Series Data')

# Step 3: Initialize the line object
def init():
    line.set_data([], [])
    return line,

# Step 4: Update function for animation
def update(frame):
    x = data.index[:frame]
    y = data['value'][:frame]
    line.set_data(x, y)
    return line,

# Step 5: Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(data), init_func=init, blit=True)

# Step 6: Save the animation as a video
ani.save('time_series_video2.mp4', writer='ffmpeg', fps=1)

# Optional: Show the plot (if you want to see it live)
# plt.show()
