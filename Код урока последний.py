import sys
import random
from PyQt5.QtWidgets import (QWidget, QToolTip,QPushButton,QLabel, QApplication,QLCDNumber,QTextEdit, QSlider, QVBoxLayout,QMainWindow,QCheckBox,QFrame,QProgressBar,QCalendarWidget,QAction, qApp)
from PyQt5.QtGui import (QIcon,QFont,QColor,QPixmap)
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal, QObject,QBasicTimer,QDate,QMetaObject,QSize,QRect,QTimer




class Window(QMainWindow):
    resized = pyqtSignal()
    click=pyqtSignal()
    def  __init__(self, parent=None):
        super().__init__()
        self.j=0


        self.UI()
    def UI(self):
        self.btn_mas=[]
        self.label_mas=[]
        self.image_mas=[]
        self.btn_x=0
        self.btn_y=100
        self.width_btn=150

        self.height_btn=300


        self.resized.connect(self.someFunction)
        self.centralwidget=QWidget(self)
        self.setWindowTitle('Resize')
        self.resize(1600,1600)

        self.CreateLabel()
        self.CreateImage()
        self.CreateButton()










        self.show()
    def CreateImage(self):
        mas_image=[]
        for i in range(9):
             path='{}'.format(i)+'.jpg'
             print(path)
             pixmap1=QPixmap(path)
             pixmap1=pixmap1.scaled(QSize(150,300))
             mas_image.append(pixmap1)



        return mas_image
    def CreateLabel(self):
        mas=[]
        self.label_number=[]
        mas_image=self.CreateImage()
        print(mas_image)

        for x in range (0, 30):
             num = random.randint(0, 30)
             while num in mas:
                 num = random.randint(0, 30)
             mas.append(num)




        j=0
        for i in range(30):

            if self.btn_x>1500:
                self.btn_x=0
                self.btn_y+=302


            label=QLabel(self)
            label.setGeometry(self.btn_x,self.btn_y,self.width_btn,self.height_btn)



            if j>8:
                j=0



            label.setPixmap(mas_image[j])
            self.label_number.append(str(j))
            j+=1
            label.setVisible(True)

            self.label_mas.insert(mas[i],label)


            self.btn_x+=160


    def CreateButton(self):

        self.j+=1

        self.btn_x=0
        self.btn_y=100


        for i in range(30):

            if self.btn_x>1500:
                self.btn_x=0
                self.btn_y+=302
            self.btn=QPushButton(self)



            self.btn.setGeometry(self.btn_x,self.btn_y,self.width_btn,self.height_btn)
            pixmap=QPixmap('10.jpg')

            pixmap=pixmap.scaled(QSize(150,300))

            self.btn.setIcon(QIcon(pixmap))


            self.btn.setIconSize(QSize(150,300))



            self.btn.setVisible(True)






            self.btn_x+=160
            self.btn.clicked.connect(self.Click)

            self.btn_mas.append(self.btn)







    def Click(self):
        j=0



        sender=self.sender()
        print(sender,'sender')
        for i in self.btn_mas:
          if sender==i:

            (self.btn_mas[j].setVisible(False))
            break
          j+=1
          print(j)

        print(self.label_number[j],'mas')





    def Button(self,event):
        print(self.sender().text())
    def resizeEvent(self, event):
        self.resized.emit()
        return super(Window, self).resizeEvent(event)

    def someFunction(self):
        print(self.width())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())