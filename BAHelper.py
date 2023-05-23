from PyQt5 import QtWidgets as QW
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QGuiApplication
import pandas as pd

class MainWindow(QW.QMainWindow):
    def __init__(self): 
        super(MainWindow,self).__init__()
        self.ui = loadUi("BAHelper_ui.ui",self)
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
        # self.ui.Theme.setChecked(False)
        # self.changeTheme()
        
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
        self.ui.actionLight.triggered.connect(lambda: self.changeTheme("light"))
        self.ui.actionDark.triggered.connect(lambda: self.changeTheme("dark"))
        self.ui.actionGerman.triggered.connect()
        self.ui.actionEnglish.triggered.connect()
        self.hpToDict("HPeng.txt")
        self.buttons()
        
    def buttons(self):
        hkey_x = 0
        pkey_x = 0
        for key in self.HP.keys():
            checkBox = QW.QCheckBox(str(key))
            if "H" in key:
                if key[1] == "2":
                    self.ui.hLayout.addWidget(checkBox,hkey_x,0)
                elif key[1] == "3":
                    self.ui.hLayout.addWidget(checkBox,hkey_x,1)
                elif key[1] == "4":
                    self.ui.hLayout.addWidget(checkBox,hkey_x,2)
                else:
                    self.ui.hLayout.addWidget(checkBox,hkey_x,3)
                hkey_x += 1
            elif "P" in key:
                if key[1] == "1":
                    self.ui.pLayout.addWidget(checkBox,pkey_x,0)
                elif key[1] == "2":
                    self.ui.pLayout.addWidget(checkBox,pkey_x,1)
                elif key[1] == "3":
                    self.ui.pLayout.addWidget(checkBox,pkey_x,2)
                elif key[1] == "4":
                    self.ui.pLayout.addWidget(checkBox,pkey_x,3)
                else:
                    self.ui.pLayout.addWidget(checkBox,pkey_x,4)
                pkey_x += 1
        
    def changeTheme(self,theme):
        """
        Changes the colour theme of the program to either light or dark.

        Returns
        -------
        None.

        """
        if theme == "light":
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
        
    def hpToDict(self,filename):
        self.HP = pd.read_csv(filename, delimiter="\t", index_col=0, header=None).to_dict()[1]

    def output(self):
        if self.ui.language.text() == "german":
            self.hpToDict("HPger.txt")
        else:
            self.hpToDict("HPeng.txt")
        self.buttons()
    #for every selected checkbox in h snetences
    #  add to list
    # dito for p sentences
    # for every key in list
    # give key \t value
    # open popup mit ergebnissen
    # copy to clipboard button?

            
#####################################APP#######################################            
            
if __name__ == '__main__':
    import sys
    BAHelper = QW.QApplication(sys.argv)
    BAHelper.setStyle('Fusion')
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(BAHelper.exec_())
