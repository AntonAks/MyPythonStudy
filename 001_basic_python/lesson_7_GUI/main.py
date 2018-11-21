import sys
import os
from PyQt5 import QtWidgets


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()

window.setWindowTitle("My first test with PyQt5")
window.resize(300, 70)
label = QtWidgets.QLabel("<center> Hello World ! </center>")

""" Buttons """
# btnAction = QtWidgets.QPushButton("&Start my procedure")
btnQuit = QtWidgets.QPushButton("&Close window")

""" Container """
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)

""" window settings """
window.setLayout(vbox)

""" buttons actions """
# btnAction.clicked.connect(os.system("C:\\Users\\Anton Aksynov\\Desktop\\pass.py"))
btnQuit.clicked.connect(app.quit)

"""  """
window.show()
sys.exit(app.exec_())


print(QtWidgets.qApp.argv())
