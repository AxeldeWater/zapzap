from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/ui/drawer.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_drawer(object):
    def setupUi(self, drawer):
        drawer.setObjectName("drawer")
        drawer.setEnabled(True)
        drawer.resize(899, 632)
        drawer.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        drawer.setMouseTracking(False)
        drawer.setWindowTitle("")
        drawer.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(drawer)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(parent=drawer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("border : 0;\n"
"background: rgba(0, 0, 0,0.8);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=drawer)
        self.stackedWidget.setObjectName("stackedWidget")
        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=drawer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("border : 0;\n"
"background: rgba(0, 0, 0,0.8);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=drawer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("border : 0;\n"
"background: rgba(0, 0, 0,0.8);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 3, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=drawer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("border : 0;\n"
"background: rgba(0, 0, 0,0.8);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 3, 1)

        self.retranslateUi(drawer)
        QtCore.QMetaObject.connectSlotsByName(drawer)

    def retranslateUi(self, drawer):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    drawer = QtWidgets.QWidget()
    ui = Ui_drawer()
    ui.setupUi(drawer)
    drawer.show()
    sys.exit(app.exec())