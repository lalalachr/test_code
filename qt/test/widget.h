#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QPainter>

QT_BEGIN_NAMESPACE
namespace Ui {      // 命名空间
class Widget;       // ui_widget.h里面的类 外部声明
}
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT        // 宏，使用QT信号槽机制需要添加

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

    void paintEvent(QPaintEvent *e);

private:
    Ui::Widget *ui; // 指向可视化界面 这里的Ui::Widget就是ui_widget类
};
#endif // WIDGET_H
