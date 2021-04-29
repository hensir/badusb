import sys
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QListWidgetItem

from document.myDocument import QMyDocument  # mdi文档
from document.myFromDoc import FromDoc  # 小组件需要升个级

from function.Enmu_Key import GlobalReplacement, DKPB
from function.myFunction import QMyFunction  # 功能区组件
from function.CodeList import DigiKeyboardH
from function.mySelectDialog import QMySelectDialog

# 这个 包导入不对劲
# duckytodigi的反向操作 不就可以生成ducky的脚本了吗


class QMyFunDoc(QMyDocument):
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
        # ---- 设置功能区信号连接 ----
        self.fun.ui.toDigiPB.clicked.connect(self.toDigiPB_clicked)
        self.fun.ui.ClickToInPB.clicked.connect(self.ClickToInPB_clicked)
        self.fun.ui.LSEPushButton.clicked.connect(self.LSEPushButton_clicked)
        self.fun.ui.SSBPButton.clicked.connect(self.SSBPButton_clicked)
        self.fun.ui.CListWidget.itemDoubleClicked.connect(self.CListWidget_itemDoubleClicked)
        self.fun.ui.PBComboBox.activated.connect(self.PBComboBox_activated)

    def toDigiPB_clicked(self):
        title = self.formDoc.windowTitle()
        text = self.formDoc.tE.toPlainText()
        if len(self.ui.mdi.subWindowList()) > 0:  # 如果有打开的MDI窗口，获取活动窗口
            self.formDoc = self.ui.mdi.activeSubWindow().widget()
            needNew = self.formDoc.isFileOpened()  # 文件已经打开，需要新建窗口
        else:
            needNew = True  # # 是否需要新建子窗口
        if needNew:
            self.formDoc = FromDoc(self)  # 必须指定父窗口
            self.ui.mdi.addSubWindow(self.formDoc)  # 添加到MDI区域
        self.formDoc.setWindowTitle(title + "_Ducky")
        self.formDoc.tE.setText(text)
        self.formDoc.show()

    def LSEPushButton_clicked(self):
        text2 = "DigiKeyboard.print(\"%s\");" % (self.fun.ui.LineStrEdit.text())
        self.formDoc.tE.insertPlainText(text2 + "\n")

    def SSBPButton_clicked(self):
        text2 = r"DigiKeyboard.delay(%s);" % (self.fun.ui.SleepSpinBox.value())
        self.formDoc.tE.insertPlainText(text2 + "\n")

    @pyqtSlot(QListWidgetItem)
    def CListWidget_itemDoubleClicked(self, item):
        listitem = item.data(Qt.UserRole)
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

    @pyqtSlot(int)
    def PBComboBox_activated(self, keytype):
        ShortCutList = [x.split('+') for x in
                        self.fun.ui.KeySeqEdit.keySequence().toString().split(',')]  # short cut list
        ShortCutList = ["".join(x.split()) for i in ShortCutList for x in i]
        # for嵌套的列表推导式 注 前一for迭代值是后一for的迭代器 最后又加了一个list转str
        self.KeySignal(ShortCutList, keytype)

    def ClickToInPB_clicked(self):
        """这个是 点击输入按钮"""
        self.__dialog = QMySelectDialog()  # 按键对话框
        self.__dialog.setAttribute(Qt.WA_DeleteOnClose)  # 对话框关闭时自动删除
        self.__dialog.ButtonClick.connect(self.KeySignal)
        self.__dialog.changePBEnable.connect(self.fun.ui.ClickToInPB.setEnabled)
        self.__dialog.show()

    @pyqtSlot()  # “新建文档”
    def on_act_New_triggered(self):
        self.formDoc = FromDoc(self)
        self.formDoc.setWindowTitle("无标题" + str(self.mdiTitleindex))
        self.formDoc.tE.setText("""#include "DigiKeyboard.h"\nvoid setup() {\n\n}\n\nvoid loop() {\n\n}\n""")
        self.mdiTitleindex += 1
        self.ui.mdi.addSubWindow(self.formDoc)  # 文档窗口添加到MDI
        self.formDoc.show()  # 在单独的窗口中显示

    @pyqtSlot(list, int)
    def KeySignal(self, text2send, keytype):  # 没事了 咱做个检测 当然要在上层显示 这里马上就要发信号了

        try:
            print(self.formDoc.defined)
        except AttributeError:
            self.formDoc.defined = []

        status = False
        patchtext = ""
        for i in range(len(text2send)):
            if text2send[i] in GlobalReplacement:
                print("GlobalReplacement", text2send[i])
                text2send[i] = GlobalReplacement[text2send[i]]
            elif text2send[i] in DKPB:
                if text2send[i] in self.formDoc.defined:
                    text2send[i] = "key_" + text2send[i]
                    continue
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
        else:
            text = "DigiKeyboard.sendKeyPress(0);"
        self.formDoc.tE.insertPlainText(text + "\n")
        if status:
            self.formDoc.tE.moveCursor(QTextCursor.Start, QTextCursor.MoveAnchor)
            self.formDoc.tE.insertPlainText(patchtext + "\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QMyFunDoc()
    form.show()
    sys.exit(app.exec_())
