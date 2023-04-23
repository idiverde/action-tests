import sys
from PyQt5.QtWidgets import *  # QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout
from PyQt5.QtCore import Qt
import psycopg2
from SUMMARY.MAIN_WINDOW import MainWindow


db_name = 'AMS'
db_username = 'postgres'
db_password = '1113'


class AuthForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Определение элементов интерфейса
        self.label_username = QLabel('Имя пользователя:', self)
        self.label_username.move(50, 30)
        self.textbox_username = QLineEdit(self)
        self.textbox_username.move(50, 50)
        self.label_password = QLabel('Пароль:', self)
        self.label_password.move(50, 90)
        self.textbox_password = QLineEdit(self)
        self.textbox_password.move(50, 110)
        self.textbox_password.setEchoMode(QLineEdit.Password)
        self.button_login = QPushButton('Войти', self)
        self.button_login.move(50, 160)
        self.button_login.clicked.connect(self.login)
        self.button_register = QPushButton('Зарегистрироваться', self)
        self.button_register.move(150, 160)
        self.button_register.clicked.connect(self.register)

        # Установка свойств формы
        self.setWindowTitle('Форма авторизации')
        self.setFixedSize(300, 220)  # фиксированный размер окна
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())  # центрирование
        self.show()

    def login(self):
        # Получение логина и пароля из полей ввода
        username = self.textbox_username.text()
        password = self.textbox_password.text()

        # Подключение к базе данных
        conn = psycopg2.connect(
            host="localhost",
            database=db_name,
            user=db_username,
            password=db_password
        )

        # Выполнение запроса на получение пользователя из базы данных
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
        user = cur.fetchone()

        # Закрытие соединения с базой данных
        cur.close()
        conn.close()

        # Проверка наличия пользователя в базе данных и вывод сообщения об ошибке, если пользователь не найден
        # if user is None:
        #     QMessageBox.warning(self, 'Ошибка', 'Неверное имя пользователя или пароль')
        # else:
        #     QMessageBox.information(self, 'Успешный вход', 'Вы успешно вошли в систему')

        if user:
            self.hide()  # скрываем форму авторизации
            # self.welcome_page = WelcomePage(user[1])  # создаем экземпляр страницы с
            self.welcome_page = MainWindow()
            # приветствием и передаем имя пользователя
            self.welcome_page.show()  # показываем страницу с приветствием
        else:
            # Если пользователь не найден, выводим сообщение об ошибке
            QMessageBox.warning(self, 'Ошибка авторизации', 'Неправильный логин или пароль')

    def register(self):
        # Получение логина и пароля из полей ввода
        username = self.textbox_username.text()
        password = self.textbox_password.text()

        # Подключение к базе данных
        conn = psycopg2.connect(
            host="localhost",
            database=db_name,
            user=db_username,
            password=db_password
        )
        # Выполнение запроса на добавление нового пользователя в базу данных
        cur = conn.cursor()
        cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
        conn.commit()

        # Закрытие соединения с базой данных
        cur.close()
        conn.close()

        # Вывод сообщения об успешной регистрации
        QMessageBox.information(self, 'Успешная регистрация', 'Вы успешно зарегистрировались')

        # Очистка полей ввода
        self.textbox_username.setText('')
        self.textbox_password.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = AuthForm()
    sys.exit(app.exec_())
