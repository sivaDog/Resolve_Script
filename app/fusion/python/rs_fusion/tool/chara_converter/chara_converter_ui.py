# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yoshi\PycharmProjects\Resolve_Script\app\fusion\python\rs_fusion\tool\chara_converter\chara_converter.ui',
# licensing of 'C:\Users\yoshi\PycharmProjects\Resolve_Script\app\fusion\python\rs_fusion\tool\chara_converter\chara_converter.ui' applies.
#
# Created: Thu Sep 22 20:30:01 2022
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.srcLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.srcLineEdit.setObjectName("srcLineEdit")
        self.horizontalLayout_2.addWidget(self.srcLineEdit)
        self.srcToolButton = QtWidgets.QToolButton(self.groupBox)
        self.srcToolButton.setObjectName("srcToolButton")
        self.horizontalLayout_2.addWidget(self.srcToolButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dstLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.dstLineEdit.setObjectName("dstLineEdit")
        self.horizontalLayout.addWidget(self.dstLineEdit)
        self.dstToolButton = QtWidgets.QToolButton(self.groupBox)
        self.dstToolButton.setObjectName("dstToolButton")
        self.horizontalLayout.addWidget(self.dstToolButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.useSwichCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.useSwichCheckBox.setObjectName("useSwichCheckBox")
        self.verticalLayout_2.addWidget(self.useSwichCheckBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.openSiteButton = QtWidgets.QPushButton(self.groupBox_5)
        self.openSiteButton.setMinimumSize(QtCore.QSize(100, 40))
        self.openSiteButton.setObjectName("openSiteButton")
        self.horizontalLayout_5.addWidget(self.openSiteButton)
        self.openFuseDirButton = QtWidgets.QPushButton(self.groupBox_5)
        self.openFuseDirButton.setMinimumSize(QtCore.QSize(100, 40))
        self.openFuseDirButton.setObjectName("openFuseDirButton")
        self.horizontalLayout_5.addWidget(self.openFuseDirButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logTextEdit = LogTextEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logTextEdit.sizePolicy().hasHeightForWidth())
        self.logTextEdit.setSizePolicy(sizePolicy)
        self.logTextEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setObjectName("logTextEdit")
        self.verticalLayout.addWidget(self.logTextEdit)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.importButton = QtWidgets.QPushButton(self.centralwidget)
        self.importButton.setMinimumSize(QtCore.QSize(100, 40))
        self.importButton.setObjectName("importButton")
        self.horizontalLayout_3.addWidget(self.importButton)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setMinimumSize(QtCore.QSize(100, 40))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "ディレクトリ設定", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "キャラ素材", None, -1))
        self.srcToolButton.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "出力先", None, -1))
        self.dstToolButton.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("MainWindow", "SwitchFuse", None, -1))
        self.useSwichCheckBox.setText(QtWidgets.QApplication.translate("MainWindow", "SwitchFuseを使う", None, -1))
        self.openSiteButton.setText(QtWidgets.QApplication.translate("MainWindow", " ダウンロードページを開く ", None, -1))
        self.openFuseDirButton.setText(QtWidgets.QApplication.translate("MainWindow", " インストールフォルダを開く ", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "ログ", None, -1))
        self.importButton.setText(QtWidgets.QApplication.translate("MainWindow", "import", None, -1))
        self.closeButton.setText(QtWidgets.QApplication.translate("MainWindow", "close", None, -1))

from rs.gui.log import LogTextEdit
