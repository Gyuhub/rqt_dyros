#include "huskypanda.h"
#include "ui_huskypanda.h"

HuskyPanda::HuskyPanda(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::HuskyPanda)
{
    ui->setupUi(this);
}

HuskyPanda::~HuskyPanda()
{
    delete ui;
}

void HuskyPanda::on_pushButton_clicked()
{

}

void HuskyPanda::on_pushButton_2_clicked()
{

}

void HuskyPanda::on_doubleSpinBox_2_valueChanged(double arg1)
{

}

void HuskyPanda::on_doubleSpinBox_3_valueChanged(double arg1)
{

}

void HuskyPanda::on_doubleSpinBox_valueChanged(double arg1)
{

}
