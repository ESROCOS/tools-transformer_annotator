# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/estrano_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1264, 1046)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fileinput = QtWidgets.QHBoxLayout()
        self.fileinput.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.fileinput.setSpacing(6)
        self.fileinput.setObjectName("fileinput")
        self.import_filename = QtWidgets.QLineEdit(self.centralwidget)
        self.import_filename.setObjectName("import_filename")
        self.fileinput.addWidget(self.import_filename)
        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browse_button.sizePolicy().hasHeightForWidth())
        self.browse_button.setSizePolicy(sizePolicy)
        self.browse_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.browse_button.setObjectName("browse_button")
        self.fileinput.addWidget(self.browse_button)
        self.import_button = QtWidgets.QPushButton(self.centralwidget)
        self.import_button.setObjectName("import_button")
        self.fileinput.addWidget(self.import_button)
        self.verticalLayout.addLayout(self.fileinput)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.transformations = QtWidgets.QWidget(self.centralwidget)
        self.transformations.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transformations.sizePolicy().hasHeightForWidth())
        self.transformations.setSizePolicy(sizePolicy)
        self.transformations.setMinimumSize(QtCore.QSize(500, 300))
        self.transformations.setObjectName("transformations")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.transformations)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.displays = QtWidgets.QGridLayout()
        self.displays.setObjectName("displays")
        self.prov_tfs = QtWidgets.QLabel(self.transformations)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prov_tfs.sizePolicy().hasHeightForWidth())
        self.prov_tfs.setSizePolicy(sizePolicy)
        self.prov_tfs.setObjectName("prov_tfs")
        self.displays.addWidget(self.prov_tfs, 0, 0, 1, 1)
        self.requ_tfs = QtWidgets.QLabel(self.transformations)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.requ_tfs.sizePolicy().hasHeightForWidth())
        self.requ_tfs.setSizePolicy(sizePolicy)
        self.requ_tfs.setObjectName("requ_tfs")
        self.displays.addWidget(self.requ_tfs, 0, 1, 1, 1)
        self.display_r = QtWidgets.QLabel(self.transformations)
        self.display_r.setText("")
        self.display_r.setObjectName("display_r")
        self.displays.addWidget(self.display_r, 1, 1, 1, 1)
        self.display_p = QtWidgets.QLabel(self.transformations)
        self.display_p.setText("")
        self.display_p.setObjectName("display_p")
        self.displays.addWidget(self.display_p, 1, 0, 1, 1)
        self.displays.setRowStretch(1, 1)
        self.verticalLayout_3.addLayout(self.displays)
        self.tools = QtWidgets.QHBoxLayout()
        self.tools.setObjectName("tools")
        self.validate_button = QtWidgets.QPushButton(self.transformations)
        self.validate_button.setObjectName("validate_button")
        self.tools.addWidget(self.validate_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.tools.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(self.transformations)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tools.addWidget(self.line)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.tools.addItem(spacerItem2)
        self.check_requested_tfs_button = QtWidgets.QPushButton(self.transformations)
        self.check_requested_tfs_button.setObjectName("check_requested_tfs_button")
        self.tools.addWidget(self.check_requested_tfs_button)
        self.verticalLayout_3.addLayout(self.tools)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout.addWidget(self.transformations)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.textOutput = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textOutput.sizePolicy().hasHeightForWidth())
        self.textOutput.setSizePolicy(sizePolicy)
        self.textOutput.setMinimumSize(QtCore.QSize(0, 27))
        self.textOutput.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textOutput.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textOutput.setObjectName("textOutput")
        self.verticalLayout.addWidget(self.textOutput)
        self.utility = QtWidgets.QHBoxLayout()
        self.utility.setObjectName("utility")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.utility.addItem(spacerItem3)
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setObjectName("clear_button")
        self.utility.addWidget(self.clear_button)
        self.verticalLayout.addLayout(self.utility)
        self.verticalLayout.setStretch(3, 1)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1264, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Transformations"))
        self.import_filename.setText(_translate("MainWindow", "~/path/to/file.xml"))
        self.browse_button.setText(_translate("MainWindow", "..."))
        self.import_button.setText(_translate("MainWindow", "import"))
        self.prov_tfs.setText(_translate("MainWindow", "Provided Transformations"))
        self.requ_tfs.setText(_translate("MainWindow", "Requested Transformations"))
        self.validate_button.setText(_translate("MainWindow", "is Tree?"))
        self.check_requested_tfs_button.setText(_translate("MainWindow", "check Requested"))
        self.clear_button.setText(_translate("MainWindow", "clear log"))
