#include "huskypanda.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    HuskyPanda w;
    w.show();

    return a.exec();
}
