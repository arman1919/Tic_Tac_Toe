import sys

from PyQt6.QtWidgets import QApplication, QDialog
 
from tik_tak import Ui_Dialog


class MyDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.setupUi(self)
        self.setFixedSize(600, 600)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec())
