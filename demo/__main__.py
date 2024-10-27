import sys

from PyQt5 import QtWidgets
from VideoPreview.videoPreview_main import VideoPreview
def __main__():
    app = QtWidgets.QApplication(sys.argv)
    app.setObjectName("InspSys")
    win = VideoPreview()
    win.show()
    win.raise_()
    sys.exit(app.exec_())
if __name__ == '__main__':
    __main__()

