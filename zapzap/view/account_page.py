from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/ui/account_page.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Account(object):
    def setupUi(self, Account):
        Account.setObjectName("Account")
        Account.resize(318, 450)
        Account.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Account)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Account)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_new = QtWidgets.QVBoxLayout()
        self.verticalLayout_new.setSpacing(6)
        self.verticalLayout_new.setObjectName("verticalLayout_new")
        self.btnNewUser = QtWidgets.QPushButton(parent=Account)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNewUser.sizePolicy().hasHeightForWidth())
        self.btnNewUser.setSizePolicy(sizePolicy)
        self.btnNewUser.setObjectName("btnNewUser")
        self.verticalLayout_new.addWidget(self.btnNewUser)
        self.label_2 = QtWidgets.QLabel(parent=Account)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_new.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.verticalLayout_new)
        self.line = QtWidgets.QFrame(parent=Account)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.scrollArea = QtWidgets.QScrollArea(parent=Account)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.account_scrollArea = QtWidgets.QWidget()
        self.account_scrollArea.setGeometry(QtCore.QRect(0, 0, 300, 309))
        self.account_scrollArea.setMinimumSize(QtCore.QSize(250, 0))
        self.account_scrollArea.setObjectName("account_scrollArea")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.account_scrollArea)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.usersList = QtWidgets.QVBoxLayout()
        self.usersList.setSpacing(3)
        self.usersList.setObjectName("usersList")
        self.verticalLayout_2.addLayout(self.usersList)
        spacerItem = QtWidgets.QSpacerItem(20, 329, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea.setWidget(self.account_scrollArea)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Account)
        QtCore.QMetaObject.connectSlotsByName(Account)

    def retranslateUi(self, Account):
        
        self.label.setText(_("Account"))
        self.btnNewUser.setText(_("New account"))
        self.label_2.setText(_("Creates a new panel for access to WhatsApp."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Account = QtWidgets.QWidget()
    ui = Ui_Account()
    ui.setupUi(Account)
    Account.show()
    sys.exit(app.exec())