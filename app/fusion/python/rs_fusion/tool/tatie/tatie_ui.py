# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yoshi\PycharmProjects\Resolve_Script\app\fusion\python\rs_fusion\tool\tatie\tatie.ui',
# licensing of 'C:\Users\yoshi\PycharmProjects\Resolve_Script\app\fusion\python\rs_fusion\tool\tatie\tatie.ui' applies.
#
# Created: Wed Jan 18 07:52:23 2023
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.openDirButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openDirButton.sizePolicy().hasHeightForWidth())
        self.openDirButton.setSizePolicy(sizePolicy)
        self.openDirButton.setMinimumSize(QtCore.QSize(100, 40))
        self.openDirButton.setObjectName("openDirButton")
        self.horizontalLayout_7.addWidget(self.openDirButton)
        self.openSampleButton = QtWidgets.QPushButton(self.centralwidget)
        self.openSampleButton.setMinimumSize(QtCore.QSize(100, 40))
        self.openSampleButton.setObjectName("openSampleButton")
        self.horizontalLayout_7.addWidget(self.openSampleButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.multiplyCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.multiplyCheckBox.setObjectName("multiplyCheckBox")
        self.verticalLayout.addWidget(self.multiplyCheckBox)
        self.loaderButton = QtWidgets.QPushButton(self.groupBox)
        self.loaderButton.setMinimumSize(QtCore.QSize(100, 40))
        self.loaderButton.setObjectName("loaderButton")
        self.verticalLayout.addWidget(self.loaderButton)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.pageNameLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.pageNameLineEdit.setObjectName("pageNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pageNameLineEdit)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.ctrlNameLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.ctrlNameLineEdit.setObjectName("ctrlNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ctrlNameLineEdit)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.widthSpinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.widthSpinBox.setMinimumSize(QtCore.QSize(100, 0))
        self.widthSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.widthSpinBox.setMinimum(1)
        self.widthSpinBox.setMaximum(999999)
        self.widthSpinBox.setDisplayIntegerBase(10)
        self.widthSpinBox.setObjectName("widthSpinBox")
        self.horizontalLayout.addWidget(self.widthSpinBox)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.heightSpinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.heightSpinBox.setMinimumSize(QtCore.QSize(100, 0))
        self.heightSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.heightSpinBox.setMinimum(1)
        self.heightSpinBox.setMaximum(999999)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.horizontalLayout.addWidget(self.heightSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.chkRadioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.chkRadioButton.setObjectName("chkRadioButton")
        self.horizontalLayout_4.addWidget(self.chkRadioButton)
        self.cmbRadioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.cmbRadioButton.setChecked(True)
        self.cmbRadioButton.setObjectName("cmbRadioButton")
        self.horizontalLayout_4.addWidget(self.cmbRadioButton)
        self.sldRadioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.sldRadioButton.setObjectName("sldRadioButton")
        self.horizontalLayout_4.addWidget(self.sldRadioButton)
        spacerItem2 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.margeButton = QtWidgets.QPushButton(self.tab_2)
        self.margeButton.setMinimumSize(QtCore.QSize(100, 40))
        self.margeButton.setObjectName("margeButton")
        self.verticalLayout_7.addWidget(self.margeButton)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(20, 114, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.dissolveButton = QtWidgets.QPushButton(self.tab_3)
        self.dissolveButton.setMinimumSize(QtCore.QSize(100, 40))
        self.dissolveButton.setObjectName("dissolveButton")
        self.verticalLayout_5.addWidget(self.dissolveButton)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.openSiteButton = QtWidgets.QPushButton(self.tab_4)
        self.openSiteButton.setMinimumSize(QtCore.QSize(100, 40))
        self.openSiteButton.setObjectName("openSiteButton")
        self.horizontalLayout_8.addWidget(self.openSiteButton)
        self.openFuseDirButton = QtWidgets.QPushButton(self.tab_4)
        self.openFuseDirButton.setMinimumSize(QtCore.QSize(100, 40))
        self.openFuseDirButton.setObjectName("openFuseDirButton")
        self.horizontalLayout_8.addWidget(self.openFuseDirButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        spacerItem5 = QtWidgets.QSpacerItem(20, 66, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.switchButton = QtWidgets.QPushButton(self.tab_4)
        self.switchButton.setMinimumSize(QtCore.QSize(100, 40))
        self.switchButton.setObjectName("switchButton")
        self.verticalLayout_4.addWidget(self.switchButton)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(20, 114, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self.addButtonButton = QtWidgets.QPushButton(self.tab_5)
        self.addButtonButton.setMinimumSize(QtCore.QSize(100, 40))
        self.addButtonButton.setObjectName("addButtonButton")
        self.verticalLayout_8.addWidget(self.addButtonButton)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setMinimumSize(QtCore.QSize(100, 40))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_2.addWidget(self.closeButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.openDirButton.setText(QtWidgets.QApplication.translate("MainWindow", "Generators テンプレートフォルダを開く", None, -1))
        self.openSampleButton.setText(QtWidgets.QApplication.translate("MainWindow", " りぞりぷとサンプルフォルダを開く ", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "読み込み(Loader)", None, -1))
        self.multiplyCheckBox.setText(QtWidgets.QApplication.translate("MainWindow", "Post-Multiply by Alpha", None, -1))
        self.loaderButton.setText(QtWidgets.QApplication.translate("MainWindow", "読み込み", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "合成", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "ページ名", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "パラメータ名", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "BG", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "幅", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "高さ", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "コントローラ タイプ", None, -1))
        self.chkRadioButton.setText(QtWidgets.QApplication.translate("MainWindow", "チェックボックス", None, -1))
        self.cmbRadioButton.setText(QtWidgets.QApplication.translate("MainWindow", "コンボボックス", None, -1))
        self.sldRadioButton.setText(QtWidgets.QApplication.translate("MainWindow", "スライダー", None, -1))
        self.margeButton.setText(QtWidgets.QApplication.translate("MainWindow", "マージ", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "マージ", None, -1))
        self.dissolveButton.setText(QtWidgets.QApplication.translate("MainWindow", "ディゾルブ", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtWidgets.QApplication.translate("MainWindow", "ディゾルブ", None, -1))
        self.openSiteButton.setText(QtWidgets.QApplication.translate("MainWindow", " ダウンロードページを開く ", None, -1))
        self.openFuseDirButton.setText(QtWidgets.QApplication.translate("MainWindow", " インストールフォルダを開く ", None, -1))
        self.switchButton.setText(QtWidgets.QApplication.translate("MainWindow", "SwitchFuse", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtWidgets.QApplication.translate("MainWindow", "SwitchFuse", None, -1))
        self.addButtonButton.setText(QtWidgets.QApplication.translate("MainWindow", "ボタン切り替え", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtWidgets.QApplication.translate("MainWindow", "ボタン切り替え", None, -1))
        self.closeButton.setText(QtWidgets.QApplication.translate("MainWindow", "close", None, -1))

