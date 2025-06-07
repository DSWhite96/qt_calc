import pathlib
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class CalcGUI(QMainWindow):
    """
    Class representing the different elements of the GUI for this calculator application
    """
    def __init__(self):
        """
        Constructor
        """
        super(CalcGUI, self).__init__()
        path = str(pathlib.Path(__file__).parent.resolve()) + "/calc.ui"
        uic.loadUi(path, self)

        #Defining input from number buttons
        self.zeroButton.clicked.connect(lambda: self.displayInput("0"))
        self.oneButton.clicked.connect(lambda: self.displayInput("1"))
        self.twoButton.clicked.connect(lambda: self.displayInput("2"))
        self.threeButton.clicked.connect(lambda: self.displayInput("3"))
        self.fourButton.clicked.connect(lambda: self.displayInput("4"))
        self.fiveButton.clicked.connect(lambda: self.displayInput("5"))
        self.sixButton.clicked.connect(lambda: self.displayInput("6"))
        self.sevenButton.clicked.connect(lambda: self.displayInput("7"))
        self.eightButton.clicked.connect(lambda: self.displayInput("8"))
        self.nineButton.clicked.connect(lambda: self.displayInput("9"))
        self.decimalButton.clicked.connect(lambda: self.displayInput("."))

    def displayInput(self, val):
        """
        Reads input from calculator buttons and displays the value in the screen

        Parameters:
            val (str) - number being read from input button
        Returns:
            None
        """
        #Get data that is currently in the calculator display
        currentData = self.outputLabel.text()
        #If the value is zero, simply display the new input
        if currentData == "0":
            self.outputLabel.setText(val)
        else:
            #Otherwise, add the new input to the previously existing data
            self.outputLabel.setText(currentData + val)

def main():
    app = QApplication(sys.argv)
    window = CalcGUI()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
