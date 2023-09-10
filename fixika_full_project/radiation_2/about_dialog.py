from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_about_radiation(object):
    def setupUi(self, about_radiation):
        about_radiation.setObjectName("about_radiation")
        about_radiation.resize(1097, 616)
        about_radiation.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(7, 219, 173, 1), stop:0.427447 rgba(7, 219, 35, 1), stop:1 rgba(7, 219, 184, 1));")
        self.frame = QtWidgets.QFrame(about_radiation)
        self.frame.setGeometry(QtCore.QRect(60, 0, 941, 621))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(16, 2, 921, 141))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(242, 196, 29, 1), stop:0.427447 rgba(57, 242, 29, 1), stop:1 rgba(29, 242, 182, 1));\n"
"border-radius:17px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 921, 121))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(242, 196, 29, 1), stop:0.427447 rgba(57, 242, 29, 1), stop:1 rgba(29, 242, 182, 1));\n"
"border-radius:17px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 921, 181))
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(242, 196, 29, 1), stop:0.427447 rgba(57, 242, 29, 1), stop:1 rgba(29, 242, 182, 1));\n"
"border-radius:17px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 440, 921, 71))
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(242, 196, 29, 1), stop:0.427447 rgba(57, 242, 29, 1), stop:1 rgba(29, 242, 182, 1));\n"
"border-radius:17px;")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(about_radiation)
        QtCore.QMetaObject.connectSlotsByName(about_radiation)

    def retranslateUi(self, about_radiation):
        _translate = QtCore.QCoreApplication.translate
        about_radiation.setWindowTitle(_translate("about_radiation", "about-dialog"))
        self.label.setText(_translate("about_radiation", "Радиа́ция (от лат. radiātiō «излучение»):\n"
"\n"
"Радиация — ионизирующее излучение;\n"
"Адаптивная радиация в биологии — явление различной адаптации родственных групп организмов к изменениям условий окружающей среды, выступающее как \n"
"одна из основных причин дивергенции;\n"
"Солнечная радиация — излучение Солнца (электромагнитной и корпускулярной природы).Эволюционная радиация в биологии — сравнительно быстрое\n"
"(в геологических масштабах) и массовое возрастание таксономического разнообразия или морфологических отличий видов вследствие \n"
"адаптивных изменений или открывшегося ранее недоступного экопространства.extLabel"))
        self.label_2.setText(_translate("about_radiation", "Ионизи́рующее излуче́ние (неточный синоним с более широким значением — радиация) — потоки фотонов и других элементарных частиц или атомных ядер, \n"
"способные ионизировать вещество.\n"
"\n"
"К ионизирующему излучению не относятся видимый свет и ультрафиолетовое излучение, которые в отдельных случаях могут ионизировать вещество. \n"
"Инфракрасное излучение и излучение радиодиапазонов не являются ионизирующими, поскольку их энергии недостаточно для ионизации атомов \n"
"и молекул в основном состоянии[1][2][3][4][5]."))
        self.label_3.setText(_translate("about_radiation", "История\n"
"Краски с использованием урановых и других радиоактивных материалов применялись еще задолго до начала нашей эры, но испускаемое ими ионизирующее \n"
"излучение было так незначительно, что его не могли заметить.\n"
"\n"
"Первым обнаруженным видом ионизирующего излучения стали катодные лучи (потоки электронов, ускоряемых в вакуумной трубке высоким напряжением), \n"
"открытые в 1860-х годах. Затем были открыты рентгеновские лучи (Вильгельм Рентген, 1895). В 1896 году Анри Беккерель обнаружил ещё один вид \n"
"ионизирующего излучения — невидимые лучи, испускаемые ураном, проходящие сквозь плотное непрозрачное вещество и засвечивающие фотоэмульсию \n"
"(в современной терминологии — гамма-излучение)[6][7]. В результате дальнейшего исследования явления радиоактивности было обнаружено \n"
"(Эрнест Резерфорд, 1899), что в результате радиоактивного распада испускаются альфа-, бета- и гамма-лучи, отличающиеся по ряду свойств, в частности, по электрическому заряду. \n"
"Впоследствии были обнаружены и другие виды ионизирующей радиации, возникающие при радиоактивном распаде ядер: позитроны, конверсионные и \n"
"оже-электроны, нейтроны, протоны, осколки деления, кластеры (лёгкие ядра, испускаемые при кластерном распаде). В 1911—1912 годах были открыты космические лучи."))
        self.label_4.setText(_translate("about_radiation", "Цепочка ядерных превращений\n"
"В процессе ядерного распада или синтеза возникают новые нуклиды, которые также могут быть нестабильны. В результате \n"
"возникает цепочка ядерных превращений. Каждое превращение имеет свою вероятность и свой набор ионизирующих излучений. В результате \n"
"интенсивность и характер излучений радиоактивного источника может значительно меняться со временем."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    about_radiation = QtWidgets.QDialog()
    ui = Ui_about_radiation()
    ui.setupUi(about_radiation)
    about_radiation.show()
    sys.exit(app.exec_())
