import sys, os
from PyQt5 import QtGui, QtCore
from GUI_ui import *

class Ui_Test(QtWidgets.QMainWindow, Ui_Test):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        self.lines.setText("1")
        self.analize.clicked.connect(self.analizeText)

    def analizeText(self):
        my_name = self.name.text()
        my_text = self.text.text()
        my_lines = self.lines.text()
        if my_name != "" and my_text != "" and my_lines != "": 
            vowels = 'aeiou'
            vowel, consonant = 0, 0
            for char in my_text.lower():
                if char.isalpha():
                    if char in vowels: vowel += 1
                    else: consonant += 1
            self.vowels.setText(str(vowel * int(my_lines)))
            self.consonants.setText(str(consonant * int(my_lines)))
            writeFile(self, my_name, my_text, my_lines)
        else: showDialog(self, "Alert", "Please fill the boxes marked with a *")

def writeFile(self, name, text, lines):
    file = open(f"{name}.txt", "w")
    for i in range(int(lines)):
        file.write(f"{text}\n")
    file.close()
    showDialog(self, "Done", "File created successfully!")

def showDialog(self, title, msg):
    dlg = QtWidgets.QDialog(self)
    dlg.setWindowTitle(title)
    dlg.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok)
    dlg.buttonBox.accepted.connect(dlg.accept)
    dlg.layout = QtWidgets.QVBoxLayout()
    message = QtWidgets.QLabel(msg)
    dlg.layout.addWidget(message)
    dlg.layout.addWidget(dlg.buttonBox)
    dlg.setLayout(dlg.layout)
    dlg.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_Test()
    window.show()
    app.exec_()