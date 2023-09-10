import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from radiation import Ui_MainWindow
from hend import Ui_Dialog


app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def open_window():
    global Dialog
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.setWindowTitle('Самостоятельное вычесление')



ui.calculate.clicked.connect(open_window)
sys.exit(app.exec_())