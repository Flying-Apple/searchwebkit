import sys
import webbrowser
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
#from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

#from PyQt5.QtGui import QIcon
class Render(QWebPage):  
  def __init__(self, url):  
    self.loop = QEventLoop()  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)
    self.mainFrame().load(QUrl(url))  
    self.loop.exec_()

  def _loadFinished(self, result):  
    self.frame = self.mainFrame() 
    self.loop.quit()  

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'search items'
        self.left = 930
        self.top = 430
        self.width = 500
        self.height = 550
        self.web=QWebView()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 420)
        self.textbox.resize(420,40)
 
        button = QPushButton('Chemist', self)
        button.setToolTip('searh item in chemist')
        button.move(50,470)
        button.clicked.connect(self.on_clickchemist)

        button = QPushButton('Woolworths', self)
        button.setToolTip('searh item in WOOL')
        button.move(130,470) 
        button.clicked.connect(self.on_clickwool)

        button = QPushButton('Coles', self)
        button.setToolTip('searh item in COLES')
        button.move(210,470) 
        button.clicked.connect(self.on_clickcoles)

        button = QPushButton('Amazon', self)
        button.setToolTip('searh item in Amazon')
        button.move(290,470) 
        button.clicked.connect(self.on_clickamazon)        

        button = QPushButton('澳邮', self)
        button.setToolTip('chakuaidi')
        button.move(370,470) 
        button.clicked.connect(self.on_clickaoyou) 

        button = QPushButton('Close', self)
        button.setToolTip('CLOSE')
        button.move(130,520) 
        button.clicked.connect(self.close)
        
        self.show()
    #@pyqtSlot()
    def on_clickchemist(self):
        textboxValue = self.textbox.text()
        search= textboxValue
        self.web.load(QUrl("https://www.chemistwarehouse.com.au/search?searchtext="+search+"&searchmode=allwords"))
        
        self.web.show()
    def on_clickwool(self):
        textboxValue = self.textbox.text()
        search= textboxValue
        self.web.load(QUrl('https://www.woolworths.com.au/shop/search/products?searchTerm='+search))
        self.web.show()
    def on_clickcoles(self):
        textboxValue = self.textbox.text()
        search= textboxValue
        self.web.load(QUrl('https://shop.coles.com.au/a/a-national/everything/search/'+search))
        self.web.show()
    def on_clickamazon(self):
        textboxValue = self.textbox.text()
        search= textboxValue
        self.web.load(QUrl('https://www.amazon.co.jp/s/ref=nb_sb_noss?__mk_ja_JP=カタカナ&url=search-alias%3Daps&field-keywords='+search))
        self.web.show()
    def on_clickaoyou(self):
        #vbox = QVBoxLayout()
        #self.setParent(None)
        textboxValue = self.textbox.text()
        search=[]
        search=textboxValue.split()
        allnumber=[]
        for i in search:
            url='http://www.auexpress.com.au/TOrderActList_Service.aspx?OrderId='+ i
            self.web = Render(url)  
            document= self.web.mainFrame().documentElement()
        #box=document.findFirst('div#ctl00_ContentPlaceHolder1_dg')
            box2=document.findFirst('a#ctl00_ContentPlaceHolder1_hlTrnsfId')
            text1=box2.toPlainText()
            allnumber.append(i)
            allnumber.append(text1)
       #text2=box.toPlainText()
       #print(text1)
       # print(text2)
        print(allnumber)
        alltext=''
        a=0
        for i in allnumber:
            alltext=alltext+i+' '
            if a%2==1:
                alltext=alltext+'\n'
            a+=1
        display=QLabel()
        display.setText(alltext)
        display.setTextInteractionFlags(Qt.TextSelectableByMouse)
        display.setAlignment(Qt.AlignBottom)
       # display2=QLabel()
        #display2.setText(text2)
        vbox = QVBoxLayout()
        vbox.addWidget(display)
        vbox.addStretch()
        
       # vbox.addWidget(display2)
       # vbox.addStretch()
        self.setLayout(vbox)

	

if __name__ == '__main__':
    try:
        app
    except:
        app = QApplication(sys.argv)

    ex = App()

    sys.exit(app.exec_())

