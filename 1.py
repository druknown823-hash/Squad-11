import sys 
from PyQt6.QtWidgets import QApplication , QMainWindow , QLabel
from PyQt6.QtGui import QIcon , QFont , QPixmap

VIDEO_PATH = r"D:\FFFFF\GUI\Mexican Yoshi - Nimbly Memes (480p, h264).mp4" 

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("mexial yooshi")
    self.setGeometry(200,100,1000,500)
    self.setWindowIcon(QIcon("D:\FFFFF\GUI\image.png"))
    
    label = QLabel(f"What's up, fuckers? Bet you never seen a Mexican Yoshi before.\nWell, check it out! We got" , self)
    label.setFont(QFont("Arial" , 20))
    label.setGeometry(0,20,1000,60)
    
    
    num = 4
    inss = 50
    x_ord= 0

    for i in range(num):
      pixmap = QPixmap("D:\FFFFF\GUI\yoshi.png")

      x_ord = inss + (i * 221)

      label_2= QLabel(self)
      label_2.setPixmap(pixmap)
      label_2.setGeometry(x_ord,100,201,358)
      label_2.setScaledContents(True)
    


def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())

if __name__ == "__main__":
   main()


