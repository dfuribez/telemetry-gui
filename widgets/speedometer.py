from PyQt5.QtWidgets import QWidget 
from PyQt5.QtCore import QUrl, QObject

from PyQt5 import uic

ui_class = uic.loadUiType("widgets/ui/speedometer.ui")[0]

class Speedometer(QWidget, ui_class):

    def __init__(self):
        QWidget.__init__(self, None)
        self.setupUi(self)
        self.qt_qw.setSource(QUrl("widgets/qml/speedometer.qml"))
        self.needle = self.qt_qw.rootObject().findChild(QObject, "gauge")
        print(self.needle)
    
    def change_value(self, value):
        self.needle.setProperty("gauge_value", value)

