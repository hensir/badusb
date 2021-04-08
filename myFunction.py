import sys

from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal
from ui_function import Ui_Form  # 功能区
from mySelectDialog import QMySelectDialog  # 功能区的点击选择的按钮
from CodeList import CodeList  # listwidget等会初始化
from Enmu_Key import GlobalReplacement, DialogKeyPushButton, DKPB


class QMyFunction(QWidget):
    ClickAppendPb = pyqtSignal(str)
    ClickListItem = pyqtSignal(list)
    ClickKeySignal = pyqtSignal(str)
    AppendPatchKey = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.curstackpageindex = 0
        self.defined = []  # 已经定义过的按键
        print("层叠页面有" + str(self.ui.stackedWidget.count()) + "个")
        self.Codelist_Init()

    @pyqtSlot()
    def on_PrevStacked_clicked(self):
        self.curstackpageindex -= 1
        if self.curstackpageindex < 0:
            self.curstackpageindex = self.ui.stackedWidget.count() - 1
        print(self.curstackpageindex)
        self.ui.stackedWidget.setCurrentIndex(self.curstackpageindex)

    @pyqtSlot()
    def on_NextStacked_clicked(self):
        self.curstackpageindex += 1
        if self.curstackpageindex >= self.ui.stackedWidget.count():
            self.curstackpageindex = 0
        print(self.curstackpageindex)
        self.ui.stackedWidget.setCurrentIndex(self.curstackpageindex)

    @pyqtSlot()
    def on_ClickToInPB_clicked(self):
        """这个是 点击输入按钮"""
        self.__dialog = QMySelectDialog()  # 按键对话框
        self.__dialog.setAttribute(Qt.WA_DeleteOnClose)  # 对话框关闭时自动删除
        self.__dialog.ButtonClick.connect(self.KeySignal)
        self.__dialog.changePBEnable.connect(self.ui.ClickToInPB.setEnabled)
        self.__dialog.show()

    # @pyqtSlot()
    # def on_toDigiPB_clicked(self):
    #     print("123")
    #     pass

    @pyqtSlot()
    def on_LSEPushButton_clicked(self):
        text2 = "DigiKeyboard.print(\"%s\");" % (self.ui.LineStrEdit.text())
        self.ClickAppendPb.emit(text2)

    @pyqtSlot()
    def on_SSBPButton_clicked(self):
        text2 = r"DigiKeyboard.delay(%s);" % (self.ui.SleepSpinBox.value())
        self.ClickAppendPb.emit(text2)

    @pyqtSlot()
    def Codelist_Init(self):  # 初始化CodeListWIdget
        for codeinfo in CodeList:
            aItem = QListWidgetItem()
            aItem.setText(codeinfo[0])
            aItem.setData(Qt.UserRole, codeinfo)
            self.ui.CListWidget.addItem(aItem)

    @pyqtSlot(QListWidgetItem)
    def on_CListWidget_itemDoubleClicked(self, item):  # 双击发送信号 打开新文档
        data = item.data(Qt.UserRole)
        self.ClickListItem.emit(data)

    @pyqtSlot(int)
    def on_PBComboBox_activated(self, keytype):
        ShortCutList = [x.split('+') for x in
                        self.ui.KeySeqEdit.keySequence().toString().split(',')]  # 哈哈哈 这两句别砍我  # short cut list
        ShortCutList = ["".join(x.split()) for i in ShortCutList for x in
                        i]  # for嵌套的列表推导式 注 前一for迭代值是后一for的迭代器 最后又加了一个list转str
        self.KeySignal(ShortCutList, keytype)

    @pyqtSlot(list, int)
    def KeySignal(self, text2send, keytype):  # 申错的太简单 而且现在还没做常量对换
        status = False
        patchtext = ""  # 将要预定义的字符串 因为信号处理顺序问题  所以需要这么写
        # 等一下 这个东西 是需要跟随formdoc一块的 也就是后期动态添加一个实例变量
        # 我新建一个文档 就会触发 函数连接信号失败
        for i in range(len(text2send)):
            if text2send[i] in GlobalReplacement:
                print("GlobalReplacement", text2send[i])
                text2send[i] = GlobalReplacement[text2send[i]]
            elif text2send[i] in DKPB:
                if text2send[i] in self.formDoc.defined:  # 他说myfunction没有fordoc
                    continue  # 当然没有了 但是怎么解决这个问题 有参数 有信号
                self.formDoc.defined.append(text2send[i])  # 添加到已定义的列表中
                print("DKPB", text2send[i])
                patchtext = DKPB[text2send[i]]
                text2send[i] = "key_" + text2send[i]
                patchtext = "#define " + text2send[i] + " " + patchtext
                status = True
                print(patchtext)
            else:
                print("未知按键", text2send[i])

        if keytype == 0:
            text = "DigiKeyboard.sendKeyStroke("
            if len(text2send) >= 2:
                text += text2send[1]
                text += ","
                text += text2send[0]
            else:
                text += text2send[0]
            text += ");"
        elif keytype == 1:
            text = "DigiKeyboard.sendKeyPress("
            if len(text2send) >= 2:
                text += text2send[1]
                text += ","
                text += text2send[0]
            else:
                text += text2send[0]
            text += ");"
        elif keytype == 2:
            text = "DigiKeyboard.sendKeyPress(0);"

        self.ClickKeySignal.emit(text + "\n")
        if status:
            self.AppendPatchKey.emit(patchtext + "\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QMyFunction()
    form.show()
    sys.exit(app.exec_())

# Ducky语法
# ALT [key name] (ex: ALT F4, ALT SPACE)
# CTRL | CONTROL [key name] (ex: CTRL ESC)
# CTRL-ALT [key name] (ex: CTRL-ALT DEL)
# CTRL-SHIFT [key name] (ex: CTRL-SHIFT ESC)
# DEFAULT_DELAY | DEFAULTDELAY [Time in millisecond] (change the delay between each command)
# DELAY [Time in millisecond] (used to overide temporary the default delay)
# GUI | WINDOWS [key name] (ex: GUI r, GUI l)
# REM [anything] (used to comment your code, no obligation :) )
# ALT-SHIFT (swap language)
# SHIFT [key name] (ex: SHIFT DEL)
# STRING [any character of your layout]
# STRING_DELAY [Number] [any character of your layout] (Number is ms delay between each character)
# REPEAT [Number] (Repeat last instruction N times)
# [key name] (anything in the keyboard.properties)
