from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(623, 700)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                             "")
        self.k_koeficent = QtWidgets.QLineEdit(Dialog)
        self.k_koeficent.setGeometry(QtCore.QRect(210, 50, 391, 21))
        self.k_koeficent.setStyleSheet("color: rgb(24, 255, 78);\n"
                                       "")
        self.k_koeficent.setObjectName("k_koeficent")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 10, 241, 16))
        self.label.setStyleSheet("font: italic 14pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 191, 31))
        self.label_2.setStyleSheet("font: italic 9pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 201, 51))
        self.label_3.setStyleSheet("font: italic 9pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.r_cherecter = QtWidgets.QLineEdit(Dialog)
        self.r_cherecter.setGeometry(QtCore.QRect(210, 110, 391, 21))
        self.r_cherecter.setStyleSheet("color: rgb(24, 255, 78);\n"
                                       "")
        self.r_cherecter.setObjectName("r_cherecter")
        self.btn_otv_1 = QtWidgets.QPushButton(Dialog)
        self.btn_otv_1.setGeometry(QtCore.QRect(430, 160, 171, 21))
        self.btn_otv_1.setStyleSheet("background-color: rgb(241, 241, 0);\n"
                                     "font: italic 9pt \"Arial\";\n"
                                     "color: rgb(0, 185, 185);")
        self.btn_otv_1.setObjectName("btn_otv_1")
        self.btn_otv_1.clicked.connect(self.test)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 441, 21))
        self.label_4.setStyleSheet("font: italic 11pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.c_active = QtWidgets.QLineEdit(Dialog)
        self.c_active.setGeometry(QtCore.QRect(200, 300, 391, 21))
        self.c_active.setStyleSheet("color: rgb(24, 255, 78);\n"
                                    "")
        self.c_active.setObjectName("c_active")
        self.k_koef_2 = QtWidgets.QLineEdit(Dialog)
        self.k_koef_2.setGeometry(QtCore.QRect(200, 350, 391, 21))
        self.k_koef_2.setStyleSheet("color: rgb(24, 255, 78);\n"
                                    "")
        self.k_koef_2.setObjectName("k_koef_2")
        self.f_koef = QtWidgets.QLineEdit(Dialog)
        self.f_koef.setGeometry(QtCore.QRect(200, 400, 391, 21))
        self.f_koef.setStyleSheet("color: rgb(24, 255, 78);\n"
                                  "")
        self.f_koef.setObjectName("f_koef")
        self.m_weight = QtWidgets.QLineEdit(Dialog)
        self.m_weight.setGeometry(QtCore.QRect(200, 500, 391, 21))
        self.m_weight.setStyleSheet("color: rgb(24, 255, 78);\n"
                                    "")
        self.m_weight.setObjectName("m_weight")
        self.d_increase = QtWidgets.QLineEdit(Dialog)
        self.d_increase.setGeometry(QtCore.QRect(200, 450, 391, 21))
        self.d_increase.setStyleSheet("color: rgb(24, 255, 78);\n"
                                      "")
        self.d_increase.setObjectName("d_increase")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 250, 371, 16))
        self.label_5.setStyleSheet("font: italic 14pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 290, 171, 31))
        self.label_6.setStyleSheet("font: italic 9pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 340, 171, 31))
        self.label_7.setStyleSheet("font: italic 9pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 380, 171, 41))
        self.label_8.setStyleSheet("font: italic 9pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 440, 151, 31))
        self.label_9.setStyleSheet("font: italic 9pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 490, 151, 31))
        self.label_10.setStyleSheet("font: italic 9pt \"Arial\";")
        self.label_10.setObjectName("label_10")
        self.first_otv = QtWidgets.QLabel(Dialog)
        self.first_otv.setGeometry(QtCore.QRect(470, 210, 71, 31))
        self.first_otv.setStyleSheet("font: italic 9pt \"Arial\";")
        self.first_otv.setText("")
        self.first_otv.setObjectName("first_otv")
        self.btn_otv_2 = QtWidgets.QPushButton(Dialog)
        self.btn_otv_2.setGeometry(QtCore.QRect(430, 550, 171, 21))
        self.btn_otv_2.setStyleSheet("background-color: rgb(241, 241, 0);\n"
                                     "font: italic 10pt \"Arial\";\n"
                                     "color: rgb(0, 185, 185);")
        self.btn_otv_2.setObjectName("btn_otv_2")
        self.btn_otv_2.clicked.connect(self.otv_2_finish)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(20, 610, 351, 21))
        self.label_12.setStyleSheet("font: italic 12pt \"Arial\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(550, 210, 21, 31))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(370, 610, 71, 31))
        self.label_14.setStyleSheet("font: italic 9pt \"Arial\";")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(440, 610, 21, 31))
        self.label_15.setObjectName("label_15")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def test(self):
        global result
        input_walue = float(self.k_koeficent.text())
        input_value = float(self.r_cherecter.text())
        result = input_walue * input_value
        self.first_otv.setText(str(result))

    def otv_2_finish(self):
        global result2
        c = float(self.c_active.text())
        k = float(self.k_koef_2.text())
        f = float(self.f_koef.text())
        d = float(self.d_increase.text())
        m = float(self.m_weight.text())
        result2 = (c * k * f * d)/ m
        self.label_14.setText(str(result2))



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Ионизирующяя радиация:"))
        self.label_2.setText(_translate("Dialog", "K - коэфицент приоброзования \n"
                                                  "энергии излучения с дозой"))
        self.label_3.setText(_translate("Dialog", "R - количества характеристик \n"
                                                  "излучения, полученная \n"
                                                  "при помощи дозиметра"))
        self.btn_otv_1.setText(_translate("Dialog", "Вывести ответ:"))
        self.label_4.setText(_translate("Dialog", "Ответ: Доза ионизирующей радиации измеряемая равняется"))
        self.label_5.setText(_translate("Dialog", "Формула нахождение радиации в земле:"))
        self.label_6.setText(_translate("Dialog", "С - Активность образца \n"
                                                  "измеряемый в беккелерах"))
        self.label_7.setText(_translate("Dialog", "К - коэфицент пересчета \n"
                                                  "зависищийот радионуклида "))
        self.label_8.setText(_translate("Dialog", "F - коэфицентпересечения \n"
                                                  "учитывая эффекты \n"
                                                  "фильтрации"))
        self.label_9.setText(_translate("Dialog", "D- Плотность образца \n"
                                                  "(г/см^3)"))
        self.label_10.setText(_translate("Dialog", "M - Масса образца,\n"
                                                   " измеряемая в граммах"))
        self.btn_otv_2.setText(_translate("Dialog", "Вывести ответ:"))
        self.label_12.setText(_translate("Dialog", "Ответ: Доза радиации на земле равняется"))
        self.label_13.setText(_translate("Dialog", "gy"))
        self.label_15.setText(_translate("Dialog", "Bq"))

    def first_otv_(self, text):
        self.result = text

    def second_otv_(self, text):
        self.result2 = text

if __name__ == "__main__":
     import sys
     app = QtWidgets.QApplication(sys.argv)
     Dialog = QtWidgets.QDialog()
     ui = Ui_Dialog()
     ui.setupUi(Dialog)
     Dialog.show()
     Dialog.setWindowTitle('Самостоятельное вычесление')
     sys.exit(app.exec_())
