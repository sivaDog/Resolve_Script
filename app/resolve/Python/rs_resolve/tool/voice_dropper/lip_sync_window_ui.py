# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\dev\PycharmProjects\Resolve_Script\app\resolve\Python\rs_resolve\tool\voice_dropper\lip_sync_window.ui',
# licensing of 'D:\dev\PycharmProjects\Resolve_Script\app\resolve\Python\rs_resolve\tool\voice_dropper\lip_sync_window.ui' applies.
#
# Created: Fri Jul 28 00:16:23 2023
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(272, 297)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.tatieTimeOutSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.tatieTimeOutSpinBox.setObjectName("tatieTimeOutSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tatieTimeOutSpinBox)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.autoLockCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.autoLockCheckBox.setObjectName("autoLockCheckBox")
        self.verticalLayout.addWidget(self.autoLockCheckBox)
        self.useDeleteCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.useDeleteCheckBox.setObjectName("useDeleteCheckBox")
        self.verticalLayout.addWidget(self.useDeleteCheckBox)
        self.shortcutButton = QtWidgets.QPushButton(self.centralwidget)
        self.shortcutButton.setObjectName("shortcutButton")
        self.verticalLayout.addWidget(self.shortcutButton)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(30, 0))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.videoListView = QtWidgets.QListView(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoListView.sizePolicy().hasHeightForWidth())
        self.videoListView.setSizePolicy(sizePolicy)
        self.videoListView.setMinimumSize(QtCore.QSize(0, 0))
        self.videoListView.setBaseSize(QtCore.QSize(0, 0))
        self.videoListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.videoListView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.videoListView.setObjectName("videoListView")
        self.verticalLayout_2.addWidget(self.videoListView)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMinimumSize(QtCore.QSize(30, 0))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.audioListView = QtWidgets.QListView(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audioListView.sizePolicy().hasHeightForWidth())
        self.audioListView.setSizePolicy(sizePolicy)
        self.audioListView.setMinimumSize(QtCore.QSize(0, 0))
        self.audioListView.setBaseSize(QtCore.QSize(1, 0))
        self.audioListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.audioListView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.audioListView.setObjectName("audioListView")
        self.verticalLayout_3.addWidget(self.audioListView)
        self.horizontalLayout_2.addWidget(self.groupBox_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.updateTrackButton = QtWidgets.QPushButton(self.groupBox_6)
        self.updateTrackButton.setObjectName("updateTrackButton")
        self.horizontalLayout_4.addWidget(self.updateTrackButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setMinimumSize(QtCore.QSize(80, 30))
        self.applyButton.setObjectName("applyButton")
        self.horizontalLayout.addWidget(self.applyButton)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setMinimumSize(QtCore.QSize(80, 30))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "time out", None, -1))
        self.autoLockCheckBox.setText(QtWidgets.QApplication.translate("MainWindow", "Auto Lock", None, -1))
        self.useDeleteCheckBox.setText(QtWidgets.QApplication.translate("MainWindow", "音声がない部分の立ち絵を削除", None, -1))
        self.shortcutButton.setText(QtWidgets.QApplication.translate("MainWindow", "shortcut", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "Video Track", None, -1))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("MainWindow", "Audio Track", None, -1))
        self.updateTrackButton.setText(QtWidgets.QApplication.translate("MainWindow", "update", None, -1))
        self.applyButton.setText(QtWidgets.QApplication.translate("MainWindow", "apply", None, -1))
        self.closeButton.setText(QtWidgets.QApplication.translate("MainWindow", "close", None, -1))

