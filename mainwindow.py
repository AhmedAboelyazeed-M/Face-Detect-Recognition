import sys

from out_window import *


class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        loadUi("mainwindow.ui", self)

        self.runButton.clicked.connect(self.runSlot)

        self._new_window = None
        self.Videocapture_ = None

    def refreshAll(self):
        """
        Set the text of lineEdit once it's valid
        """
        # self.Videocapture_ = "0"
        self.Videocapture_ = "1"

    # @pyqtSlot()
    def runSlot(self):
        """
        Called when the user presses the Run button
        """
        print("program started..")
        self.refreshAll()
        # print(self.Videocapture_)
        ui.hide()  # hide the main window
        self.outputWindow_()  # Create and open new output window

    def outputWindow_(self):
        """
        Created new window for the output of the video in GUI
        """
        self._new_window = Ui_OutputDialog()
        self._new_window.show()
        self._new_window.startVideo(self.Videocapture_)
        print("camera started....")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
