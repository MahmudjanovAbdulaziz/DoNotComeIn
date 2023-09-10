import sys
from PyQt5.QtWidgets import * #import section

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 300)

        self.btn = QPushButton('Show Message', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)


    def evt_btn_clicked(self):
        # res = QMessageBox.information(self, 'Disk Full', 'Your disk drive is almoust full')
        # print(res)
        # res_2 = QMessageBox.warning(self, 'Disk Full', 'Your disk drive is almoust full')
        # # res_3 = QMessageBox.critical(self, 'Disk Full', 'Your disk drive is almoust full')
        # res_4 = QMessageBox.question(self, 'Disk Full', 'Your disk drive is almoust full')
        # if res_4 == QMessageBox.Yes:
        #     QMessageBox.information(self, '', 'You`ve clicked yes button')
        # elif res_4 == QMessageBox.No:
        #     QMessageBox.information(self, '', 'You`ve clicked no button')
        msg_disk = QMessageBox()
        msg_disk.setText('You hard drive is allmoust full')
        msg_disk.setDetailedText("Please free up disk space")
        msg_disk.setIcon(QMessageBox.Information)
        msg_disk.setWindowTitle('Fule drive')
        msg_disk.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg_disk.exec_()





if __name__ == "__main__":
    app = QApplication(sys.argv) # create run configuration
    dlgMain = DlgMain() #Create Main Gui Window
    dlgMain.show()  #sghow gui
    sys.exit(app.exec_())  # execute the run