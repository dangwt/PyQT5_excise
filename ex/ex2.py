#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time     : ${DATE} ${TIME}
 @Author   : dangwt
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QToolTip, QPushButton)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('Button', self)
#        try:
        btn.clicked.connect( QCoreApplication.instance().quit )

        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        
        
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Dota2')
        self.setWindowIcon(QIcon('1.png'))
        
        self.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    ex = Example()
    sys.exit(app.exec_())
#     ex = Example()
#     ex.show
