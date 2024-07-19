#include "widget.h"
#include "ui_widget.h"
#include <QPainter>
#include <QStyleOption>
// Widget(this)是QWidget类，ui是ui_widget类
Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);  // 初始化
    //ui->label->setText("可以通过这样改变ui值");
}


Widget::~Widget()
{
    delete ui;
}

// 解决显示不了照片的问题
void Widget::paintEvent(QPaintEvent *e)
{
    QStyleOption opt;
    opt.initFrom(this);
    QPainter p(this);
    style()->drawPrimitive(QStyle::PE_Widget, &opt, &p, this);
}
