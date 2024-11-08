import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class ObjectMovement:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], 'ro-')
        self.ax.set_xlim(0, self.data['x'].max() + 1)
        self.ax.set_ylim(0, self.data['y'].max() + 1)
        self.ax.set_title('Object Movement Over Time')
        self.ax.set_xlabel('X Coordinate')
        self.ax.set_ylabel('Y Coordinate')

    def init(self):
        self.line.set_data([], [])
        return self.line,

    def update(self, frame):
        x = self.data['x'][:frame + 1]
        y = self.data['y'][:frame + 1]
        self.line.set_data(x, y)
        return self.line,

    def animate(self):
        ani = animation.FuncAnimation(self.fig, self.update, frames=len(self.data), init_func=self.init, blit=True)
        plt.show()

if __name__ == "__main__":
    movement = ObjectMovement('object_movement.csv')
    movement.animate()
