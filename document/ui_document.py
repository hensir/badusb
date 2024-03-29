# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'documentF.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.mdi = QtWidgets.QMdiArea(self.centralwidget)
        self.mdi.setObjectName("mdi")
        self.gridLayout.addWidget(self.mdi, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 23))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
        self.menu_O = QtWidgets.QMenu(self.menubar)
        self.menu_O.setObjectName("menu_O")
        self.menu_V = QtWidgets.QMenu(self.menubar)
        self.menu_V.setObjectName("menu_V")
        self.menus = QtWidgets.QMenu(self.menu_V)
        self.menus.setObjectName("menus")
        self.menu_H = QtWidgets.QMenu(self.menubar)
        self.menu_H.setObjectName("menu_H")
        MainWindow.setMenuBar(self.menubar)
        self.StatusB = QtWidgets.QStatusBar(MainWindow)
        self.StatusB.setObjectName("StatusB")
        MainWindow.setStatusBar(self.StatusB)
        self.act_New = QtWidgets.QAction(MainWindow)
        self.act_New.setObjectName("act_New")
        self.act_New_Window = QtWidgets.QAction(MainWindow)
        self.act_New_Window.setObjectName("act_New_Window")
        self.act_Open = QtWidgets.QAction(MainWindow)
        self.act_Open.setObjectName("act_Open")
        self.act_Save = QtWidgets.QAction(MainWindow)
        self.act_Save.setObjectName("act_Save")
        self.act_SaveAs = QtWidgets.QAction(MainWindow)
        self.act_SaveAs.setObjectName("act_SaveAs")
        self.act_PageSetup = QtWidgets.QAction(MainWindow)
        self.act_PageSetup.setObjectName("act_PageSetup")
        self.act_Printing = QtWidgets.QAction(MainWindow)
        self.act_Printing.setObjectName("act_Printing")
        self.act_Exit = QtWidgets.QAction(MainWindow)
        self.act_Exit.setObjectName("act_Exit")
        self.act_Undo = QtWidgets.QAction(MainWindow)
        self.act_Undo.setObjectName("act_Undo")
        self.act_Cut = QtWidgets.QAction(MainWindow)
        self.act_Cut.setObjectName("act_Cut")
        self.act_Copy = QtWidgets.QAction(MainWindow)
        self.act_Copy.setObjectName("act_Copy")
        self.act_Paste = QtWidgets.QAction(MainWindow)
        self.act_Paste.setObjectName("act_Paste")
        self.act_Delete = QtWidgets.QAction(MainWindow)
        self.act_Delete.setObjectName("act_Delete")
        self.act_Bing = QtWidgets.QAction(MainWindow)
        self.act_Bing.setObjectName("act_Bing")
        self.act_Find = QtWidgets.QAction(MainWindow)
        self.act_Find.setObjectName("act_Find")
        self.act_FindNext = QtWidgets.QAction(MainWindow)
        self.act_FindNext.setObjectName("act_FindNext")
        self.act_FindPrevious = QtWidgets.QAction(MainWindow)
        self.act_FindPrevious.setObjectName("act_FindPrevious")
        self.act_Replace = QtWidgets.QAction(MainWindow)
        self.act_Replace.setObjectName("act_Replace")
        self.act_Goto = QtWidgets.QAction(MainWindow)
        self.act_Goto.setObjectName("act_Goto")
        self.act_SelectAll = QtWidgets.QAction(MainWindow)
        self.act_SelectAll.setObjectName("act_SelectAll")
        self.act_TimeDate = QtWidgets.QAction(MainWindow)
        self.act_TimeDate.setObjectName("act_TimeDate")
        self.act_Wrap = QtWidgets.QAction(MainWindow)
        self.act_Wrap.setObjectName("act_Wrap")
        self.act_Font = QtWidgets.QAction(MainWindow)
        self.act_Font.setObjectName("act_Font")
        self.act_ZoomIn = QtWidgets.QAction(MainWindow)
        self.act_ZoomIn.setObjectName("act_ZoomIn")
        self.act_ZoomOut = QtWidgets.QAction(MainWindow)
        self.act_ZoomOut.setObjectName("act_ZoomOut")
        self.act_DefaultZoom = QtWidgets.QAction(MainWindow)
        self.act_DefaultZoom.setObjectName("act_DefaultZoom")
        self.act_StatusBar = QtWidgets.QAction(MainWindow)
        self.act_StatusBar.setObjectName("act_StatusBar")
        self.act_ViewHelp = QtWidgets.QAction(MainWindow)
        self.act_ViewHelp.setObjectName("act_ViewHelp")
        self.act_Feedback = QtWidgets.QAction(MainWindow)
        self.act_Feedback.setObjectName("act_Feedback")
        self.act_About = QtWidgets.QAction(MainWindow)
        self.act_About.setObjectName("act_About")
        self.act_Redo = QtWidgets.QAction(MainWindow)
        self.act_Redo.setObjectName("act_Redo")
        self.act_Mdi = QtWidgets.QAction(MainWindow)
        self.act_Mdi.setObjectName("act_Mdi")
        self.act_LevelExpansion = QtWidgets.QAction(MainWindow)
        self.act_LevelExpansion.setObjectName("act_LevelExpansion")
        self.act_FlatOut = QtWidgets.QAction(MainWindow)
        self.act_FlatOut.setObjectName("act_FlatOut")
        self.act_CloseAll = QtWidgets.QAction(MainWindow)
        self.act_CloseAll.setObjectName("act_CloseAll")
        self.menu_F.addAction(self.act_New)
        self.menu_F.addAction(self.act_New_Window)
        self.menu_F.addAction(self.act_Open)
        self.menu_F.addAction(self.act_Save)
        self.menu_F.addAction(self.act_SaveAs)
        self.menu_F.addAction(self.act_CloseAll)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.act_PageSetup)
        self.menu_F.addAction(self.act_Printing)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.act_Exit)
        self.menu_E.addAction(self.act_Redo)
        self.menu_E.addAction(self.act_Undo)
        self.menu_E.addSeparator()
        self.menu_E.addAction(self.act_Cut)
        self.menu_E.addAction(self.act_Copy)
        self.menu_E.addAction(self.act_Paste)
        self.menu_E.addAction(self.act_Delete)
        self.menu_E.addSeparator()
        self.menu_E.addAction(self.act_Bing)
        self.menu_E.addAction(self.act_Find)
        self.menu_E.addAction(self.act_FindNext)
        self.menu_E.addAction(self.act_FindPrevious)
        self.menu_E.addAction(self.act_Replace)
        self.menu_E.addAction(self.act_Goto)
        self.menu_E.addSeparator()
        self.menu_E.addAction(self.act_SelectAll)
        self.menu_E.addAction(self.act_TimeDate)
        self.menu_O.addAction(self.act_Wrap)
        self.menu_O.addAction(self.act_Font)
        self.menus.addAction(self.act_ZoomIn)
        self.menus.addAction(self.act_ZoomOut)
        self.menus.addAction(self.act_DefaultZoom)
        self.menu_V.addAction(self.menus.menuAction())
        self.menu_V.addAction(self.act_StatusBar)
        self.menu_V.addSeparator()
        self.menu_V.addAction(self.act_Mdi)
        self.menu_V.addAction(self.act_LevelExpansion)
        self.menu_V.addAction(self.act_FlatOut)
        self.menu_H.addAction(self.act_ViewHelp)
        self.menu_H.addAction(self.act_Feedback)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.act_About)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.menubar.addAction(self.menu_O.menuAction())
        self.menubar.addAction(self.menu_V.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())

        self.retranslateUi(MainWindow)
        self.act_Exit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "无标题"))
        self.menu_F.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_E.setTitle(_translate("MainWindow", "编辑(&E)"))
        self.menu_O.setTitle(_translate("MainWindow", "格式(&O)"))
        self.menu_V.setTitle(_translate("MainWindow", "查看(&V)"))
        self.menus.setTitle(_translate("MainWindow", "缩放"))
        self.menu_H.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.act_New.setText(_translate("MainWindow", "新建"))
        self.act_New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.act_New_Window.setText(_translate("MainWindow", "新窗口"))
        self.act_New_Window.setShortcut(_translate("MainWindow", "Ctrl+Shift+N"))
        self.act_Open.setText(_translate("MainWindow", "打开..."))
        self.act_Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.act_Save.setText(_translate("MainWindow", "保存"))
        self.act_Save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.act_SaveAs.setText(_translate("MainWindow", "另存为..."))
        self.act_SaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.act_PageSetup.setText(_translate("MainWindow", "页面设置..."))
        self.act_Printing.setText(_translate("MainWindow", "打印..."))
        self.act_Printing.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.act_Exit.setText(_translate("MainWindow", "退出"))
        self.act_Undo.setText(_translate("MainWindow", "撤销"))
        self.act_Undo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.act_Cut.setText(_translate("MainWindow", "剪切"))
        self.act_Cut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.act_Copy.setText(_translate("MainWindow", "复制"))
        self.act_Copy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.act_Paste.setText(_translate("MainWindow", "粘贴"))
        self.act_Paste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.act_Delete.setText(_translate("MainWindow", "删除"))
        self.act_Delete.setShortcut(_translate("MainWindow", "Del"))
        self.act_Bing.setText(_translate("MainWindow", "使用Bing搜索..."))
        self.act_Bing.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.act_Find.setText(_translate("MainWindow", "查找..."))
        self.act_Find.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.act_FindNext.setText(_translate("MainWindow", "查找下一个"))
        self.act_FindNext.setShortcut(_translate("MainWindow", "F3"))
        self.act_FindPrevious.setText(_translate("MainWindow", "查找上一个"))
        self.act_FindPrevious.setShortcut(_translate("MainWindow", "Shift+F3"))
        self.act_Replace.setText(_translate("MainWindow", "替换"))
        self.act_Replace.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.act_Goto.setText(_translate("MainWindow", "转到"))
        self.act_Goto.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.act_SelectAll.setText(_translate("MainWindow", "全选"))
        self.act_SelectAll.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.act_TimeDate.setText(_translate("MainWindow", "时间/日期"))
        self.act_TimeDate.setShortcut(_translate("MainWindow", "F5"))
        self.act_Wrap.setText(_translate("MainWindow", "自动换行"))
        self.act_Font.setText(_translate("MainWindow", "字体..."))
        self.act_ZoomIn.setText(_translate("MainWindow", "放大"))
        self.act_ZoomIn.setShortcut(_translate("MainWindow", "Ctrl+Shift+="))
        self.act_ZoomOut.setText(_translate("MainWindow", "缩小"))
        self.act_ZoomOut.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.act_DefaultZoom.setText(_translate("MainWindow", "恢复默认缩放"))
        self.act_DefaultZoom.setShortcut(_translate("MainWindow", "Ctrl+0"))
        self.act_StatusBar.setText(_translate("MainWindow", "状态栏"))
        self.act_ViewHelp.setText(_translate("MainWindow", "查看帮助"))
        self.act_Feedback.setText(_translate("MainWindow", "发送反馈"))
        self.act_About.setText(_translate("MainWindow", "关于记事本"))
        self.act_Redo.setText(_translate("MainWindow", "重做"))
        self.act_Redo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.act_Mdi.setText(_translate("MainWindow", "MDI模式"))
        self.act_Mdi.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.act_LevelExpansion.setText(_translate("MainWindow", "层级展开"))
        self.act_FlatOut.setText(_translate("MainWindow", "平铺展开"))
        self.act_CloseAll.setText(_translate("MainWindow", "关闭全部"))
