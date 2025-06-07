import operator
import pathlib
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class CalcGUI(QMainWindow):
    def __init__(self):
        """
        Class representing the different elements of the GUI for this calculator application
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

        #Defining input from operation buttons
        self.addButton.clicked.connect(lambda: self.startOperation("+"))
        self.subButton.clicked.connect(lambda: self.startOperation("-"))
        self.multButton.clicked.connect(lambda: self.startOperation("*"))
        self.divButton.clicked.connect(lambda: self.startOperation("/"))

        #Running operation when equals button is clicked
        self.equalButton.clicked.connect(lambda: self.performCalculation())

        #Deleting most recent character when DEL button is clicked
        self.delButton.clicked.connect(lambda: self.deleteChar())

        #Clearing data when clear button is clicked
        self.clearButton.clicked.connect(lambda: self.clearData())

        #Tracking the current data and operation being used to perform a calculation
        self.dataCache = ""
        self.operation = ""

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
        #If a decimal is being added to zero, start input as 0.
        if currentData == "0" and val == ".":
            self.outputLabel.setText("0.")
        #If the value is zero, simply display the new input
        elif currentData == "0":
            self.outputLabel.setText(val) 
        else:
            #Otherwise, add the new input to the previously existing data
            self.outputLabel.setText(currentData + val)

    def deleteChar(self):
        """
        Deletes the last entered character from the input string

        Parameters:
            None
        Returns:
            None
        """
        currentData = self.outputLabel.text()

        #Delete the last entered character if the length of the input string is greater than one
        if len(currentData) > 1:
            self.outputLabel.setText(currentData[:-1])

        #If only one character has been entered, reset the input string
        elif currentData != "0":
            self.outputLabel.setText("0")

    def clearData(self):
        """
        Clears the cache, operation, and current data

        Parameters:
            None
        Returns:
            None
        """
        self.dataCache = ""
        self.operation = ""
        self.outputLabel.setText("0")

    def startOperation(self, op):
        """
        Begins an opration to be performed on the inputed data

        Parameters:
            op (str) - Operation being performed for the current calculation
        Returns:
            None
        """
        #Read in data from calculator display
        data = self.outputLabel.text()

        #Try converting the data to a numerical value
        try:
            self.dataCache = float(data)

            #If conversion is successful, update current operation
            self.operation = op

            #Reset input string
            self.outputLabel.setText("0")

        except ValueError:
            #If that fails, reset values and return an error
            self.clearData()
            self.outputLabel.setText("ERROR")

    def performCalculation(self):
        """
        Performs a calculation based on the currrent input and operation

        Parameters:
            None
        Returns:
            None
        """
        #Only perform calculation if an operation has begun
        if self.operation:
            currentData = self.outputLabel.text()
            try:
                #Try to convert the data currently in the display to a numerical value
                cdVal = float(currentData)

                #Dict containing operations
                ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

                #Perform calculation
                op = ops[self.operation]
                res = round(op(self.dataCache, cdVal), 10)

                #Convert to an int if possible
                if res % 1 == 0:
                    res = int(res)

                #Display the result to the calculater screen
                self.outputLabel.setText(str(res))

            except ValueError:
                #If that fails, reset values and return an error
                self.clearData()
                self.outputLabel.setText("ERROR")

            except ZeroDivisionError:
                #If the user tries to divide by zero, reset values and return an error
                self.clearData()
                self.outputLabel.setText("ERROR")

def main():
    app = QApplication(sys.argv)
    window = CalcGUI()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
