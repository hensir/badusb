#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_pb_sp_ap_clicked();

    void on_pb_ps_ap_clicked();

    void on_cb_ci_ap_activated(const QString &arg1);

    void on_cb_ci_ap_activated(int index);

    void on_cb_ci_ap_currentIndexChanged(int index);

    void on_pb_dtd_clicked();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
