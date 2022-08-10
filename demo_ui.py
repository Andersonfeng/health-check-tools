# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 251, 74))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.username_label = QtWidgets.QLabel(self.layoutWidget)
        self.username_label.setObjectName("username_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.username_label)
        self.username = QtWidgets.QLineEdit(self.layoutWidget)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username)
        self.password_label = QtWidgets.QLabel(self.layoutWidget)
        self.password_label.setObjectName("password_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.password_label)
        self.password = QtWidgets.QLineEdit(self.layoutWidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.dmz_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.dmz_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.dmz_password.setObjectName("dmz_password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dmz_password)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 110, 601, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.HC_tab = QtWidgets.QWidget()
        self.HC_tab.setObjectName("HC_tab")
        self.tableWidget = QtWidgets.QTableWidget(self.HC_tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 50, 591, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.splitter = QtWidgets.QSplitter(self.HC_tab)
        self.splitter.setGeometry(QtCore.QRect(0, 20, 150, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.update_all_button = QtWidgets.QPushButton(self.splitter)
        self.update_all_button.setObjectName("update_all_button")
        self.update_selected_button = QtWidgets.QPushButton(self.splitter)
        self.update_selected_button.setObjectName("update_selected_button")
        self.tabWidget.addTab(self.HC_tab, "")
        self.Log_tab = QtWidgets.QWidget()
        self.Log_tab.setObjectName("Log_tab")
        self.pushButton = QtWidgets.QPushButton(self.Log_tab)
        self.pushButton.setGeometry(QtCore.QRect(490, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.log_table = QtWidgets.QTableWidget(self.Log_tab)
        self.log_table.setGeometry(QtCore.QRect(0, 20, 291, 331))
        self.log_table.setObjectName("log_table")
        self.log_table.setColumnCount(0)
        self.log_table.setRowCount(0)
        self.start_date_label = QtWidgets.QLabel(self.Log_tab)
        self.start_date_label.setGeometry(QtCore.QRect(300, 30, 61, 16))
        self.start_date_label.setObjectName("start_date_label")
        self.end_date_label = QtWidgets.QLabel(self.Log_tab)
        self.end_date_label.setGeometry(QtCore.QRect(300, 60, 54, 12))
        self.end_date_label.setObjectName("end_date_label")
        self.start_date_Edit = QtWidgets.QDateEdit(self.Log_tab)
        self.start_date_Edit.setGeometry(QtCore.QRect(370, 30, 110, 22))
        self.start_date_Edit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1753, 9, 14), QtCore.QTime(0, 0, 0)))
        self.start_date_Edit.setDate(QtCore.QDate(2022, 8, 10))
        self.start_date_Edit.setObjectName("start_date_Edit")
        self.end_date_Edit = QtWidgets.QDateEdit(self.Log_tab)
        self.end_date_Edit.setGeometry(QtCore.QRect(370, 60, 110, 22))
        self.end_date_Edit.setObjectName("end_date_Edit")
        self.tabWidget.addTab(self.Log_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listView = QtWidgets.QListView(self.tab)
        self.listView.setGeometry(QtCore.QRect(20, 40, 261, 321))
        self.listView.setObjectName("listView")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(380, 30, 54, 12))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(340, 50, 131, 101))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_label.setText(_translate("MainWindow", "username"))
        self.username.setText(_translate("MainWindow", "feng"))
        self.password_label.setText(_translate("MainWindow", "password"))
        self.password.setText(_translate("MainWindow", "anderson"))
        self.label.setText(_translate("MainWindow", "dmz_password"))
        self.update_all_button.setText(_translate("MainWindow", "更新全部"))
        self.update_selected_button.setText(_translate("MainWindow", "更新选中行"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HC_tab), _translate("MainWindow", "Health Check"))
        self.pushButton.setText(_translate("MainWindow", "Get Log"))
        self.start_date_label.setText(_translate("MainWindow", "Start date"))
        self.end_date_label.setText(_translate("MainWindow", "End date"))
        self.start_date_Edit.setDisplayFormat(_translate("MainWindow", "yyyyMMdd"))
        self.end_date_Edit.setDisplayFormat(_translate("MainWindow", "yyyyMMdd"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Log_tab), _translate("MainWindow", "Get Log"))
        self.label_4.setText(_translate("MainWindow", "Command"))
        self.pushButton_2.setText(_translate("MainWindow", "run"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Run Command"))
        self.menu.setTitle(_translate("MainWindow", "关于"))
