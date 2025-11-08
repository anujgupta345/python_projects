import sys
from PySide6.QtWidgets import QApplication, QDialog
from TwoTextWithTwoButtons import Ui_Form

from WorkWithUI import WorkWithUI

class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form() #took ui variable a member variable and set it to our complete UI from.ui file
        self.ui.setupUi(self) # creates complete UI inside it
       


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainDialog()

    #calling WorkWithUI will make UI class independent of main
    workwithUI =  WorkWithUI(
            window.ui.okPushButton,
            window.ui.resetPushButton,
            window.ui.inputTextEdit,
            window.ui.responseTextEdit,
            window.ui.roleComboBox
        )
    window.show()
    sys.exit(app.exec())
