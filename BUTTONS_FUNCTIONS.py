from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import *
import psycopg2

db_name = 'AMS'
db_username = 'postgres'
db_password = '1113'


class MyFunctions(QObject):
    @pyqtSlot()
    def on_triggered(self):
        # Выполнение функции для первой кнопки
        print("Нажата кнопка 1!")
        QMessageBox.information(self.parent(), 'Сообщение', 'Нажата кнопка 1!')

    @pyqtSlot()
    def sql_query(self):
        # Выполнение функции для второй кнопки
        print("Нажата кнопка 2!")
        QMessageBox.information(self.parent(), 'Сообщение', 'Нажата кнопка 2!')

    @pyqtSlot()
    def button3(self, tab):
        QMessageBox.information(self.parent(), 'Сообщение', 'Нажата кнопка 3!')
        db = Database(dbname=db_name, user=db_username, password=db_password, host='localhost')
        db.connect()
        cursor = db.conn.cursor()
        cursor.execute("SELECT * from users;")
        result = cursor.fetchall()
        db.disconnect()

        print(result)

        table = QTableWidget(tab)
        table.setColumnCount(len(result[0]))
        table.setRowCount(len(result))
        table.setHorizontalHeaderLabels(['Column ' + str(i + 1) for i in range(len(result[0]))])
        for i, row in enumerate(result):
            for j, item in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(item)))

        # ВОТ ЭТО НАДО
        layout = QVBoxLayout(tab)
        layout.addWidget(table)


class Database:
    def __init__(self, dbname, user, password, host):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host
        )

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def execute(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        cursor.close()