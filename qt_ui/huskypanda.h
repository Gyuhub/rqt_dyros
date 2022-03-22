#ifndef HUSKYPANDA_H
#define HUSKYPANDA_H

#include <QMainWindow>

namespace Ui {
class HuskyPanda;
}

class HuskyPanda : public QMainWindow
{
    Q_OBJECT

public:
    explicit HuskyPanda(QWidget *parent = 0);
    ~HuskyPanda();

private:
    Ui::HuskyPanda *ui;
};

#endif // HUSKYPANDA_H
