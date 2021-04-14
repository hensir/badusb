import os
import sys
from PyQt5.QtCore import Qt, QFile, QIODevice
from PyQt5.QtGui import QTextOption
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QGridLayout, QWidget, \
    QFontDialog


class FromDoc(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.setWindowTitle("无标题")  # 窗口标题
        self.setAttribute(Qt.WA_DeleteOnClose)  # MDI子窗口会被自动删除
        self.__fileOpened = ""
        self.currentFilePath = ""
        self.defined = []  # 已经出现的按键 绑定给本体了

    def setupUi(self):
        self.resize(666, 401)
        self.widget = QWidget(self)
        self.gL = QGridLayout(self.widget)
        self.gL.setContentsMargins(0, 0, 0, 0)
        self.tE = QTextEdit(self)
        self.font = self.tE.font()
        self.font.setFamily("宋体")  # 文本文档中的字体是 微软雅黑常规小四12磅
        self.font.setPointSize(12)
        self.tE.setFont(self.font)
        self.gL.addWidget(self.tE, 0, 0, 1, 1)
        self.setCentralWidget(self.widget)
        self.tE.setWordWrapMode(QTextOption.NoWrap)
        # self.tE.setWordWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)
        print(self.tE.wordWrapMode())

    def loadFromFile(self, filename):  # 打开文件
        self.currentFilePath = filename
        self.setWindowTitle(filename)
        self.__fileOpened = True
        baseFilename = os.path.basename(filename)  # 去掉目录后的文件名
        self.setWindowTitle(baseFilename)
        fileDevice = QFile(filename)
        if not fileDevice.exists():
            return False
        if not fileDevice.open(QIODevice.ReadOnly | QIODevice.Text):
            return False
        try:
            self.tE.clear()
            qtBytes = fileDevice.readAll()  # 返回QByteArray类型
            pyBytes = bytes(qtBytes.data())  # 将QByteArray转换为bytes类型
            text = pyBytes.decode("utf-8")  # 用utf-8编码为字符串
            self.tE.setText(text)
        finally:
            fileDevice.close()
        return True

    def currentFileName(self):  # 返回当前文件名
        return self.windowTitle()

    def isFileOpened(self):  # 文件是否打开
        if len(self.tE.toPlainText()) > 0:  # 在主窗口调用方法的时候多了一个检测功能 就是如果编辑框不为空同样也返回 文件已打开
            self.__fileOpened = True  # 这样mdi就会新建一个窗口来打开文本文件了
        return self.__fileOpened

    def textSetFont(self):  # 设置字体
        iniFont = self.tE.font()  # 获取文本框的字体
        font, OK = QFontDialog.getFont(iniFont)  # 选择字体, 注意与C++版本不同
        if OK:  # 选择有效
            self.tE.setFont(font)

    def mysetWordWrapMode(self):
        if self.tE.wordWrapMode() == 0:
            self.tE.setWordWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)
        else:
            self.tE.setWordWrapMode(QTextOption.NoWrap)
        print("666")


if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = FromDoc()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
