import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QLabel, QGridLayout
from PyQt5.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class Visualization(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.figure = Figure(figsize=(5, 5))
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_aspect('equal', adjustable='box')
        self.ax.set_xlim(-1.1, 1.1)
        self.ax.set_ylim(-1.1, 1.1)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self, angle):
        self.ax.clear()
        angle_rad = np.radians(angle)
        opposite = np.sin(angle_rad)
        adjacent = np.cos(angle_rad)
        hypotenuse = 1
        triangle_points = [(0,0),(adjacent,0),(adjacent,opposite)]
        theta = np.linspace(0, 2*np.pi, 100)
        x = np.cos(theta)
        y = np.sin(theta)
        self.ax.plot(x, y)
        self.ax.plot([p[0] for p in triangle_points + [triangle_points[0]]], [p[1] for p in triangle_points + [triangle_points[0]]], 'r-')
        self.ax.plot([0, adjacent], [0, opposite], 'k--')
        self.ax.plot([adjacent, adjacent], [0, opposite], 'k--')
        self.ax.plot([0, adjacent], [0, 0], 'k--')
        self.ax.grid(True)
        self.ax.xaxis.set_major_locator(plt.MultipleLocator(0.5))
        self.ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
        self.canvas.draw()

class ValueOfAngle(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.sin = QLabel()
        self.cos = QLabel()
        self.tan = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.sin)
        layout.addWidget(self.cos)
        layout.addWidget(self.tan)
        self.setLayout(layout)

    def changeValue(self, degree):
        rad = math.radians(degree)
        sinv = math.sin(rad)
        cosv = math.cos(rad)
        tanv = math.tan(rad)
        self.sin.setText(f"sinθ = {sinv:.2f}")
        self.cos.setText(f"cosθ = {cosv:.2f}")
        self.tan.setText(f"tanθ = {tanv:.2f}")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("삼각함수 시각화")
        self.setGeometry(300, 300, 600, 600)

        self.value_of_angle = ValueOfAngle()
        self.visualization = Visualization()

        layout = QGridLayout()
        self.setLayout(layout)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 360)
        self.slider.setValue(0)
        self.slider.valueChanged.connect(self.sliderValueChanged)
        self.slider.valueChanged.connect(self.visualization.plot)

        layout.addWidget(self.slider, 0, 0)
        layout.addWidget(self.value_of_angle, 1, 0)
        layout.addWidget(self.visualization, 2, 0)

    def sliderValueChanged(self, val):
        self.value_of_angle.changeValue(val)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
