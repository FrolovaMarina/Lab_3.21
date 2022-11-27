import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from encryption import*


class UiEntry(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(UiEntry, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(426, 459)
        Dialog.setStyleSheet("background-color: rgb(158, 78, 255)")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(39, 30, 351, 401))
        self.frame.setStyleSheet("background-color: rgb(223, 196, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 10, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 36, 103);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(50, 90, 251, 31))
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 150, 251, 31))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(100, 330, 151, 23))
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.add_functions()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Регистрация / Авторизация:  "))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "ФИО "))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Пароль "))
        self.pushButton.setText(_translate("Dialog", "Войти: "))

    def add_functions(self):
        self.pushButton.clicked.connect(self.method_1)

    def method_1(self):
        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Введите ФИО и пароль")
            error.setStandardButtons(QMessageBox.Ok)

            error.exec()
        else:
            encoded_txt = xtea_encode(self.lineEdit.text() + self.lineEdit_2.text())
            new_file = open("file.txt", "wb")
            new_file.write(encoded_txt)
            self.openDialog()

    def openDialog(self):
        self.hide()
        self.dialog_1 = Work_2()
        self.dialog_1.show()


class UiDescription(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(UiDescription, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, MainWindow_1):
        MainWindow_1.setObjectName("Страница личного кабинета")
        MainWindow_1.resize(550, 807)
        MainWindow_1.setStyleSheet("background-color: rgb(231, 225, 255)")
        self.pushButton = QtWidgets.QPushButton(MainWindow_1)
        self.pushButton.setGeometry(QtCore.QRect(20, 270, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(159, 140, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(MainWindow_1)
        self.label.setGeometry(QtCore.QRect(20, 40, 101, 21))
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(MainWindow_1)
        self.textEdit.setGeometry(QtCore.QRect(20, 70, 501, 192))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textBrowser_2 = QtWidgets.QTextBrowser(MainWindow_1)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 310, 501, 191))
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(MainWindow_1)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 550, 501, 191))
        self.textBrowser_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_2 = QtWidgets.QLabel(MainWindow_1)
        self.label_2.setGeometry(QtCore.QRect(200, 20, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow_1)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 510, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(159, 140, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_exit = QtWidgets.QPushButton(MainWindow_1)
        self.pushButton_exit.setGeometry(QtCore.QRect(230, 760, 81, 31))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("background-color: rgb(159, 140, 255);")
        self.pushButton_exit.setObjectName("pushButton_3")

        self.retranslateUi(MainWindow_1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_1)

        self.add_functions()

    def retranslateUi(self, MainWindow_1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_1.setWindowTitle(_translate("MainWindow_1", "MainWindow_1"))
        self.pushButton.setText(_translate("MainWindow_1", "Выполнить шифрование "))
        self.label.setText(_translate("MainWindow_1", "Введите текст: "))
        self.label_2.setText(_translate("MainWindow_1", "Личный кабинет "))
        self.pushButton_2.setText(_translate("MainWindow_1", "Расшифровка "))
        self.pushButton_exit.setText(_translate("MainWindow_1", "Выйти "))

    def add_functions(self):
        self.pushButton.clicked.connect(self.method_2)

    def method_2(self):
        encoded2_txt = xtea_encode(self.textEdit.toPlainText())
        new_file = open("file.txt", "ab")
        new_file.write(encoded2_txt)
        self.textBrowser_2.append(str(encoded2_txt))
        self.pushButton_2.clicked.connect(self.method_3)

    def method_3(self):
        decoded2_txt = xtea_decode(self.textEdit.toPlainText())
        self.textBrowser_3.append(decoded2_txt)


class UiExit(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(UiExit, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, MainWindow_2):
        MainWindow_2.setObjectName("Dialog")
        MainWindow_2.resize(400, 300)
        MainWindow_2.setStyleSheet("background-color: rgb(231, 225, 255)")
        self.textBrowser = QtWidgets.QTextBrowser(MainWindow_2)
        self.textBrowser.setGeometry(QtCore.QRect(30, 80, 331, 111))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textEdit")
        self.textBrowser.append("Выполнение программы завершено. Вы можете перейти на главную страницу.")
        self.pushButton_to_start = QtWidgets.QPushButton(MainWindow_2)
        self.pushButton_to_start.setGeometry(QtCore.QRect(80, 230, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton_to_start.setFont(font)
        self.pushButton_to_start.setStyleSheet("background-color: rgb(159, 140, 255)")
        self.pushButton_to_start.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(MainWindow_2)
        self.label.setGeometry(QtCore.QRect(130, 30, 121, 21))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(MainWindow_2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_2)

    def retranslateUi(self, MainWindow_2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_2.setWindowTitle(_translate("MainWindow_2", "MainWindow_2"))
        self.pushButton_to_start.setText(_translate("MainWindow_2", "Перейти на главную страницу "))
        self.label.setText(_translate("MainWindow_2", "Экран выхода "))


class Work_2(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.ui = UiDescription()
        self.ui.setupUi(self)
        self.ui.pushButton_exit.clicked.connect(self.openExit)

    def openExit(self):
        self.hide()
        self.dialog_2 = Work_3()
        self.dialog_2.show()


class Work_3(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.ui = UiExit()
        self.ui.setupUi(self)
        self.ui.pushButton_to_start.clicked.connect(self.openExit)

    def openExit(self):
        self.hide()
        self.dialog_3 = UiEntry()
        self.dialog_3.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UiEntry()
    window.show()
    sys.exit(app.exec_())
