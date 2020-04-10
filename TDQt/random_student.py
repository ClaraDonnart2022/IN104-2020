#!/usr/bin/env python3


# Documentation:
#  - the one from PySide is nicely formatted, and applies (almost) to PySide2:
#    https://srinikom.github.io/pyside-docs/PySide/QtGui/QWidget.html#
#  - the official one: 
#    https://doc.qt.io/qtforpython/quickstart.html
#  - this course seems nice (in French):
#    https://courspython.com/interfaces.html


import sys
import random


from PySide2 import QtCore, QtGui, QtWidgets

# TODO: import students, group and github link from Gr8-sous-groupes.md
groups = { 1: ['Alice', 'Bob', 'Charlie'],
           2: ['David', 'Eve'],
           3: ['Frank', 'Grace'],
           4: ['Heidi', 'Ivan'],
           5: ['Judy', 'Mallory'],
           6: ['Olivia', 'Peggy'],
           7: ['Rupert', 'Sybil'],
           8: ['Ted', 'Victor'] }

students = sum([v for v in groups.values()], [])
# also possible: students = itertools.chain.from_iterable(v for v in groups.values())

#print(list(students), groups)

# TODO: open the github link with: PySide.QtGui.QDesktopServices.openUrl(url)

class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        # bizarre : pyside2-uic ne marche plus (?), je recopie ce que donne un pyside-uic
        # d'avoir installe PySide2 _et_ PyQt5 n'etait peut-etre pas une bonne idee...
        # en principe, les lignes qui suivent (hormis clicked.connect) sont importees du fichier ui que qt-designer a cree.
        Form = self
        Form.resize(600, 300)
        
        self.randomStudentButton = QtWidgets.QPushButton(Form)
        self.randomStudentButton.setGeometry(QtCore.QRect(40, 50, 111, 27))
        self.randomStudentButton.setText("student")
        self.randomStudentButton.clicked.connect(self.randomStudentClicked)
        
        self.randomGroupButton = QtWidgets.QPushButton(Form)
        self.randomGroupButton.setGeometry(QtCore.QRect(190, 50, 121, 27))
        self.randomGroupButton.setText("group")
        self.randomGroupButton.clicked.connect(self.randomGroupClicked)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 100, 400, 31))

        self.urlButton = QtWidgets.QPushButton(Form)
        self.urlButton.setGeometry(QtCore.QRect(130, 200, 400, 31))
        self.urlButton.clicked.connect(self.urlButtonClicked)

    def randomStudentClicked(self):
        pick = random.choice(students)
        self.label.setText(pick)
        url = 'https://github.com/'
        self.urlButton.setText(url)

    def urlButtonClicked(self):
        url = self.urlButton.text()
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))

    def randomGroupClicked(self):
        pick = random.choice(list(groups.items()))
        self.label.setText(str(pick))
       

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    myapp = MyMainWindow()
    myapp.show()
    sys.exit(app.exec_())
