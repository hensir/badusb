import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFontDialog, QPushButton, QStyleFactory
from PyQt5.QtCore import pyqtSlot, Qt, QEvent, pyqtSignal
from ui_mainwindow import Ui_MainWindow
from myKeyDialog import QmyDialog
from KEY import KeyShowdict, KeyInputdict, BadUSBCodes, DNDefine, ENDConst, KDT
from DuckToDigi import Duckyspark_translator


# TODO 三 有优化的地方 按键处理 看一下 显示在textEdit的前一步 合成最终的input按键
# TODO    可以使用 一 个函数 把所有的按键信号都链接过来 这样我们的三个窗口就只用一个合成函数了
# TODO 这两步是一块的  define兼容那边可能有点问题 所有还是先把那个槽函数写出来 在考虑合并吧 槽函数选择特征值太憨

# TODO 上面的先不管  我们还是恢复过来 一个信号一个槽函数 te对接一个吧


class QmyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.__dialog = None  # 对话框占位
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.setWindowTitle("BadUSB代码生成")  # 标题
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)  # 更窄的边框
        self.ui.le_ci.setPlaceholderText("Ctrl+Shift+A")  # 按键识别输入占位符
        self.ui.le_ps.setPlaceholderText("echo HelloWorld")  # 打印字符串占位符
        self.ui.le_ci.installEventFilter(self)  # 注册监控器 供le_ci获取按键
        self._KeyBoardStatus = 0  # 按键状态
        self._keystring = ""  # 用来传值的 发送给 组合框单击打印的
        self._Definedconst = []

        self.sB_label = QLabel(self)  # 放在状态栏中的标签
        self.ui.statusBar.addPermanentWidget(self.sB_label)

    def eventFilter(self, watched, event):
        if watched == self.ui.le_ci:  # 如果当前监测对象为
            # ==================== 按键按下 =======================
            if event.type() == QEvent.KeyPress:
                if self._KeyBoardStatus == 1:  # status为1 就会开启新一轮叠加
                    self.ui.le_ci.clear()  # 新一轮 需要清除编辑框
                    self._keystring = ""  # 和这个用于打印到textEdit上的字符串
                # ========================================
                if self.ui.cb_ci_ap.currentIndex() == 1:  # 索引值为1 的时候只能输入一个按键
                    self.ui.le_ci.clear()  # 把上一个press给清除掉了
                # ===================组合input要用的字符串=====================
                if len(self._keystring) == 0:
                    self._keystring = "%s" % KeyInputdict[event.key()]
                else:
                    self._keystring += ", %s" % KeyInputdict[event.key()]
                # =================↓组合show要用的字符串↓=======================
                showstr = self.ui.le_ci.text()
                if len(showstr) == 0:  # 当前编辑框是空的
                    if len(KeyShowdict[event.key()]) == 1:  # 编辑框为空时也需要屏蔽 按键重复
                        showstr = showstr
                    else:  # 否则这是个“不可打印字符”
                        showstr = KeyShowdict[event.key()]
                else:  # 编辑框里 有按键了
                    if showstr == "Ctrl" or showstr == "Ctrl+Shift":  # 这个按键 为
                        showstr = showstr + "+" + KeyShowdict[event.key()]
                    elif len(KeyShowdict[event.key()]) == 1:  # 这个按键是 单个的 用于判断 “可打印字符”
                        showstr = showstr + "+"
                    else:  # 这个是放行 shift alt tab等这些的
                        showstr = showstr + "+" + KeyShowdict[event.key()]
                self.ui.le_ci.setText(showstr)
                # ================适配=========================
                print("按键%s按下" % KeyShowdict[event.key()])  # 两个用来汇报的 日志
                self.sB_label.setText("按键%s按下" % KeyShowdict[event.key()])  # 状态栏
                self._KeyBoardStatus = 0  # 初始化键盘状态 不会开启新一轮叠加

            # ==================== 按键松开 =======================
            if event.type() == QEvent.KeyRelease:
                self._KeyBoardStatus = 1  # 目前的这三行 都是为了这个新一轮的叠加 那么最终呈现效果
                print("按键%s松开" % KeyShowdict[event.key()])
                self.sB_label.setText("按键%s松开" % KeyShowdict[event.key()])
        return super().eventFilter(watched, event)

    @pyqtSlot()
    def on_pb_od_clicked(self):
        """这个是 点击输入按钮"""
        self.__dialog = QmyDialog(self)  # 按键对话框
        self.__dialog.setAttribute(Qt.WA_DeleteOnClose)  # 对话框关闭时自动删除
        self.__dialog.ButtonClick.connect(self.MainInput)
        self.__dialog.changePBEnable.connect(self.do_setPBEnable)
        self.__dialog.show()

    @pyqtSlot()
    def on_pb_sp_ap_clicked(self):
        """这个按钮是 延时按钮"""
        ms = "DigiKeyboard.delay(%d);\n" % self.ui.sp_ms.value()
        self.ui.TextEdit.insertPlainText(ms)

    @pyqtSlot()
    def on_pb_ps_ap_clicked(self):
        """这个按钮是 打印字符串"""
        if len(self.ui.le_ps.text()) != 0:
            mystring = "DigiKeyboard.println(\"%s\");\n" % self.ui.le_ps.text()
            self.ui.TextEdit.insertPlainText(mystring)

    @pyqtSlot(int)
    def on_cb_ci_ap_activated(self, num):
        """单击 按下 松开"""
        if num == 0:
            keylist = list(self._keystring.split(","))
            self.MainInput(keylist, num, 0)
        elif num == 1:
            self.MainInput(self._keystring, num, 0)
        elif num == 2:  # 如果当前选项为 松开 则禁用编辑框
            self.ui.le_ci.setEnabled(False)
        else:
            self.ui.le_ci.setEnabled(True)
        # TODO 这里也是要有一个暂存区的

    @pyqtSlot(int)
    def on_cb_ci_ap_currentIndexChanged(self, index):
        """
        组合框当前项改变 因为每个选项都有不同的输入要求 所以 我们直接把存储字符串数值的
        两个变量给清除掉了   要记得 一个是用于 编辑框显示的 show  另一个是实际打印到TextEdit的input
        """
        self.ui.le_ci.clear()
        self._keystring = ""

    @pyqtSlot()
    def on_action_font_triggered(self):
        inifont = self.ui.TextEdit.font()
        font, ok = QFontDialog.getFont(inifont)
        if ok:
            self.ui.TextEdit.setFont(font)

    @pyqtSlot()
    def on_pb_dtd_clicked(self):
        duckystr = self.ui.TextEdit.toPlainText()
        digistr = Duckyspark_translator(duckystr)
        self.ui.TextEdit.setPlainText(digistr)

    @pyqtSlot(list, int, int)
    def MainInput(self, keylist, num, status):
        # if len(keylist) == 0 and num != 2:  # 如果编辑框为空 而且 当前是第三
        #     return

        # TODO 如果当前状态是松开 点击任何一个键都是 num = 2 上面这个判断我先不做
        # TODO 依旧是0号字符串 我们现在知道了 先人的思路 首先keylist
        # TODO 一个大麻烦是 这个 0号字符串的规范 我们的规范牵扯的转换实在是太多了
        # TODO 显示个print 后世一个ENDConst 这里注意一下哈 ENDConst智能接收主界面的
        # TODO 那个lineedit
        # TODO 独立 DND和END都是给编辑框准备的 而不是对话框 如果我们不处理对话框 直接从主界面
        # TODO 传出现在的数值 是不是还是能用的
        # TODO 首先我是希望这keydialog是可以复用的 所以keydialog就只负责传送正常的按键字符
        # TODO 所以转换就有maininput来做了
        # TODO 记得 这个keydialog有几个主键盘按键是没有tooltip的 所以 不管(先)
        # TODO ctrl和那几个不需要的声明的 好像是需要if独立判断的
        # TODO 现在maininput把这个本地给做出来吧

        print("======================")
        print(keylist)
        print(num)
        print(status)
        print("======================")  # 接收成功

        # 处理以下对话框 对他进行一个追加 key 然后是 upper
        # 还是先看keystring
        if status == 1:
            self._keystring = ""
            for key in keylist:
                if key in ("Ctrl", "Shift", "Alt", "Win", "Space", "Enter"):
                    if len(self._keystring) == 0:
                        self._keystring = KDT[key]
                    else:
                        self._keystring += ", " + KDT[key]
                else:
                    if len(self._keystring) == 0:
                        self._keystring = "KEY_" + key.upper()
                    else:
                        self._keystring += ", KEY_" + key.upper()

        if num == 0:
            mystring = "DigiKeyboard.sendKeyStroke(%s);\n" % self._keystring
            self.ui.TextEdit.insertPlainText(mystring)
        elif num == 1:
            mystring = "DigiKeyboard.sendKeyPress(%s);\n" % self._keystring
            self.ui.TextEdit.insertPlainText(mystring)
        elif num == 2:
            mystring = "DigiKeyboard.sendKeyPress(0);\n"
            self.ui.TextEdit.insertPlainText(mystring)


        for key in keylist:
            key = key.lstrip()
            if key in DNDefine:
                print("当前按键" + key + "已被头文件定义")
                continue  # 如果这个按键在这个列表中就不 定义 了
            else:
                print("当前按键" + key + "未被头文件定义")
                try:
                    if ENDConst[key] not in self._Definedconst:
                        print("当前按键" + key + "已被软件定义")
                        text = list(self.ui.TextEdit.toPlainText().split('\n'))
                        pos = text.index("#include \"DigiKeyboard.h\"") + 1  # 这是一个列表 所以注意 加一之后的位置
                        text.insert(pos, "#define %s %s" % (key, ENDConst[key]))  # 在指定位置插入define
                        self.ui.TextEdit.clear()
                        self.ui.TextEdit.insertPlainText("\n".join(text))  # 给TextEdit刷新以下
                        self._Definedconst.append(ENDConst[key])  # 添加到列表中 以判断是否重复定义
                    else:
                        continue
                except KeyError:
                    continue

    @pyqtSlot(bool)
    def do_setPBEnable(self, enable):
        self.ui.pb_od.setEnabled(enable)

    # =========快捷按钮 1234=================
    @pyqtSlot()  # 这里也可以用数组处理 因为代码太重复了 完全可以遍历操作
    def on_pb_qc1_clicked(self):
        self.ui.TextEdit.clear()
        self._Definedconst.clear()  # 清空这个统计之后就能继续使用defind的功能了
        payload = BadUSBCodes[2]
        self.ui.TextEdit.insertPlainText(payload)

    @pyqtSlot()
    def on_pb_qc2_clicked(self):
        self.ui.TextEdit.clear()
        self._Definedconst.clear()
        payload = BadUSBCodes[1]
        self.ui.TextEdit.insertPlainText(payload)

    @pyqtSlot()
    def on_pb_qc3_clicked(self):
        self.ui.TextEdit.clear()
        self._Definedconst.clear()
        payload = BadUSBCodes[3]
        self.ui.TextEdit.insertPlainText(payload)

    @pyqtSlot()
    def on_pb_qc4_clicked(self):
        self.ui.TextEdit.clear()
        self._Definedconst.clear()
        payload = BadUSBCodes[0]
        self.ui.TextEdit.insertPlainText(payload)


if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyMainWindow()  # 创建窗体
    QApplication.setStyle(QStyleFactory.create("windowsvista"))
    form.show()
    sys.exit(app.exec_())
