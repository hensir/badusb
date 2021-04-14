import sys

from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QMdiArea
from documentF.myDocument import QMyDocument  # mdi文档
from functionF.Enmu_Key import GlobalReplacement, DKPB
from functionF.myFunction import QMyFunction  # 功能区组件
from documentF.myFromDoc import FromDoc  # 小组件需要升个级
from functionF.DuckToDigi import Duckyspark_translator
from functionF.CodeList import DigiKeyboardH

# duckytodigi的反向操作 不就可以生成ducky的脚本了吗

# 这个fundoc和function 的区别到底是什么   function做好内务工作  像初始化列表那种
# 而fundoc这边的共用信号 指的是 必须要用到 self的 无法通过信号进行操作的 方法定义
# 具体区别主要表现和规定在 function一定要做好内务 然后其他的方法可能都要放到fundoc里
# 全部信号连接在功能区信号那里做槽函数 function的限定我已经理出来了
# 这样可以取消大量信号操作 而且那个defind列表可以动态添加了 就不用破坏文本文档本质了





from functionF.mySelectDialog import QMySelectDialog


class QMyFunDoc(QMyDocument):
    ClickAppendPb = pyqtSignal(str)
    ClickListItem = pyqtSignal(list)
    ClickKeySignal = pyqtSignal(str)
    AppendPatchKey = pyqtSignal(str)
    PressButton = pyqtSignal(list, int)
Z
    def __init__(self):
        super().__init__()
        # ---- 设置UI ----
        self.fun = QMyFunction(self)
        self.ui.gridLayout.removeWidget(self.ui.mdi)
        self.ui.gridLayout.addWidget(self.fun)
        self.ui.gridLayout.addWidget(self.ui.mdi)

        # ---- 初始化窗口 ---
        self.on_act_New_triggered()
        self.formDoc.setWindowTitle("DigiKeyboard头文件")
        self.formDoc.tE.setText(DigiKeyboardH)
        self.on_act_New_triggered()
        self.ui.mdi.tileSubWindows()
        # ---- 设置功能区信号 ----
        self.fun.ui.toDigiPB.clicked.connect(lambda: self.OpenListItem(
            [self.formDoc.windowTitle(), Duckyspark_translator(self.formDoc.tE.toPlainText())]))
        self.fun.ClickListItem.connect(self.OpenListItem)  # 单信号结束
        self.fun.AppendPatchKey.connect(self.AppendPatch)
        self.fun.ui.ClickToInPB.clicked.connect(self.ClickToInPB_clicked)
        self.fun.ui.LSEPushButton.clicked.connect(LSEPushButton_clicked)

    def LSEPushButton_clicked(self):
        text2 = "DigiKeyboard.print(\"%s\");" % (self.fun.ui.LineStrEdit.text())

        self.ClickAppendPb.emit(text2 + "\n")


def AppendPatch(self, patchstr):
        self.formDoc.tE.moveCursor(QTextCursor.Start, QTextCursor.MoveAnchor)
        self.formDoc.tE.insertPlainText(patchstr)

    def ClickToInPB_clicked(self):
        """这个是 点击输入按钮"""
        self.__dialog = QMySelectDialog()  # 按键对话框
        self.__dialog.setAttribute(Qt.WA_DeleteOnClose)  # 对话框关闭时自动删除
        self.__dialog.ButtonClick.connect(self.KeySignal)
        self.__dialog.changePBEnable.connect(self.fun.ui.ClickToInPB.setEnabled)
        self.__dialog.show()

    @pyqtSlot(list)
    def OpenListItem(self, listitem):
        if len(self.ui.mdi.subWindowList()) > 0:  # 如果有打开的MDI窗口，获取活动窗口
            self.formDoc = self.ui.mdi.activeSubWindow().widget()
            needNew = self.formDoc.isFileOpened()  # 文件已经打开，需要新建窗口
        else:
            needNew = True  # # 是否需要新建子窗口
        if needNew:
            self.formDoc = FromDoc(self)  # 必须指定父窗口
            self.ui.mdi.addSubWindow(self.formDoc)  # 添加到MDI区域
        self.formDoc.setWindowTitle(listitem[0])
        self.formDoc.tE.setText(listitem[1])
        self.formDoc.show()

    @pyqtSlot()  # “新建文档”
    def on_act_New_triggered(self):
        self.formDoc = FromDoc(self)
        self.formDoc.setWindowTitle("无标题" + str(self.mdiTitleindex))
        self.formDoc.tE.setText("""#include "DigiKeyboard.h"\nvoid setup() {\n\n}\n\nvoid loop() {\n\n}\n""")
        self.mdiTitleindex += 1
        self.ui.mdi.addSubWindow(self.formDoc)  # 文档窗口添加到MDI
        self.formDoc.show()  # 在单独的窗口中显示

    def on_mdi_subWindowActivated(self, mdisubwindow):  # 参数为当前激活窗口   不要激活 要子窗口切换的信号   信号有很大重构的可能
        try:
            curmdiwidget = mdisubwindow.widget()
        except AttributeError as e:
            print(e)  # 出现于关闭主窗口时 最后一次激活无效
            return
        mdisubwindowlist = self.ui.mdi.subWindowList(QMdiArea.ActivationHistoryOrder)
        cnt = len(mdisubwindowlist)
        if cnt == 0:
            self.ui.StatusB.clearMessage()
        else:
            self.formDoc = curmdiwidget
            self.ui.StatusB.showMessage(self.formDoc.currentFileName())  # 显示子窗口的文件名
        # ---- 断开上一个窗口的信号连接 ----
        try:
            self.fun.ClickAppendPb.disconnect()
            self.fun.ClickKeySignal.disconnect()
            # print("上一个窗口组件信号已解除")
        except TypeError as e:  # 新信号切换依旧有NoneType的问题
            print(e)
        except Exception as e:
            print(e)
        # ---- 当前激活窗口的信号连接 ----
        self.fun.ClickAppendPb.connect(curmdiwidget.tE.insertPlainText)
        self.fun.ClickKeySignal.connect(curmdiwidget.tE.insertPlainText)
        # print("当前窗口组件信号已连接")  # 这里一个 多态  如果不注释的 下面调用父类的方法后就会有两个print
        super().on_mdi_subWindowActivated(mdisubwindow)

    # def on_act_ViewHelp_triggered(self):
    #     pass
    #     # 打开一个新窗口里面有一个label 但是帮助菜单该怎么写



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QMyFunDoc()
    form.show()
    sys.exit(app.exec_())
