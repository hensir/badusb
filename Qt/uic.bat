echo off

pyuic5 -o ..\ui_mainwindow.py  mainwindow.ui
pyuic5 -o ..\ui_keyDialog.py  dialog.ui
rem pyrcc5 .\QtApp\res.qrc -o res_rc.py

