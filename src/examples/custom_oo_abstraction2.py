import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def __init__(self, x_data, y_data, title, x_label, y_label, y2_data=None, y2_label=None):
        self.x_data = x_data
        self.y_data = y_data
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.y2_data = y2_data
        self.y2_label = y2_label
        self.fig, self.ax = plt.subplots()

    def create_plot(self, line_style='-', color='b', marker='o', label='Data Line'):
        """Create the plot with the provided data."""
        self.ax.plot(self.x_data, self.y_data, linestyle=line_style, color=color, marker=marker, label=label)
        self.ax.set_title(self.title, fontsize=16)
        self.ax.set_xlabel(self.x_label, fontsize=14)
        self.ax.set_ylabel(self.y_label, fontsize=14)
        self.ax.grid(True)
        self.ax.legend(loc='upper left')  # Adjust legend position
        self.ax.set_xlim([min(self.x_data) - 1, max(self.x_data) + 1])
        self.ax.set_ylim([min(self.y_data) - 1, max(self.y_data) + 1])

        # If a second dataset is provided, create a second y-axis
        if self.y2_data is not None and self.y2_label is not None:
            ax2 = self.ax.twinx()
            ax2.plot(self.x_data, self.y2_data, linestyle='--', color='r', label=self.y2_label)
            ax2.set_ylabel(self.y2_label, fontsize=14)
            ax2.legend(loc='upper right')

    def add_description(self, text, position=(0.5, -0.15), fontsize=12, ha='center', va='center'):
        """Add a description below the plot."""
        self.ax.text(position[0], position[1], text, ha=ha, va=va, transform=self.ax.transAxes, fontsize=fontsize)

    def annotate_point(self, x, y, text, offset=(5, 5), fontsize=10):
        """Annotate a specific data point with text."""
        self.ax.annotate(text, (x, y), textcoords="offset points", xytext=offset, ha='center', fontsize=fontsize, bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='white'))

    def show(self):
        """Display the plot with tight layout."""
        plt.tight_layout()
        plt.show()

# Sample data
x = np.linspace(0, 10, 10)
y1 = np.sin(x)
y2 = np.cos(x) * 10  # Second dataset for the secondary y-axis

# Create a plot instance
plot = Plotter(x_data=x, y_data=y1, title='Sine and Cosine Waves', x_label='X-axis (radians)', y_label='Y-axis (sin(x))', y2_data=y2, y2_label='Y-axis (10*cos(x))')

# Create the plot
plot.create_plot(line_style='-', color='b', marker='o', label='Sine Wave')

# Add a description
description_text = "This plot shows the sine function and a scaled cosine function over the interval [0, 10]."
plot.add_description(description_text, position=(0.5, -0.25), fontsize=12)  # Adjusted position

# Annotate a specific point
plot.annotate_point(x=5, y=np.sin(5), text='(5, sin(5))', offset=(0, 10))

# Show the plot
plot.show()
