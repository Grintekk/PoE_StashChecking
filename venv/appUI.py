import sys
from main import MainApp
from  PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication,QHBoxLayout,QPushButton,QWidget,QGraphicsItem,QLabel

class AppWindow(QWidget):
    icon_indent = 70
    list_of_currency = ["Chaos Orb", "Orb of Alchemy", "Orb of Regret", "Gemcutter's Prism",
                        "Orb of Alteration", "Orb of Regret", "Orb of Fusing", "Cartographer's Chisel",
                        "Orb of Scouring", "Regal Orb", "Divine Orb", "Vaal Orb", "Awakened Sextant"] # упорядоченый список валюты
    def __init__(self):
        super().__init__()
        self.app_main = MainApp()
        self.setWindowTitle("App")
        self.left = 40
        self.top = 40
        self.width = 1500
        self.height = 900
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.labels_arr = [QLabel(self) for i in range(13)]
        self.currency_counts = [QLabel(self) for i in range(13)]
        self.image_arr_path = self.create_path()
        self.curency_value = self.app_main.give_new_value()

        # self.button_save_file = QPushButton(self)
        # self.button_save_file.setText("Save")
        # self.button_save_file.setGeometry(1000,300,100,50)
        # self.button_save_file.clicked.connect(self.button_save_click)

        self.button_currency_eq = QPushButton(self)
        self.button_currency_eq.setText("calculate eq")
        self.button_currency_eq.setGeometry(1000,300,100,50)
        self.button_currency_eq.clicked.connect(self.button_currency_calculate)

        self.button_refresh = QPushButton(self)
        self.button_refresh.setText("refresh")
        self.button_refresh.setGeometry(800,300,100,50)
        self.button_refresh.clicked.connect(self.button_refresh_click)

        self.creating_display()

    def load_image(self,file_name,n): #загружаем картинку с отступом сверху
        transport = (5 + self.icon_indent*n)
        pixmap = QPixmap(file_name)
        self.labels_arr[n].setPixmap(pixmap)
        self.labels_arr[n].setGeometry(30, transport, self.icon_indent, self.icon_indent)

    def load_value(self,value,n): # Загружаем значение как и картинки
        transport = (15 + self.icon_indent * n)
        self.currency_counts[n].setText(str(value))
        self.currency_counts[n].setGeometry(150,transport,self.icon_indent,self.icon_indent)

    def creating_display(self): # цикл для загрузки картинок и значений, будет привязан к кнопке "обновить"
        # self.app_main.save_info("New_info")
        count = 0
        for i in self.image_arr_path:
            self.load_image(i, count)
            self.load_value(self.curency_value[self.list_of_currency[count]], count)
            count += 1

    def button_refresh_click(self):#клик кнопки
        self.creating_display()
    # def button_save_click(self):
        # self.app_main.save_info("NewFile")#переделать
    def button_currency_calculate(self):
        value = self.app_main.ninja_request()
        sum = 0
        arr = self.list_of_currency
        arr.remove("Chaos Orb")
        for i in self.list_of_currency:    #проверка только по выведенным
            sum += self.curency_value[i]*value[i]
        sum += self.curency_value["Chaos Orb"]
        self.button_currency_eq.setText(str(sum))
    def create_path(self):  # список путей иконок
        image_arr_path = []
        for i in self.list_of_currency:
            image_arr_path.append("./Icons/" + str(i) + ".png")
        return image_arr_path

def main_window():
    app = QApplication(sys.argv)
    window = AppWindow()

    window.show()
    sys.exit(app.exec_())
main_window()