#include "xcon.h"
#include "ui_xcon.h"

XCon::XCon(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::XCon)
{
    ui->setupUi(this);
}

XCon::~XCon()
{
    delete ui;
}
