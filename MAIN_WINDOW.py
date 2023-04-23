import sys
from PyQt5.QtWidgets import *
from SUMMARY.BUTTONS_FUNCTIONS import MyFunctions


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Создаем меню
        self.menu = self.menuBar()

        # Создаем виджет с двумя вкладками
        tabs = QTabWidget(self)
        tabs.resize(300, 200)
        tabs.move(20, 20)

        # Добавляем вкладки
        self.tab1 = QWidget()
        tabs.addTab(self.tab1, "Вкладка 1")

        self.tab2 = QWidget()
        tabs.addTab(self.tab2, "Вкладка 2")

        # Создаем экземпляр класса MyFunctions
        self.functions = MyFunctions()

        # связываем кнопки с обработчиками
        self.setup_buttons()

        # Настраиваем главное окно
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Пример GUI на PyQt5')
        self.show()

    def setup_buttons(self):
        # Создаем две кнопки для меню и подключаем функции
        menu_button_1 = QAction('Кнопка 1', self)
        menu_button_1.triggered.connect(self.functions.on_triggered)
        menu_button_2 = QAction('Кнопка 2', self)
        menu_button_2.triggered.connect(self.functions.sql_query)
        # Добавляем кнопки в меню
        self.menu.addAction(menu_button_1)
        self.menu.addAction(menu_button_2)

        # Вызываем функцию и отображаем таблицу.
        menu_button_3 = QAction('Кнопка 3', self)
        menu_button_3.triggered.connect(lambda: self.functions.button3(self.tab1))  # передаем в какой вкладке рисовать
        # result = menu_button_3.triggered.connect(self.functions.button3)
        self.menu.addAction(menu_button_3)

        #
        # table = QTableWidget(self.tab1)
        # table.setRowCount(len(result))
        # table.setColumnCount(len(result[0]))
        # for i, row in enumerate(result):
        #     for j, value in enumerate(row):
        #         table.setItem(i, j, QTableWidgetItem(str(value)))
        #
        # self.tab2.layout().addWidget(menu_button_3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
