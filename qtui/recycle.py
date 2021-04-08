# @pyqtSlot()  # Cut 操作
# def on_actEdit_Cut_triggered(self):
#     # self.formDoc = self.ui.mdi.activeSubWindow().widget()
#     self.formDoc.textCut()
#
# @pyqtSlot()  # Copy 操作
# def on_actEdit_Copy_triggered(self):
#     # self.formDoc = self.ui.mdi.activeSubWindow().widget()
#     self.formDoc.textCopy()
#
# @pyqtSlot()  # Paste 操作
# def on_actEdit_Paste_triggered(self):
#     # self.formDoc = self.ui.mdi.activeSubWindow().widget()
#     self.formDoc.textPaste()
#
# @pyqtSlot()  # “字体设置”
# def on_actEdit_Font_triggered(self):
#     # self.formDoc = self.ui.mdi.activeSubWindow().widget()
#     self.formDoc.textSetFont()
#
#    @pyqtSlot(type)   子窗口切换
# def on_mdi_subWindowActivated(self, arg1):
#     cnt = len(self.ui.mdi.subWindowList())
#     if cnt == 0:
#         self.ui.StatusB.clearMessage()
#     else:
#         self.formDoc = self.ui.mdi.activeSubWindow().widget()
#         self.ui.StatusB.showMessage(self.formDoc.currentFileName())  # 显示子窗口的文件名
#
#     # print(self.ui.mdi.subWindowList())
#     # print("----")
#     # for widget in self.ui.mdi.subWindowList(QMdiArea.ActivationHistoryOrder):
#     #     print(widget.windowTitle())
#     # # 上一个窗口的求出方式
#     # print()
#
#     # ---- 断开上一个窗口的信号连接 ----
#     mdilist = self.ui.mdi.subWindowList(QMdiArea.ActivationHistoryOrder)
#     if len(mdilist) >= 2:
#         mdicurentwidget = mdilist[-2].widget()
#         print(mdicurentwidget)
#         print(mdicurentwidget.windowTitle())
        # # if self.ui.act_Undo.isSignalConnected(self.ui.act_Undo.triggered):
        # if True:
        # for mdiwindow in mdilist:
        #     mdiwidget = mdiwindow.widget()
        #     try:
        #         self.ui.act_Undo.triggered.disconnect(mdiwidget.tE.undo)
        #         self.ui.act_Redo.triggered.disconnect(mdiwidget.tE.redo)
        #         self.ui.act_Cut.triggered.disconnect(mdiwidget.tE.cut)
        #         self.ui.act_Copy.triggered.disconnect(mdiwidget.tE.copy)
        #         self.ui.act_Paste.triggered.disconnect(mdiwidget.tE.paste)
        #         self.ui.act_SelectAll.triggered.disconnect(mdiwidget.tE.selectAll)
        #         print("上一个组件信号已解除")
        #     except Exception as e:
        #         print("信号解除失败")
        #         print(e)

    #     try:
    #         self.ui.act_Undo.triggered.disconnect(mdicurentwidget.tE.undo)
    #         self.ui.act_Redo.triggered.disconnect(mdicurentwidget.tE.redo)
    #         self.ui.act_Cut.triggered.disconnect(mdicurentwidget.tE.cut)
    #         self.ui.act_Copy.triggered.disconnect(mdicurentwidget.tE.copy)
    #         self.ui.act_Paste.triggered.disconnect(mdicurentwidget.tE.paste)
    #         self.ui.act_SelectAll.triggered.disconnect(mdicurentwidget.tE.selectAll)
    #         self.ui.act_Font.triggered.connect(self.formDoc.textSetFont)
    #         print("上一个窗口组件信号已解除")
    #     except Exception as e:
    #         print("上一个窗口组件信号解除失败")
    #         print(e)
    #
    # # ---- 当前激活窗口的信号连接 ----
    # self.ui.act_Undo.triggered.connect(self.formDoc.tE.undo)
    # self.ui.act_Redo.triggered.connect(self.formDoc.tE.redo)
    # self.ui.act_Cut.triggered.connect(self.formDoc.tE.cut)
    # self.ui.act_Copy.triggered.connect(self.formDoc.tE.copy)
    # self.ui.act_Paste.triggered.connect(self.formDoc.tE.paste)
    # self.ui.act_SelectAll.triggered.connect(self.formDoc.tE.selectAll)
    # self.ui.act_Font.triggered.connect(self.formDoc.textSetFont)
    # print("当前窗口组件信号已连接")



