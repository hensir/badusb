#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pb_sp_ap_clicked()
{

}

void MainWindow::on_pb_ps_ap_clicked()
{

}

void MainWindow::on_cb_ci_ap_activated(const QString &arg1)
{

}

void MainWindow::on_cb_ci_ap_activated(int index)
{

}

void MainWindow::on_cb_ci_ap_currentIndexChanged(int index)
{

}

void MainWindow::on_pb_dtd_clicked()
{

}
