from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_Dialog6(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 600)
        self.grafik_input = QtWidgets.QLabel(Dialog)
        self.grafik_input.setGeometry(QtCore.QRect(0, 0, 1081, 641))
        self.grafik_input.setText("")
        self.grafik_input.setPixmap(QtGui.QPixmap("graph.png"))
        self.grafik_input.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.grafik_input.setPixmap(QtGui.QPixmap("graph.png"))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Frafik!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog6 = QtWidgets.QDialog()
    ui = Ui_Dialog6()
    ui.setupUi(Dialog6)
    Dialog6.show()
    sys.exit(app.exec_())
