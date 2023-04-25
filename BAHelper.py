from PyQt5 import QtWidgets as QW
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QGuiApplication
import numpy as np
import pandas as pd

class MainWindow(QW.QMainWindow):
    def __init__(self): 
        super(MainWindow,self).__init__()
        self.ui = loadUi("BAHelper.ui",self)
        self.startUp()
        self.functionality()
  
    def startUp(self):
        """
        Ensures that upon startup everything is shown correctly.

        Returns
        -------
        None.

        """
        self.default_palette = QGuiApplication.palette()
        self.finalInputs = {}
        self.ui.input_tree.header().setSectionResizeMode(QW.QHeaderView.ResizeToContents)
        self.radios = QW.QButtonGroup(self)
        self.radios.addButton(self.ui.GLA_radio)
        self.radios.addButton(self.ui.GTA_radio_preset_model)
        self.radios.addButton(self.ui.GTA_radio_custom_model)
        self.radios.addButton(self.ui.GTA_radio_custom_matrix)
        self.ui.stack.setCurrentIndex(0)
        self.ui.Theme.setChecked(False)
        self.changeTheme()
        
    def onQuit(self):
        """
        Resets the color theme of the application and saves input values.

        Returns
        -------
        None.

        """
        BAHelper.setPalette(self.default_palette)
        
    def functionality(self):
        """
        Adds functionality to the respective UI element.

        Returns
        -------
        None.

        """
        BAHelper.aboutToQuit.connect(self.onQuit)
        
    def changeTheme(self):
        """
        Changes the colour theme of the program to either light or dark.

        Returns
        -------
        None.

        """
        if self.ui.Theme.isChecked() == True:
            BAHelper.setPalette(self.default_palette)
        else:
            darkmode = QPalette()
            darkmode.setColor(darkmode.Window, QColor(53, 53, 53))
            darkmode.setColor(darkmode.WindowText, Qt.white)
            darkmode.setColor(darkmode.Base, QColor(25, 25, 25))
            darkmode.setColor(darkmode.AlternateBase, QColor(53, 53, 53))
            darkmode.setColor(darkmode.ToolTipBase, Qt.black)
            darkmode.setColor(darkmode.ToolTipText, Qt.white)
            darkmode.setColor(darkmode.Text, Qt.white)
            darkmode.setColor(darkmode.Button, QColor(53, 53, 53))
            darkmode.setColor(darkmode.ButtonText, Qt.white)
            darkmode.setColor(darkmode.BrightText, Qt.green)
            darkmode.setColor(darkmode.Link, QColor(42, 130, 218))
            darkmode.setColor(darkmode.Highlight, QColor(42, 130, 218))
            darkmode.setColor(darkmode.HighlightedText, Qt.black)
            BAHelper.setPalette(darkmode)
        
#####################################APP#######################################            
            
if __name__ == '__main__':
    import sys
    BAHelper = QW.QApplication(sys.argv)
    BAHelper.setStyle('Fusion')
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(BAHelper.exec_())
