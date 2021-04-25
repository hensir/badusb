import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem
from PyQt5.QtCore import Qt,pyqtSlot
from function.ui_function import Ui_Form  # 功能区
from function.CodeList import CodeList  # listwidget等会初始化


class QMyFunction(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.curstackpageindex = 0
        self.defined = []  # 已经定义过的按键

        for codeinfo in CodeList:  # 初始化list
            aItem = QListWidgetItem()
            aItem.setText(codeinfo[0])
            aItem.setData(Qt.UserRole, codeinfo)
            self.ui.CListWidget.addItem(aItem)

        print("层叠页面有" + str(self.ui.stackedWidget.count()) + "个")

    # ---- 自动连接的信号 ----
    @pyqtSlot()
    def on_PrevStacked_clicked(self):  # 层叠组件上一页
        self.curstackpageindex -= 1
        if self.curstackpageindex < 0:
            self.curstackpageindex = self.ui.stackedWidget.count() - 1
        print("当前页面索引", self.curstackpageindex)
        self.ui.stackedWidget.setCurrentIndex(self.curstackpageindex)

    @pyqtSlot()
    def on_NextStacked_clicked(self):  # 层叠组件下一页
        self.curstackpageindex += 1
        if self.curstackpageindex >= self.ui.stackedWidget.count():
            self.curstackpageindex = 0
        print("当前页面索引", self.curstackpageindex)
        self.ui.stackedWidget.setCurrentIndex(self.curstackpageindex)


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
