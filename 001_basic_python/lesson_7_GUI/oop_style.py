from PyQt5 import QtWidgets, QtCore


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.label = QtWidgets.QLabel("<center> Hello World ! </center>")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)

        """ Buttons """
        # btnAction = QtWidgets.QPushButton("&Start my procedure")
        self.btnQuit = QtWidgets.QPushButton("&Close window")

        """ Container """
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)

        self.setLayout(self.vbox)

        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


