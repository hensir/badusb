import sys

from PyQt5.QtCore import pyqtSlot, QDir, QFile, QIODevice
from PyQt5.QtGui import QTextOption
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMdiArea, QMessageBox

from myFromDoc import FromDoc
from ui_document import Ui_MainWindow


# if len(self.ui.mdi.subWindowList()) > 0:  # 如果有打开的MDI窗口，获取活动窗口
#     self.formDoc = self.ui.mdi.activeSubWindow().widget()
# 把这个东西做成一个装饰器 称为 子窗口操作保险装饰器
# 新窗口 页面设置 打印 使用bing搜索 转到 查找等功能都没做

# 自动换行有一个 setWordWrapMode    def setLineWrapMode (mode)


class QMyDocument(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mdi.setActivationOrder(QMdiArea.ActivationHistoryOrder)
        self.mdiTitleindex = 1  # 窗口标题索引
        self.formDoc = None  # 当前已激活的窗口指针

        # 简单的本窗口信号连接
        self.ui.act_LevelExpansion.triggered.connect(self.ui.mdi.cascadeSubWindows)  # 层级排列窗口
        self.ui.act_FlatOut.triggered.connect(self.ui.mdi.tileSubWindows)  # 平铺排列窗口
        self.ui.act_StatusBar.triggered.connect(
            lambda: self.ui.StatusB.setVisible(not (self.ui.StatusB.isVisible())))  # 显示/关闭状态栏
        self.ui.act_CloseAll.triggered.connect(self.ui.mdi.closeAllSubWindows)  # 关闭所有子窗口

    #  ==========由connectSlotsByName() 自动连接的槽函数==================
    @pyqtSlot()  # “新建文档”
    def on_act_New_triggered(self):
        self.formDoc = FromDoc(self)
        self.formDoc.setWindowTitle("无标题" + str(self.mdiTitleindex))
        self.mdiTitleindex += 1
        self.ui.mdi.addSubWindow(self.formDoc)  # 文档窗口添加到MDI
        self.formDoc.show()  # 在单独的窗口中显示

        # ---- 子窗口信号连接 ----

    @pyqtSlot()  # “打开文档”
    def on_act_Open_triggered(self):
        if len(self.ui.mdi.subWindowList()) > 0:  # 如果有打开的MDI窗口，获取活动窗口
            self.formDoc = self.ui.mdi.activeSubWindow().widget()
            needNew = self.formDoc.isFileOpened()  # 文件已经打开，需要新建窗口
        else:
            needNew = True  # # 是否需要新建子窗口
        filename, flt = QFileDialog.getOpenFileName(self, "打开一个文件", QDir.currentPath(),
                                                    "文本文件(*.cpp *.h *.py);;所有文件(*.*)")
        if filename == "":
            return
        # 这里做一个 重复打开文件的检测
        for window in self.ui.mdi.subWindowList():
            widget = window.widget()
            if filename == widget.currentFilePath:
                QMessageBox.warning(self, "提示", "该文件已打开,不允许脏写")
                return
        if needNew:
            self.formDoc = FromDoc(self)  # 必须指定父窗口
            self.ui.mdi.addSubWindow(self.formDoc)  # 添加到MDI区域
        self.formDoc.loadFromFile(filename)
        self.formDoc.show()

    @pyqtSlot()
    def on_act_Save_triggered(self):  # 如果当前路径没有这个标题的文件就调出getfiledialog
        if len(self.ui.mdi.subWindowList()) > 0:  # 如果有打开的MDI窗口，获取活动窗口
            self.formDoc = self.ui.mdi.activeSubWindow().widget()

        # 从这里开始取文件路径 然后就是setcurrentpath 我觉得可以搞一个绝对路径
        # 先取出这个子窗口的 文件绝对路径 然后追加
        # 当然也要判断这个 文件绝对路径是否存在啊 因为是有这个无标题存在的
        if len(self.formDoc.currentFilePath):
            print(self.formDoc.currentFilePath)

        cursubwidget = self.formDoc.currentFilePath
        if QFile.exists(cursubwidget):  # 存在就直接保存
            print(cursubwidget)
            fileDevice = QFile(cursubwidget)
            if not fileDevice.open(QIODevice.WriteOnly | QIODevice.Text):
                return False
            try:
                text = self.formDoc.tE.toPlainText()  # 返回str类型
                strBytes = text.encode("utf-8")  # str转换为bytes类型
                fileDevice.write(strBytes)  # 写入文件
            finally:
                fileDevice.close()
            return True
        else:
            self.on_act_SaveAs_triggered()  # 如果当前路径不存在

    @pyqtSlot()
    def on_act_SaveAs_triggered(self):
        if len(self.ui.mdi.subWindowList()) > 0:  # 如果有打开的MDI窗口，获取活动窗口
            self.formDoc = self.ui.mdi.activeSubWindow().widget()
        curPath = QDir.currentPath()  # 获取系统当前目录
        title = "另存为一个文件"  # 对话框标题
        filt = "Python程序(*.py);; C++程序(*.h *.cpp);;文本文件(*.txt);;所有文件(*.*)"  # 文件过滤器
        fileName, flt = QFileDialog.getSaveFileName(self, title, curPath, filt)
        print(fileName)
        if fileName == "":
            return
        try:
            fileDevice = QFile(fileName)
            if not fileDevice.open(QIODevice.WriteOnly | QIODevice.Text):
                return False
            try:
                text = self.formDoc.tE.toPlainText()  # 返回str类型
                strBytes = text.encode("utf-8")  # str转换为bytes类型
                fileDevice.write(strBytes)  # 写入文件
            finally:
                fileDevice.close()
        except Exception as e:
            print(e)
            QMessageBox.critical(self, "错误", "保存文件失败")
        else:
            print("保存成功")
            self.formDoc.loadFromFile(fileName)
            # 有两种可能会触发这个槽函数 一个是新建的文档图方便 直接偷懒使用了这个另存为的槽函数 连标题名字都没有换
            # 另一个信号是 本另存为 下载我最后这个loadfromfile 解决了不管是那个信号出发的 都会重新加载这个文件
            # 它们都符合一个很重要的特征 就是 都是已经保存过的文件

    @pyqtSlot(bool)  # “MDI模式”
    def on_act_Mdi_triggered(self):
        if self.ui.mdi.viewMode() == QMdiArea.SubWindowView:  # Tab多页显示模式
            self.ui.mdi.setViewMode(QMdiArea.TabbedView)  # Tab多页显示模式
            self.ui.mdi.setTabsClosable(True)  # 页面可关闭
        else:  # 子窗口模式
            self.ui.mdi.setViewMode(QMdiArea.SubWindowView)  # 子窗口模式

    @pyqtSlot()
    def on_act_Wrap_triggered(self):

        pass

    # @pyqtSlot(type)
    def on_mdi_subWindowActivated(self, mdisubwindow):  # 参数为当前激活窗口
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
        try:  # 这个地方 其实改写 也简单 就是on_act_Undo的槽函数 然后函数里面有个form指向当前窗口 进行一个tE.undo 重复的写一下就好了
            self.ui.act_Undo.triggered.disconnect()  # 或者是我没写下来的那个 就是可以检测一个槽函数有没有被链接的状态
            self.ui.act_Redo.triggered.disconnect()
            self.ui.act_Cut.triggered.disconnect()
            self.ui.act_Copy.triggered.disconnect()
            self.ui.act_Paste.triggered.disconnect()
            self.ui.act_SelectAll.triggered.disconnect()
            self.ui.act_Font.triggered.disconnect()
            self.ui.act_ZoomIn.triggered.disconnect()
            self.ui.act_ZoomOut.triggered.disconnect()
            self.ui.act_DefaultZoom.triggered.disconnect()
            self.ui.act_Wrap.triggered.disconnect()
            print("上一个窗口组件信号已解除")
        except TypeError as e:
            print(e)
        except Exception as e:
            print(e)

        # ---- 当前激活窗口的信号连接 ----
        self.ui.act_Undo.triggered.connect(curmdiwidget.tE.undo)
        self.ui.act_Redo.triggered.connect(curmdiwidget.tE.redo)
        self.ui.act_Cut.triggered.connect(curmdiwidget.tE.cut)
        self.ui.act_Copy.triggered.connect(curmdiwidget.tE.copy)
        self.ui.act_Paste.triggered.connect(curmdiwidget.tE.paste)
        self.ui.act_SelectAll.triggered.connect(curmdiwidget.tE.selectAll)
        self.ui.act_Font.triggered.connect(curmdiwidget.textSetFont)
        self.ui.act_ZoomIn.triggered.connect(curmdiwidget.tE.zoomIn)
        self.ui.act_ZoomOut.triggered.connect(curmdiwidget.tE.zoomOut)
        self.ui.act_DefaultZoom.triggered.connect(lambda: curmdiwidget.tE.setFont(curmdiwidget.font))
        self.ui.act_Wrap.triggered.connect(curmdiwidget.mysetWordWrapMode)
        print("当前窗口组件信号已连接")


if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QMyDocument()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
