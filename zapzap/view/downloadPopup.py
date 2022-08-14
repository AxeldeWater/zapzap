from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/downloadPopup.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DownloadPopup(object):
    def setupUi(self, DownloadPopup):
        DownloadPopup.setObjectName("DownloadPopup")
        DownloadPopup.resize(326, 93)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(DownloadPopup)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.popupContainer = QtWidgets.QFrame(DownloadPopup)
        self.popupContainer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.popupContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.popupContainer.setObjectName("popupContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.popupContainer)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.popupFrame = QtWidgets.QFrame(self.popupContainer)
        self.popupFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.popupFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.popupFrame.setObjectName("popupFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.popupFrame)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.popupFrame)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.frame_3 = QtWidgets.QFrame(self.popupFrame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.popupFrame)
        self.verticalLayout_3.addWidget(self.popupContainer)

        self.retranslateUi(DownloadPopup)
        QtCore.QMetaObject.connectSlotsByName(DownloadPopup)

    def retranslateUi(self, DownloadPopup):
        
        DownloadPopup.setWindowTitle(_("Form"))
        self.label_2.setText(_("What do you want to do with the file?"))
        self.pushButton.setText(_("Open"))
        self.pushButton_2.setText(_("Save as"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DownloadPopup = QtWidgets.QWidget()
    ui = Ui_DownloadPopup()
    ui.setupUi(DownloadPopup)
    DownloadPopup.show()
    sys.exit(app.exec())