import sys
from main import MainApp
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication,QHBoxLayout,QPushButton,QWidget,QGraphicsItem,QLabel

class App_window(QWidget):
    icon_indent = 70
    list_of_currency = [ "Orb of Alchemy", "Orb of Regret", "Gemcutter's Prism","Chaos Orb",
                        "Orb of Alteration", "Orb of Regret", "Orb of Fusing", "Cartographer's Chisel",
                        "Orb of Scouring", "Regal Orb", "Divine Orb", "Vaal Orb", "Awakened Sextant"] # упорядоченый список валюты
    def __init__(self):
        super().__init__()
        self.app_main = MainApp()

        self.setWindowTitle("App")
        self.left = 40
        self.top = 40
        self.width = 1500
        self.height = 950
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.labels_arr = [QLabel(self) for i in range(len(self.list_of_currency))]
        self.currency_counts = [QLabel(self) for i in range(len(self.list_of_currency))] #главный
        self.new_currency_counts = [QLabel(self) for i in range(len(self.list_of_currency))] #новый
        self.changing_currency = [QLabel(self) for i in range(len(self.list_of_currency))] #разница
        self.currency_equal_values = [QLabel(self) for i in range(len(self.list_of_currency))] #массив в хаосах

        self.image_arr_path = self.create_path()
        self.old_value_arr = self.app_main.items_list.copy()
        self.new_value_arr = self.app_main.items_list
        # self.currency_value = self.app_main.give_value()


        # self.button_save_file = QPushButton(self)
        # self.button_save_file.setText("Save")
        # self.button_save_file.setGeometry(1000,300,100,50)
        # self.button_save_file.clicked.connect(self.button_save_click)

        self.button_currency_eq = QPushButton(self)
        self.button_currency_eq.setText("calculate eq")
        self.button_currency_eq.setGeometry(1000,300,100,50)
        self.button_currency_eq.clicked.connect(self.button_new_info)

        self.button_refresh = QPushButton(self)
        self.button_refresh.setText("refresh")
        self.button_refresh.setGeometry(800,300,100,50)
        self.button_refresh.clicked.connect(self.button_refresh_click)

        self.creating_display()
    def load_image(self,label,file_name,n,pos_x): #загружаем картинку с отступом сверху
        transport = (5 + self.icon_indent*n)#?каждый раз вызывается
        pixmap = QPixmap(file_name)
        label.setPixmap(pixmap)
        label.setGeometry(pos_x, transport, self.icon_indent, self.icon_indent)

    def load_value(self,label,value,n,pos_x): # Загружаем значение как и картинки
        transport = (15 + self.icon_indent * n)#?каждый раз вызывается
        label.setText(str(value))
        label.setGeometry(pos_x,transport,self.icon_indent,self.icon_indent)

    def creating_display(self): # цикл для загрузки картинок и значений, будет привязан к кнопке "сбросить"
        count = 0
        for i in self.image_arr_path:
            self.load_image(self.labels_arr[count],i, count,pos_x=30)
            self.load_value(self.currency_counts[count],self.old_value_arr[self.list_of_currency[count]], count, pos_x=150)
            count += 1
        #сбросить остальные зачения

    def button_refresh_click(self):#клик кнопки "сбросить"
        self.old_value_arr = self.app_main.send_request().copy()
        self.creating_display()

    def button_new_info(self):
        self.new_value_arr = self.app_main.send_request()
        # calc_list = []
        count = 0
        for i in self.list_of_currency:
            self.load_value(self.new_currency_counts[count],self.new_value_arr[i],count,pos_x=350)
            a = self.new_value_arr[i] - self.old_value_arr[i]
            if(int(a)>0):
                a = '+' + str(a)
                self.changing_currency[count].setStyleSheet('color: green')
            else:
                self.changing_currency[count].setStyleSheet('color: red')
            self.load_value(self.changing_currency[count],a,count,pos_x=500)
            # print(self.changing_currency[count].text())
            # print(type(self.changing_currency[count].text()))
            count +=1
        self.button_currency_calculate()

    # def button_save_click(self):
        # self.app_main.save_info("NewFile")#переделать
    def button_currency_calculate(self):
        value = self.app_main.ninja_request()
        sum = 0
        arr = self.list_of_currency.copy()

        count = 0
        for i in arr:    #проверка только по выведенным
            mult = float(self.changing_currency[count].text())*value[i]
            self.load_value(self.currency_equal_values[count],int(mult),count,pos_x=750)
            sum += mult
            count +=1
        # sum += self.currency_value["Chaos Orb"]
        self.button_currency_eq.setText(str(sum))###########

    def create_path(self):  # список путей иконок
        image_arr_path = []
        for i in self.list_of_currency:
            image_arr_path.append("./Icons/" + str(i) + ".png")
        return image_arr_path

def main_window():
    app = QApplication(sys.argv)
    window = App_window()

    window.show()
    sys.exit(app.exec_())
main_window()
