#include "xcon.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    XCon w;
    w.show();

    return a.exec();
}
