import conf
import sys
import rungame
from api import *
from PyQt6 import QtWidgets, uic
server = conf.server
#online = isOnline()

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("launcher.ui")
window.show()

window.progressBar.setValue(0)
window.pushButton.clicked.connect(rungame.play)


app.exec()