import sys
from PyQt5.QtWidgets import * #import section

app = QApplication(sys.argv) #create application
dlgMain = QMainWindow() #create main GUI window
dlgMain.setWindowTitle('First GUI') #Window name
dlgMain.show()  #Show the GUI

sys.exit(app.exec_()) #App run