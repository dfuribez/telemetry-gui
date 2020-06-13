from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from collections import deque

import pyqtgraph as pg


ui_class = uic.loadUiType("widgets/ui/graph.ui")[0]


class Graph(QWidget, ui_class):

    def __init__(self):
        QWidget.__init__(self, None)
        self.setupUi(self)

        self.plots = {}

        self.pg_window = pg.GraphicsWindow()
        self.plot = self.pg_window.addPlot()
        self.plot.addLegend()
        self.qt_vl.addWidget(self.pg_window)
    
    def set_style(self, background, foreground):
        pg.setConfigOption("background", "red")
        pg.setConfigOption("foreground", "w")
    
    def addplot(self, name):
        self.plots[name] = self.plot.plot(name=name)
    
    def plot_(self, plot_name, x, y):
        self.plots[plot_name].setData(x, y, pen=(1, 3), antialias=True)
    
    def set_plot_limit(self, max_points):
