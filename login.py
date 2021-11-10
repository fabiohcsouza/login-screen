from PyQt5 import uic,QtWidgets

def show_second_screen():
    first_screen.label_4.setText("")
    user_name = first_screen.lineEdit.text()
    password = first_screen.lineEdit_2.text()
    if user_name == "oh_binho" and password == "1d6477":
        first_screen.close()
        second_screen.show()
    else: 
        first_screen.label_4.setText("Incorrect login details!")

def logout():
    second_screen.close()
    first_screen.show()

app=QtWidgets.QApplication([])
first_screen=uic.loadUi("login-first-screen.ui")
second_screen=uic.loadUi("logged-second-screen.ui")
first_screen.pushButton.clicked.connect(show_second_screen)
second_screen.pushButton.clicked.connect(logout)
first_screen.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

first_screen.show()
app.exec()
