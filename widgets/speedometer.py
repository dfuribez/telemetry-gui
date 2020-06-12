from PyQt5.QtWidgets import QWidget 
from PyQt5.QtCore import QUrl, QObject

from PyQt5 import uic

ui_class = uic.loadUiType("widgets/ui/speedometer.ui")[0]

class Speedometer(QWidget, ui_class):

    def __init__(self):
        QWidget.__init__(self, None)
        self.setupUi(self)
        self.qt_qw.setSource(QUrl("widgets/qml/speedometer.qml"))
        self.root = self.qt_qw.rootObject()
        self.gauge = self.root.findChild(QObject, "gauge")
        self.text = self.root.findChild(QObject, "text")
        print(self.qt_qw.rootObject().findChild(QObject, ""))
    
    def change_value(self, value):
        self.gauge.setProperty("gauge_value", value)  # changes needle position
        self.text.setProperty("text", value)  # change value of the text
    
    def set_backgroundcolor(self, color):
        self.root.setProperty("color", color)
    
    def set_limits(self, min_value, max_value):
        self.gauge.setProperty("max_value", max_value)
        self.gauge.setProperty("min_value", min_value)
    
    def set_limit_colors(self, min_color, max_color):
        self.gauge.setProperty("min_color", min_color)
        self.gauge.setProperty("max_color", max_color)
        

