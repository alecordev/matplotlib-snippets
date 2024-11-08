import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class ObjectMovement:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
        self.fig, self.ax = plt.subplots()
        self.circle = plt.Circle((0, 0), 0.1, color='red')  # Create a circle with a radius of 0.1
        self.ax.add_artist(self.circle)
        self.ax.set_xlim(0, self.data['x'].max() + 1)
        self.ax.set_ylim(0, self.data['y'].max() + 1)
        self.ax.set_title('Object Movement Over Time')
        self.ax.set_xlabel('X Coordinate')
        self.ax.set_ylabel('Y Coordinate')

    def init(self):
        self.circle.set_center((0, 0))  # Initialize the circle's position
        return self.circle,

    def update(self, frame):
        # Get the current position from the data
        x = self.data['x'].iloc[frame]
        y = self.data['y'].iloc[frame]
        self.circle.set_center((x, y))  # Update the circle's position
        return self.circle,

    def animate(self, filename="animation"):
        ani = animation.FuncAnimation(self.fig, self.update, frames=len(self.data), init_func=self.init, blit=True)
        ani.save(f'{filename}.mp4', writer='ffmpeg', fps=1)
        plt.show()

if __name__ == "__main__":
    # Example CSV data creation for demonstration purposes
    # You can replace this with your actual CSV file
    data = {
        'x': np.linspace(0, 10, 100),  # 100 points from 0 to 10
        'y': np.sin(np.linspace(0, 10, 100)) * 5 + 5  # Sine wave for y values
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_object_movement.csv', index=False)

    movement = ObjectMovement('object_movement.csv')
    movement.animate()
