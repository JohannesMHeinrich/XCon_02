#ifndef XCON_H
#define XCON_H

#include <QMainWindow>

namespace Ui {
class XCon;
}

class XCon : public QMainWindow
{
    Q_OBJECT

public:
    explicit XCon(QWidget *parent = 0);
    ~XCon();

private:
    Ui::XCon *ui;
};

#endif // XCON_H
