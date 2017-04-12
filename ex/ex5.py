#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time     : 2017/4/12 21:33
 @Author   : dangwt
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QDesktopWidget, QMessageBox)
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Dota2')
        self.setWindowIcon(QIcon('1.png'))
        self.center()
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     'Are you sure to quit?', QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    ex = Example()
    sys.exit(app.exec_())
