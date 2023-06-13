from PyQt5 import QtWidgets as QW
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QGuiApplication
import pandas as pd
import numpy as np

class MainWindow(QW.QMainWindow):
    def __init__(self): 
        super(MainWindow,self).__init__()
        self.ui = loadUi("BAHelper_ui.ui",self)
        self.startUp()
        self.functionality()
        self.AllH = []
        self.AllP = []
  
    def startUp(self):
        """
        Ensures that upon startup everything is shown correctly.

        Returns
        -------
        None.

        """
        self.default_palette = QGuiApplication.palette()
        self.hpToDict("HPger.txt")
        self.ui.labelOutput.setText("Output Language: German")
        self.buttons()
        
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
        self.ui.actionGerman.triggered.connect(self.german)
        self.ui.actionEnglish.triggered.connect(self.english)
        self.ui.pushOutput.clicked.connect(self.singleOutput)
        self.ui.pushClearConsole.clicked.connect(self.clearConsole)
        self.ui.pushResetButtons.clicked.connect(self.resetButtons)
        self.ui.pushCopy.clicked.connect(self.copyToClipboard)
        self.ui.pushOutputAll.clicked.connect(self.fullOutput)
        
    def german(self):
        self.hpToDict("HPger.txt")
        self.ui.labelOutput.setText("Output Language: German")
        
    def english(self):
        self.hpToDict("HPeng.txt")
        self.ui.labelOutput.setText("Output Language: English")
        
    def buttons(self):
        bh = 0
        ch = 0
        dh = 0
        eh = 0
        ap = 0
        bp = 0
        cp = 0
        dp = 0
        ep = 0
        for key in self.HP.keys():
            checkBox = QW.QCheckBox(str(key))
            if "H" in key:
                if key[1] == "2":
                    self.ui.hLayout.addWidget(checkBox,bh,0)
                    bh += 1
                elif key[1] == "3":
                    self.ui.hLayout.addWidget(checkBox,ch,1)
                    ch += 1
                elif key[1] == "4":
                    self.ui.hLayout.addWidget(checkBox,dh,2)
                    dh += 1
                else:
                    self.ui.hLayout.addWidget(checkBox,eh,3)
                    eh += 1
            elif "P" in key:
                if key[1] == "1":
                    self.ui.pLayout.addWidget(checkBox,ap,0)
                    ap += 1
                elif key[1] == "2":
                    self.ui.pLayout.addWidget(checkBox,bp,1)
                    bp += 1
                elif key[1] == "3":
                    self.ui.pLayout.addWidget(checkBox,cp,2)
                    cp += 1
                elif key[1] == "4":
                    self.ui.pLayout.addWidget(checkBox,dp,3)
                    dp += 1
                else:
                    self.ui.pLayout.addWidget(checkBox,ep,4)
                    ep += 1
        
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

    def clearConsole(self):
        self.ui.textOutput.clear()
        
    def resetButtons(self):
        for checkBox in self.findChildren(QW.QCheckBox):
            checkBox.setChecked(False)
            
    def copyToClipboard(self):
        self.ui.textOutput.selectAll()
        self.ui.textOutput.copy()

    def singleOutput(self):
        Hshort = []
        for HcheckBox in self.findChildren(QW.QCheckBox):
            if HcheckBox.isChecked() == True and HcheckBox.text()[0] == "H":
                Hshort.append(HcheckBox.text())
        Pshort = []
        for PcheckBox in self.findChildren(QW.QCheckBox):
            if PcheckBox.isChecked() == True and PcheckBox.text()[0] == "P":
                Pshort.append(PcheckBox.text())
        for H in Hshort:
            if H not in self.AllH:
                self.AllH.append(H)
        for P in Pshort:
            if P not in self.AllP:
                self.AllP.append(P)
        hNum = str(Hshort).replace("[", "").replace("]", "").replace("'","")
        self.ui.textOutput.append(hNum)
        self.ui.textOutput.append("\n")
        pNum = str(Pshort).replace("[", "").replace("]", "").replace("'","")
        self.ui.textOutput.append(pNum)
        self.ui.textOutput.append("\n")
        self.resetButtons()

    def fullOutput(self):
        for short in self.AllH:
            fulltext = short + ": " + self.HP[short]
            self.ui.textOutput.append(fulltext)
        self.ui.textOutput.append("\n")
        for short in self.AllP:
            fulltext = short + ": " + self.HP[short]
            self.ui.textOutput.append(fulltext)
        
###############################################################################

        
        
#####################################APP#######################################            
            
if __name__ == '__main__':
    import sys
    BAHelper = QW.QApplication(sys.argv)
    BAHelper.setStyle('Fusion')
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(BAHelper.exec_())
