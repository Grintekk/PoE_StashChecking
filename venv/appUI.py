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

    def load_image(self,file_name,n): #загружаем картинку с отступом сверху
        transport = (5 + self.icon_indent*n)
        pixmap = QPixmap(file_name)
        #self.currency_counts[n].setText(str(file_name))
        #self.currency_counts[n].setGeometry(200,transport, self.icon_indent, self.icon_indent)
        self.labels_arr[n].setPixmap(pixmap)
        self.labels_arr[n].setGeometry(30, transport, self.icon_indent, self.icon_indent)

    def load_value(self,dict_values,list_of_currency): #
        count = 0
        for i in list_of_currency:
            transport = (15 + self.icon_indent * count)
            self.currency_counts[count].setText(str(dict_values[i]))
            self.currency_counts[count].setGeometry(150,transport,self.icon_indent,self.icon_indent)
            count +=1
            #self.currency_counts[n].setText(str(n*10))

def create_path(list_of_currency):
    image_arr_path = []
    for i in list_of_currency:
        image_arr_path.append("./Icons/" + str(i) + ".png")
    return image_arr_path
def main_window():
    app = QApplication(sys.argv)
    window = AppWindow()
    count = 0
    image_arr_path = create_path(window.list_of_currency)  #
    for i in image_arr_path:
        window.load_image(i,count)
        count += 1
    window.load_value(allCurrency.getCurrency(),window.list_of_currency)
    window.show()
    sys.exit(app.exec_())
# main_window()