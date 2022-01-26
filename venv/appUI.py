import sys
import allCurrency
from  PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication,QHBoxLayout,QPushButton,QWidget,QGraphicsItem,QLabel

class AppWindow(QWidget):
    icon_indent = 70
    list_of_currency = ["Chaos Orb", "Orb of Alchemy", "Orb of Regret", "Gemcutter's Prism",
                        "Orb of Alteration", "Orb of Regret", "Orb of Fusing", "Cartographer's Chisel",
                        "Orb of Scouring", "Regal Orb", "Divine Orb", "Vaal Orb", "Awakened Sextant"] # упорядоченый список валюты
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App")
        self.left = 40
        self.top = 40
        self.width = 1500
        self.height = 900
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.labels_arr = [QLabel(self) for i in range(13)]
        self.currency_counts = [QLabel(self) for i in range(13)]
        self.image_arr_path = create_path(self.list_of_currency)

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
        curency_value = allCurrency.getCurrency()
        count = 0
        for i in self.image_arr_path:
            self.load_image(i, count)
            self.load_value(curency_value[self.list_of_currency[count]], count)
            count += 1
    def button_refresh_click(self):
        self.creating_display()

def create_path(list_of_currency):
    image_arr_path = []
    for i in list_of_currency:
        image_arr_path.append("./Icons/" + str(i) + ".png")
    return image_arr_path
def main_window():
    app = QApplication(sys.argv)
    window = AppWindow()

    window.show()
    sys.exit(app.exec_())
main_window()