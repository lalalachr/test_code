#include "widget.h"

#include <QApplication>


int main(int argc, char *argv[])
{
    QApplication a(argc, argv); // 定义并创建程序
    Widget w;                   // 定义窗口
    w.show();                   // 显示窗口
    return a.exec();            // 运行程序，开始循环
}
