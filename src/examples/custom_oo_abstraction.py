import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def __init__(self, x_data, y_data, title, x_label, y_label):
        self.x_data = x_data
        self.y_data = y_data
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.fig, self.ax = plt.subplots()

    def create_plot(self):
        """Create the plot with the provided data."""
        self.ax.plot(self.x_data, self.y_data, marker='o', linestyle='-', color='b', label='Data Line')
        self.ax.set_title(self.title, fontsize=16)
        self.ax.set_xlabel(self.x_label, fontsize=14)
        self.ax.set_ylabel(self.y_label, fontsize=14)
        self.ax.grid(True)
        self.ax.legend()
        self.ax.set_xlim([min(self.x_data) - 1, max(self.x_data) + 1])
        self.ax.set_ylim([min(self.y_data) - 1, max(self.y_data) + 1])

    def add_description(self, text, position=(0.5, -0.15)):
        """Add a description below the plot."""
        self.ax.text(position[0], position[1], text, ha='center', va='center', transform=self.ax.transAxes, fontsize=12)

    def show(self):
        """Display the plot."""
        plt.tight_layout()
        plt.show()

# Sample data
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Create a plot instance
plot = Plotter(x_data=x, y_data=y, title='Sine Wave', x_label='X-axis (radians)', y_label='Y-axis (sin(x))')

# Create the plot
plot.create_plot()

# Add a description
description_text = "This plot shows the sine function over the interval [0, 10]."
plot.add_description(description_text)

# Show the plot
plot.show()
