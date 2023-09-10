from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog4(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(997, 646)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1081, 641))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image9.jpg"))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "graf_1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog4 = QtWidgets.QDialog()
    ui = Ui_Dialog4()
    ui.setupUi(Dialog4)
    Dialog4.show()
    sys.exit(app.exec_())
