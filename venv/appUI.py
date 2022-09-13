import sys
from main import MainApp
from datetime import datetime
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QTabWidget,QHBoxLayout,QPushButton,QWidget,QGraphicsItem,QLabel,QComboBox


class App_window(QWidget):
    icon_indent = 70
    list_of_currency = [ "Orb of Alchemy", "Orb of Regret", "Gemcutter's Prism","Chaos Orb",
                        "Orb of Alteration", "Orb of Regret", "Orb of Fusing", "Cartographer's Chisel",
                        "Orb of Scouring", "Regal Orb", "Divine Orb", "Vaal Orb", "Awakened Sextant"] # упорядоченый список валюты
    def __init__(self,parent=None):
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

        # self.timer_end = QLabel(self)
        self.league_list = QComboBox(self)
        self.stash_list = QComboBox(self)

        # self.timer_begin = strftime('%H:%M:%S', time.localtime())
        # self.timer_end = strftime('%H:%M:%S', time.localtime())


        # self.tabwidget = QTabWidget()
        # self.tabwidget.width()
        # self.next_tab = QTabWidget(self)
        # self.next_tab.setGeometry(50,50,100,30)
        # self.new_window = [NextWindow() for i in range(3)]
        # count = 0
        # for i in self.new_window:
        #     self.next_tab.addTab(i,"new window" + str(count))
        #     self.next_tab.setTabText(count, str(count))
        #     count +=1
        # self.next_tab = [QTabWidget(self) for i in range(3)]
        # for i in range(len(self.next_tab)):
        #     self.next_tab[i].setTabText(str(i))

        # self.button_test = QPushButton(self)
        # self.button_test.setGeometry(1100,700,100,100)
        # self.button_test.setText("test")
        # self.button_test.clicked.connect(self.create_window)

        self.timer_result = QLabel(self)
        self.timer_result.setGeometry(1000,250,100,25)

        self.image_arr_path = self.create_path()
        self.old_value_arr = self.app_main.items_list.copy()
        self.new_value_arr = self.app_main.items_list

        self.league_list.setGeometry(900,100,70,25)
        self.league_list.addItems(["standard","hardcore"])
        self.league_list.activated[str].connect(self.change_league)

        self.stash_list.setGeometry(1000,100,150,30)

        self.button_currency_eq = QPushButton(self)
        self.button_currency_eq.setText("calculate eq")
        self.button_currency_eq.setGeometry(1000,300,100,50)
        self.button_currency_eq.clicked.connect(self.button_new_info)

        self.button_refresh = QPushButton(self)
        self.button_refresh.setText("refresh")
        self.button_refresh.setGeometry(800,300,100,50)
        self.button_refresh.clicked.connect(self.button_refresh_click)

        self.creating_display()
        
    def change_league(self, text):
        self.stash_list.clear()
        stash_list_get = {}
        stash_list_get = self.app_main.stash_list_get(text)
        print(type(stash_list_get))
        for i in stash_list_get:
            self.stash_list.addItem(i["name"])
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
        self.timer_begin = datetime.now()
        count = 0
        for i in self.image_arr_path:
            self.load_image(self.labels_arr[count],i, count,pos_x=30)
            self.load_value(self.currency_counts[count],self.old_value_arr[self.list_of_currency[count]], count, pos_x=150)
            count += 1
        #сбросить остальные зачения

    def button_refresh_click(self):#клик кнопки "сбросить"
        self.old_value_arr = self.app_main.send_request().copy()
        self.timer_result.setText('0:00:00')
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


    def button_currency_calculate(self):
        self.timer_end = datetime.now()
        self.timer_result.setText(str(self.timer_end - self.timer_begin).split('.')[0])
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
