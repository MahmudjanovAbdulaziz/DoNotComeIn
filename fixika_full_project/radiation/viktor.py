import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton, QPushButton, QMessageBox

class Quiz(QWidget):
    def _init_(self):
        super()._init_()

        self.setWindowTitle('Викторина')
        self.setGeometry(200, 200, 400, 300)

        self.question_num = 0
        self.score = 0

        self.questions = {
            'Вопрос 1': {'Вариант 1': False, 'Вариант 2': True, 'Вариант 3': False},
            'Вопрос 2': {'Вариант 1': False, 'Вариант 2': False, 'Вариант 3': True},
            'Вопрос 3': {'Вариант 1': True, 'Вариант 2': False, 'Вариант 3': False},
            'Вопрос 4': {'Вариант 1': False, 'Вариант 2': True, 'Вариант 3': False},
            'Вопрос 5': {'Вариант 1': False, 'Вариант 2': False, 'Вариант 3': True}
        }

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        self.question = QLabel('Вопрос')
        vbox.addWidget(self.question)

        self.radio_button_1 = QRadioButton('Вариант 1')
        vbox.addWidget(self.radio_button_1)

        self.radio_button_2 = QRadioButton('Вариант 2')
        vbox.addWidget(self.radio_button_2)

        self.radio_button_3 = QRadioButton('Вариант 3')
        vbox.addWidget(self.radio_button_3)

        hbox = QHBoxLayout()

        self.prev_button = QPushButton('Назад')
        self.prev_button.setEnabled(False)
        hbox.addWidget(self.prev_button)

        self.next_button = QPushButton('Далее')
        hbox.addWidget(self.next_button)

        vbox.addLayout(hbox)

        self.next_button.clicked.connect(self.checkAnswer)
        self.prev_button.clicked.connect(self.showPrevQuestion)

        self.setLayout(vbox)

        self.showQuestion()

    def showQuestion(self):
        question = list(self.questions.keys())[self.question_num]
        self.question.setText(question)

        options = self.questions[question]
        self.radio_button_1.setText(list(options.keys())[0])
        self.radio_button_2.setText(list(options.keys())[1])
        self.radio_button_3.setText(list(options.keys())[2])

    def showPrevQuestion(self):
        self.question_num -= 1
        self.prev_button.setEnabled(self.question_num != 0)
        self.next_button.setText('Далее')
        self.showQuestion()

    def checkAnswer(self):
        selected = None

        if self.radio_button_1.isChecked():
            selected = self.radio_button_1.text()
        elif self.radio_button_2.isChecked():
            selected = self.radio_button_2.text()
        elif self.radio_button_3.isChecked():
            selected = self.radio_button_3.text()

        if selected is None:
            QMessageBox.warning(self, 'Ошибка', 'Выберите ответ')
            return

        correct = list(self.questions.values())[self.question_num][selected]

        if correct:
            self.score += 1

        def showResult(self):
            vbox = QVBoxLayout()

            result_label = QLabel(f'Вы набрали {self.score} из {len(self.questions)}')
            vbox.addWidget(result_label)

            hbox = QHBoxLayout()

            self.retry_button = QPushButton('Попробовать еще раз')
            hbox.addWidget(self.retry_button)

            self.quit_button = QPushButton('Выйти')
            hbox.addWidget(self.quit_button)

            vbox.addLayout(hbox)

            self.setLayout(vbox)

            self.retry_button.clicked.connect(self.retryQuiz)
            self.quit_button.clicked.connect(self.quitQuiz)

        def retryQuiz(self):
            self.question_num = 0
            self.score = 0
            self.prev_button.setEnabled(False)
            self.next_button.setText('Далее')
            self.showQuestion()

        def quitQuiz(self):
            self.close()

        def showQuestion(self):
            question = list(self.questions.keys())[self.question_num]
            self.question.setText(question)

            options = self.questions[question]
            self.radio_button_1.setText(list(options.keys())[0])
            self.radio_button_2.setText(list(options.keys())[1])
            self.radio_button_3.setText(list(options.keys())[2])

        def showPrevQuestion(self):
            self.question_num -= 1
            self.prev_button.setEnabled(self.question_num != 0)
            self.next_button.setText('Далее')
            self.showQuestion()

        def checkAnswer(self):
            selected = None

            if self.radio_button_1.isChecked():
                selected = self.radio_button_1.text()
            elif self.radio_button_2.isChecked():
                selected = self.radio_button_2.text()
            elif self.radio_button_3.isChecked():
                selected = self.radio_button_3.text()

            if selected is None:
                QMessageBox.warning(self, 'Ошибка', 'Выберите ответ')
                return

            correct = list(self.questions.values())[self.question_num][selected]

            if correct:
                self.score += 1

            self.question_num += 1
            self.prev_button.setEnabled(True)

            if self.question_num == len(self.questions):
                self.showResult()
            else:
                self.showQuestion()

if __name__ == '_main_':
    app = QApplication(sys.argv)
    quiz = Quiz()
    quiz.show()
    sys.exit(app.exec_())