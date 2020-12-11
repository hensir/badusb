import sys

from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, QPushButton, QGridLayout, QComboBox, QDesktopWidget
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QRect
from ui_keyDialog import Ui_Dialog
from KEY import DialogKeyPushButton


class QmyDialog(QDialog):
    ButtonClick = pyqtSignal(str)
    ComBoxClick = pyqtSignal(str)
    changeActionEnable = pyqtSignal(bool)  # 用于设置主窗口的Action的Enabled

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Dialog()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.size = self.size()
        # self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)  # 更窄的边框
        self.setWindowTitle("按键对话框")  # 标题
        self.ui.gridLayout_2.setRowStretch(4, 10)  # 设置布局 行大小自动扩展

        # =============界面所有按钮连接信号的适配(除了那个功能按钮）=================
        self._pblist = self.findChildren(QPushButton)
        for i in range(len(self._pblist)):
            # TODO clicked作为一个bool str参数是怎么传过去的
            # TODO 有了这个lambda后 就都不一样了
            if self._pblist[i].objectName() != "AllKey":
                self._pblist[i].clicked.connect(lambda: self.sendname(self.sender().text()))
        # ==================界面四个组合框连接信号的适配=====================
        self._cblist = self.findChildren(QComboBox)
        for i in range(len(self._cblist)):
            self._cblist[i].activated.connect(lambda: self.sendname(self.sender().currentText()))
        # =====================AllKey按钮生成其他按钮要用的============================
        self.gL_right = None  # 整个HorizontalLayout下有左边和右边两个Grid
        self.board_group = None  # 布局下的两个group
        self.pad_group = None
        self.boardgridLayout = None  # 两个组分别一个layout 用于添加组件
        self.padgridLayout = None
        self._DialogAontherButton = None  # 用来存按钮的

    @pyqtSlot()
    def on_AllKey_clicked(self):
        # ==============创建这个对话框的其他按钮=================
        if self.gL_right is None:
            self.gL_right = QGridLayout()
            self.board_group = QGroupBox("KeyBoard", self)
            self.boardgridLayout = QGridLayout()
            self.pad_group = QGroupBox("KeyPad", self)
            self.padgridLayout = QGridLayout()
            self._DialogAontherButton = [x for x in range(len(DialogKeyPushButton))]
            k = list(DialogKeyPushButton.keys())
            v = list(DialogKeyPushButton.values())
            r = c = status = 0
            for i in range(len(self._DialogAontherButton)):
                self._DialogAontherButton[i] = QPushButton(v[i], self)
                self._DialogAontherButton[i].setToolTip(k[i])
                if status == 0:
                    self.boardgridLayout.addWidget(self._DialogAontherButton[i], r, c)
                else:
                    self.padgridLayout.addWidget(self._DialogAontherButton[i], r, c)
                c += 1
                if c == 9:
                    c = 0
                    r += 1
                if k[i] == "E7":
                    status = 1
                    c = 0
                    r = 0

            self.board_group.setLayout(self.boardgridLayout)
            self.pad_group.setLayout(self.padgridLayout)
            self.gL_right.addWidget(self.board_group)
            self.gL_right.addWidget(self.pad_group)
            self.ui.horizontalLayout.addLayout(self.gL_right)

        # =============按钮是否可见==========================
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

    def sendname(self, name):
        name = "Key_" + name  # 合并字符串
        if self.ui.press.isChecked():  # 三个单选按钮
            name = "DigiKeyboard.sendKeyPress(%s);\n" % name
        elif self.ui.release.isChecked():
            name = "DigiKeyboard.sendKeyPress(0);\n"
        elif self.ui.stroke.isChecked():
            name = "DigiKeyboard.sendKeyStroke(%s);\n" % name
        self.ButtonClick.emit(name)

    def showEvent(self, event):  # 对话框显示事件
        self.changeActionEnable.emit(False)
        super().showEvent(event)

    def closeEvent(self, event):  # 对话框关闭事件
        self.changeActionEnable.emit(True)
        super().closeEvent(event)

    def __del__(self):
        print("窗口关闭")


# ============窗体测试程序 ==============================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyDialog()
    form.show()
    sys.exit(app.exec_())
