from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QThread, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QTextEdit, QWidget)

from Worker import Worker

class WorkWithUI(object):
    def __init__(self, button1, button2, inputTextEdit, outputTextEdit, roleComboBox):
        self.button1 = button1
        self.button2 = button2

        self.button1.clicked.connect(
        self.startThread)  
        self.button2.clicked.connect(
        self.clearTexts) 

        self.inputTextEdit = inputTextEdit
        self.outputTextEdit = outputTextEdit

        self.roleComboBox = roleComboBox
        self.roleComboBox.addItems(["user", "system", "assistant"])
        self.roleComboBox.currentIndexChanged.connect(
        self.onRoleSelected)
        self.role = "user"  #default role
  
 
    @Slot()
    def clearTexts(self):
        self.inputTextEdit.setPlainText("")
        self.outputTextEdit.setPlainText("")
    
    @Slot(str)
    def updateTextEdit(self, text):
        print(f"updateTextEdit: {QThread.currentThread()}")
        self.outputTextEdit.setPlainText(text)
        #print(text)

    def startThread(self):
        print(f"Starting thread: {QThread.currentThread()}")
        #self.thread = QThread()
        self.worker = Worker(self.inputTextEdit.toPlainText(), self.role)
        
        #self.worker.moveToThread(self.thread)
        
        #connections
        #self.thread.started.connect(self.worker.fun)
        self.worker.responseGenerated.connect(self.updateTextEdit, type=Qt.ConnectionType.QueuedConnection)
        

        #cleanup
        self.worker.finished.connect(lambda x: self.worker.quit())
        self.worker.finished.connect(lambda x: self.worker.deleteLater())
        #self.thread.finished.connect(self.thread.deleteLater)

        #start
        self.worker.start()

    def onRoleSelected(self, index):
        self.role = self.roleComboBox.itemText(index)
        print(f"Selected role: {self.role}")