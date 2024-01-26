from PyQt6 import QtCore, QtGui, QtWidgets

from PyQt6.QtWidgets import QLineEdit
import XO


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("TIC TAC TOE")
        Dialog.resize(600, 600)
        
        self.buttons =  []
        
        self.pushButton_1 = QtWidgets.QPushButton(parent=Dialog)
        self.buttons.append(self.pushButton_1)
        self.pushButton_1.setGeometry(QtCore.QRect(60, 160, 100, 100))
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton_1")
        
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.buttons.append(self.pushButton_2)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 160, 100, 100))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.buttons.append(self.pushButton_3)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 160, 100, 100))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.buttons.append(self.pushButton_4)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 300, 100, 100))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.pushButton_5 = QtWidgets.QPushButton(parent=Dialog)
        self.buttons.append(self.pushButton_5)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 300, 100, 100))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        
        self.pushButton_6 = QtWidgets.QPushButton(parent=Dialog)
        self.buttons.append(self.pushButton_6)
        self.pushButton_6.setGeometry(QtCore.QRect(420, 300, 100, 100))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.pushButton_7 = QtWidgets.QPushButton(parent=Dialog)
        self.buttons.append(self.pushButton_7)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 440, 100, 100))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        
        self.pushButton_8 = QtWidgets.QPushButton(parent=Dialog)
        self.buttons.append(self.pushButton_8)
        self.pushButton_8.setGeometry(QtCore.QRect(240, 440, 100, 100))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        
        self.pushButton_9 = QtWidgets.QPushButton(parent=Dialog)
        self.buttons.append(self.pushButton_9)
        self.pushButton_9.setGeometry(QtCore.QRect(420, 440, 100, 100))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        
        self.display0 = QtWidgets.QTextBrowser(parent=Dialog)
        self.display0.setGeometry(QtCore.QRect(70, 0, 450, 40))
        self.display0.setObjectName("display0")
        self.display = QtWidgets.QTextBrowser(parent=Dialog)
        self.display.setGeometry(70, 40, 450, 40)
        self.display.setObjectName("display")        
       
        self.pushButton_10 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(540, 540, 51, 51))
        self.pushButton_10.setText("")
        icon = QtGui.QIcon.fromTheme("edit-undo")
        self.pushButton_10.setIcon(icon)
        self.pushButton_10.setObjectName("pushButton_10")
        
        self.ok_button = QtWidgets.QPushButton(parent=Dialog)
        self.ok_button.setGeometry(550,90,40,40)
        self.ok_button.setText("OK")
        self.ok_button.clicked.connect(self.clik_ok)
        
        self.text_input = QLineEdit(parent=Dialog)
        self.text_input.setPlaceholderText("Enter name player 1")
        self.text_input.setGeometry(70,90,450,40)
        
        self.font = QtGui.QFont()
        self.font.setPointSize(80)
        
        self.playaer1 = XO.Player(None,"X")
        self.playaer2 = XO.Player(None,"O")
        
        
        
            
        
        self.pushButton_1.clicked.connect(lambda: self.on_button_click(self.pushButton_1))
        self.pushButton_2.clicked.connect(lambda: self.on_button_click(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.on_button_click(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.on_button_click(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.on_button_click(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.on_button_click(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: self.on_button_click(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: self.on_button_click(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda: self.on_button_click(self.pushButton_9))
        
        
        for buton in  self.buttons:
            buton.symbol = ""
            buton.setFont(self.font)
            
        self.symbol = "X"
        
        self.count_step = 0
        
        
        self.pushButton_10.clicked.connect(self.all_restart)
        self.board = XO.Board()
       
        
        
       
        
    
        self.font_D = QtGui.QFont()

        self.font_D.setPointSize(15)
        
        self.display0.setFont(self.font_D)
        self.display.setFont(self.font_D)
        
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.curent_palyer = self.playaer1
       
    def clik_ok(self):
        
        if self.playaer1.name and self.playaer2.name:
            return
        
        if self.playaer1.name == None:
            self.playaer1.name = self.text_input.text()
            self.text_input.clear()
            self.text_input.setPlaceholderText("Enter name player 2")
        else:
            self.playaer2.name = self.text_input.text()
            self.text_input.clear()
            self.text_input.setPlaceholderText("")
            
            self.display.setText(f"Step {self.playaer1.name} - {self.playaer1.sybol}")
            
            
            
            

    
    def on_button_click(self, button):
        
        if  not self.playaer1.name or not self.playaer2.name:
            self.display.setText("Enter player name !")
            return
        
        self.display0.setText("")
        
        if button.text() == "":
            self.count_step += 1
            
            if self.curent_palyer.sybol == "X":
                button.setStyleSheet('color: rgb(255, 0, 0);')
            else:
                button.setStyleSheet('color: rgb(0, 0, 255);')
            
            button.setText(self.curent_palyer.sybol)
            
            
            self.board.press_symbol(int(button.objectName()[-1]),self.curent_palyer.sybol)
            if self.board.check_winner():
                self.display0.setText(f"Win flayer {self.curent_palyer.name}")
                self.restart()
                return

                
                
            
            if self.count_step == 9:
                self.display0.setText(f"DRAW")
                self.restart()
                return
                
            self.curent_palyer = self.playaer1 if self.curent_palyer.sybol == "O" else self.playaer2
            
            self.display.setText(f"Step playe {self.curent_palyer.name}")
            
            
        
    def restart(self):
        self.display.setText(f"Step player {self.curent_palyer.name}")
        self.count_step = 0
        self.board.restart()
        
        for button in self.buttons:
            button.setText("")
    
    def all_restart(self):
        self.playaer1.name = None
        self.playaer2.name = None
        self.text_input.setPlaceholderText("Enter name player 1")
        self.count_step = 0
        self.board.restart()
        self.display0.setText("")
        self.display.setText("")
        for button in self.buttons:
            button.setText("")
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("TIC TAC TOE", "TIC TAC TOE"))



