import sys
from PyQt5.QtWidgets import QDialog, QApplication, QGridLayout, QGroupBox, QPushButton, QDesktopWidget, QComboBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from function.ui_selectdialog import Ui_Dialog
from function.Enmu_Key import NeedShift, DKPB


class QMySelectDialog(QDialog):
    ButtonClick = pyqtSignal(list, int)
    changePBEnable = pyqtSignal(bool)  # 用于设置主窗口的Action的Enabled

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # =====================AllKey按钮生成其他按钮要用的============================
        self.gL_right = None  # 整个HorizontalLayout下有左边和右边两个Grid
        self.board_group = None  # 布局下的两个group
        self.pad_group = None
        self.boardgridLayout = None  # 两个组分别一个layout 用于添加组件
        self.padgridLayout = None
        self._DialogAontherButton = None  # 用来存按钮实例的

        # =============界面所有按钮连接信号的适配=================
        # 目前排除了 其他按键 清空 和 添加
        self._pblist = self.findChildren(QPushButton)
        for i in range(len(self._pblist)):
            pbname = self._pblist[i].objectName()
            if pbname != "AllKey" and pbname != "clear" and pbname != "append":
                self._pblist[i].clicked.connect(lambda: self.ShowKey(self.sender().text()))

        # ==================界面四个组合框连接信号的适配=====================
        self._cblist = self.findChildren(QComboBox)
        for i in range(len(self._cblist)):
            self._cblist[i].activated.connect(lambda: self.ShowKey(self.sender().currentText()))
        # 对话框窗口 不更新的话 就这样定了
        self._rtspb = []  # ready to send pushbutton
        self.num = 0

        # ==== 新编辑框的代码 ====
        # self.ButtonClick.connect(self.signaltest)

    # ==========================自动连接的槽函数==========================
    @pyqtSlot()
    def on_AllKey_clicked(self):  # test     !!!!!!!!!!! 测试
        # ==============创建这个对话框的其他按钮=================
        if self.gL_right is None:
            self.gL_right = QGridLayout()
            self.board_group = QGroupBox("KeyBoard", self)
            self.boardgridLayout = QGridLayout()
            self.pad_group = QGroupBox("KeyPad", self)
            self.padgridLayout = QGridLayout()
            self._DialogAontherButton = [x for x in range(len(DKPB))]
            k = list(DKPB.keys())
            v = list(DKPB.values())
            r = c = status = 0
            for i in range(len(self._DialogAontherButton)):
                self._DialogAontherButton[i] = QPushButton(k[i], self)  # 创建时 写上按钮名字
                self._DialogAontherButton[i].setToolTip(v[i])  # 设置tt后就是连接信号
                self._DialogAontherButton[i].clicked.connect(lambda: self.ShowKey(self.sender().text()))
                if status == 0:
                    self.boardgridLayout.addWidget(self._DialogAontherButton[i], r, c)
                else:
                    self.padgridLayout.addWidget(self._DialogAontherButton[i], r, c)
                c += 1
                if c == 9:
                    c = 0
                    r += 1
                if v[i] == "A4":  # A4是最后一个keyboard
                    status = 1  # 改变status后 新的pb会添加到pad的格子布局中
                    c = 0  # 行和列的计数 也都在 pad布局中重新计算
                    r = 0
                if v[i] == "DD":  # 到了DD就说明keypad的按键也生成完毕了 加一个break是因为后面还有要判读 是否需要定义的附加元素
                    break

            self.board_group.setLayout(self.boardgridLayout)  # 组 加 布局 加 顶级布局
            self.pad_group.setLayout(self.padgridLayout)
            self.gL_right.addWidget(self.board_group)
            self.gL_right.addWidget(self.pad_group)
            self.ui.horizontalLayout.addLayout(self.gL_right)

        # =============重复点击后 按钮是否可见==========================
        if self.board_group.isVisible():
            self.setMaximumSize(408, 403)
            self.board_group.setVisible(False)
            self.pad_group.setVisible(False)
        else:
            self.board_group.setVisible(True)
            self.pad_group.setVisible(True)

        # =======设置窗体居中于屏幕中心 并且还原大小=============
        self.adjustSize()
        window = self.frameGeometry()
        point = QDesktopWidget().availableGeometry().center()
        window.moveCenter(point)
        self.move(window.topLeft())

    # @pyqtSlot()
    # def on_AllKey_clicked(self):
    #     # ==============创建这个对话框的其他按钮=================
    #     if self.gL_right is None:
    #         self.gL_right = QGridLayout()
    #         self.board_group = QGroupBox("KeyBoard", self)
    #         self.boardgridLayout = QGridLayout()
    #         self.pad_group = QGroupBox("KeyPad", self)
    #         self.padgridLayout = QGridLayout()
    #         self._DialogAontherButton = [x for x in range(len(DialogKeyPushButton))]
    #         k = list(DialogKeyPushButton.keys())
    #         v = list(DialogKeyPushButton.values())
    #         r = c = status = 0
    #         for i in range(len(self._DialogAontherButton)):
    #             self._DialogAontherButton[i] = QPushButton(v[i], self)  # 创建时 写上按钮名字
    #             self._DialogAontherButton[i].setToolTip(k[i])  # 设置tt后就是连接信号
    #             self._DialogAontherButton[i].clicked.connect(lambda: self.ShowKey(self.sender().text()))
    #             if status == 0:
    #                 self.boardgridLayout.addWidget(self._DialogAontherButton[i], r, c)
    #             else:
    #                 self.padgridLayout.addWidget(self._DialogAontherButton[i], r, c)
    #             c += 1
    #             if c == 9:
    #                 c = 0
    #                 r += 1
    #             if k[i] == "E7":  # E7是最后一个keyboard
    #                 status = 1  # 改变status后 新的pb会添加到pad的格子布局中
    #                 c = 0  # 行和列的计数 也都在 pad布局中重新计算
    #                 r = 0
    #
    #         self.board_group.setLayout(self.boardgridLayout)  # 组 加 布局 加 顶级布局
    #         self.pad_group.setLayout(self.padgridLayout)
    #         self.gL_right.addWidget(self.board_group)
    #         self.gL_right.addWidget(self.pad_group)
    #         self.ui.horizontalLayout.addLayout(self.gL_right)
    #
    #     # =============重复点击后 按钮是否可见==========================
    #     if self.board_group.isVisible():
    #         self.setMaximumSize(408, 403)
    #         self.board_group.setVisible(False)
    #         self.pad_group.setVisible(False)
    #     else:
    #         self.board_group.setVisible(True)
    #         self.pad_group.setVisible(True)
    #
    #     # =======设置窗体居中于屏幕中心 并且还原大小=============
    #     self.adjustSize()
    #     window = self.frameGeometry()
    #     point = QDesktopWidget().availableGeometry().center()
    #     window.moveCenter(point)
    #     self.move(window.topLeft())

    @pyqtSlot()
    def on_append_clicked(self):
        self.num = 0
        if self.ui.stroke.isChecked():  # 三个单选按钮
            self.num = 0
        elif self.ui.press.isChecked():
            self.num = 1
        elif self.ui.release.isChecked():
            self.num = 2
        self.ButtonClick.emit(self._rtspb, self.num)

    @pyqtSlot()
    def on_clear_clicked(self):
        self.ui.lineEdit.clear()
        self._rtspb.clear()

    # ==========================自定义槽函数==========================
    def ShowKey(self, name):  # 记得添加列表
        if name in NeedShift:  # 如果想输入列表中的字符 是需要在后面加上一个shift才能通过sendstorke发送的
            print(NeedShift[name])
            self.ShowKey(NeedShift[name])
            self.ShowKey("Shift")
            return
        self._rtspb.append(name)
        pre = self.ui.lineEdit.text()
        if len(pre) == 0:
            self.ui.lineEdit.setText(name)
        else:
            name = pre + "+" + name
            self.ui.lineEdit.setText(name)

    # @pyqtSlot(list, int)
    # def signaltest(self, keylist, num):
    #     print("======signaltest=======")
    #     print(keylist)
    #     print(num)
    #     print("第三个数字是状态")
    #     # print(status)
    #     print("==============")

    def showEvent(self, event):  # 对话框显示事件
        self.changePBEnable.emit(False)
        super().showEvent(event)

    def closeEvent(self, event):  # 对话框关闭事件
        self.changePBEnable.emit(True)  # 用于开启按钮的信号
        super().closeEvent(event)


# ============窗体测试程序 ==============================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QMySelectDialog()
    form.show()
    sys.exit(app.exec_())
