# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/msatcommander.ui'
#
# Created: Sat Jan 16 16:38:42 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_msatcommander(object):
    def setupUi(self, msatcommander):
        msatcommander.setObjectName("msatcommander")
        msatcommander.resize(522, 546)
        self.tabWidget = QtGui.QTabWidget(msatcommander)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 501, 491))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 221, 241))
        self.groupBox.setObjectName("groupBox")
        self.dinucCheckBox = QtGui.QCheckBox(self.groupBox)
        self.dinucCheckBox.setGeometry(QtCore.QRect(10, 46, 115, 31))
        self.dinucCheckBox.setObjectName("dinucCheckBox")
        self.pentanucCheckBox = QtGui.QCheckBox(self.groupBox)
        self.pentanucCheckBox.setGeometry(QtCore.QRect(10, 121, 120, 31))
        self.pentanucCheckBox.setObjectName("pentanucCheckBox")
        self.trinucCheckBox = QtGui.QCheckBox(self.groupBox)
        self.trinucCheckBox.setGeometry(QtCore.QRect(10, 71, 120, 31))
        self.trinucCheckBox.setObjectName("trinucCheckBox")
        self.hexanucCheckBox = QtGui.QCheckBox(self.groupBox)
        self.hexanucCheckBox.setGeometry(QtCore.QRect(10, 146, 120, 31))
        self.hexanucCheckBox.setObjectName("hexanucCheckBox")
        self.tetranucCheckBox = QtGui.QCheckBox(self.groupBox)
        self.tetranucCheckBox.setGeometry(QtCore.QRect(10, 96, 120, 31))
        self.tetranucCheckBox.setObjectName("tetranucCheckBox")
        self.combineLociCheckBox = QtGui.QCheckBox(self.groupBox)
        self.combineLociCheckBox.setGeometry(QtCore.QRect(10, 210, 131, 31))
        self.combineLociCheckBox.setObjectName("combineLociCheckBox")
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(10, 180, 201, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.perfectRepeatsCheckBox = QtGui.QCheckBox(self.groupBox)
        self.perfectRepeatsCheckBox.setGeometry(QtCore.QRect(10, 190, 131, 31))
        self.perfectRepeatsCheckBox.setObjectName("perfectRepeatsCheckBox")
        self.mononucCheckBox = QtGui.QCheckBox(self.groupBox)
        self.mononucCheckBox.setGeometry(QtCore.QRect(10, 21, 121, 31))
        self.mononucCheckBox.setObjectName("mononucCheckBox")
        self.mononucSpinBox = QtGui.QSpinBox(self.groupBox)
        self.mononucSpinBox.setGeometry(QtCore.QRect(150, 25, 51, 25))
        self.mononucSpinBox.setMaximum(100)
        self.mononucSpinBox.setProperty("value", 10)
        self.mononucSpinBox.setObjectName("mononucSpinBox")
        self.dinucSpinBox = QtGui.QSpinBox(self.groupBox)
        self.dinucSpinBox.setGeometry(QtCore.QRect(150, 50, 51, 25))
        self.dinucSpinBox.setMaximum(100)
        self.dinucSpinBox.setProperty("value", 8)
        self.dinucSpinBox.setObjectName("dinucSpinBox")
        self.trinucSpinBox = QtGui.QSpinBox(self.groupBox)
        self.trinucSpinBox.setGeometry(QtCore.QRect(150, 75, 51, 25))
        self.trinucSpinBox.setMaximum(100)
        self.trinucSpinBox.setProperty("value", 8)
        self.trinucSpinBox.setObjectName("trinucSpinBox")
        self.tetranucSpinBox = QtGui.QSpinBox(self.groupBox)
        self.tetranucSpinBox.setGeometry(QtCore.QRect(150, 100, 51, 25))
        self.tetranucSpinBox.setMaximum(100)
        self.tetranucSpinBox.setProperty("value", 6)
        self.tetranucSpinBox.setObjectName("tetranucSpinBox")
        self.pentanucSpinBox = QtGui.QSpinBox(self.groupBox)
        self.pentanucSpinBox.setGeometry(QtCore.QRect(150, 125, 51, 25))
        self.pentanucSpinBox.setMaximum(100)
        self.pentanucSpinBox.setProperty("value", 6)
        self.pentanucSpinBox.setObjectName("pentanucSpinBox")
        self.hexanucSpinBox = QtGui.QSpinBox(self.groupBox)
        self.hexanucSpinBox.setGeometry(QtCore.QRect(150, 150, 51, 25))
        self.hexanucSpinBox.setMaximum(100)
        self.hexanucSpinBox.setProperty("value", 6)
        self.hexanucSpinBox.setObjectName("hexanucSpinBox")
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 250, 221, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.designPrimersCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.designPrimersCheckBox.setGeometry(QtCore.QRect(10, 30, 151, 21))
        self.designPrimersCheckBox.setObjectName("designPrimersCheckBox")
        self.tagPrimersCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.tagPrimersCheckBox.setGeometry(QtCore.QRect(10, 60, 151, 21))
        self.tagPrimersCheckBox.setObjectName("tagPrimersCheckBox")
        self.pigtailsPrimersCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.pigtailsPrimersCheckBox.setGeometry(QtCore.QRect(10, 170, 171, 21))
        self.pigtailsPrimersCheckBox.setObjectName("pigtailsPrimersCheckBox")
        self.cagTagCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.cagTagCheckBox.setGeometry(QtCore.QRect(30, 80, 151, 21))
        self.cagTagCheckBox.setChecked(True)
        self.cagTagCheckBox.setObjectName("cagTagCheckBox")
        self.m13rCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.m13rCheckBox.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m13rCheckBox.setChecked(True)
        self.m13rCheckBox.setObjectName("m13rCheckBox")
        self.customTagCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.customTagCheckBox.setGeometry(QtCore.QRect(30, 120, 151, 21))
        self.customTagCheckBox.setObjectName("customTagCheckBox")
        self.customTagLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.customTagLineEdit.setGeometry(QtCore.QRect(50, 140, 160, 22))
        self.customTagLineEdit.setAutoFillBackground(False)
        self.customTagLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.customTagLineEdit.setObjectName("customTagLineEdit")
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(265, 0, 221, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.useMultiprocessingCheckBox = QtGui.QCheckBox(self.groupBox_3)
        self.useMultiprocessingCheckBox.setGeometry(QtCore.QRect(20, 30, 161, 31))
        self.useMultiprocessingCheckBox.setObjectName("useMultiprocessingCheckBox")
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(265, 90, 221, 191))
        self.groupBox_4.setObjectName("groupBox_4")
        self.checkBox_16 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_16.setGeometry(QtCore.QRect(40, 70, 161, 31))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_17.setGeometry(QtCore.QRect(40, 90, 161, 31))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_18.setGeometry(QtCore.QRect(40, 110, 161, 31))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_19.setGeometry(QtCore.QRect(40, 130, 161, 31))
        self.checkBox_19.setObjectName("checkBox_19")
        self.commaSeparatedRadioButton = QtGui.QRadioButton(self.groupBox_4)
        self.commaSeparatedRadioButton.setGeometry(QtCore.QRect(20, 30, 151, 21))
        self.commaSeparatedRadioButton.setChecked(True)
        self.commaSeparatedRadioButton.setObjectName("commaSeparatedRadioButton")
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 50, 151, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 160, 151, 21))
        self.radioButton_3.setObjectName("radioButton_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_5 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 80, 191, 103))
        self.groupBox_5.setObjectName("groupBox_5")
        self.spinBox_4 = QtGui.QSpinBox(self.groupBox_5)
        self.spinBox_4.setGeometry(QtCore.QRect(120, 22, 58, 25))
        self.spinBox_4.setMinimum(15)
        self.spinBox_4.setMaximum(30)
        self.spinBox_4.setProperty("value", 18)
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_4 = QtGui.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(10, 24, 111, 20))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtGui.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 111, 20))
        self.label_7.setObjectName("label_7")
        self.spinBox_6 = QtGui.QSpinBox(self.groupBox_5)
        self.spinBox_6.setGeometry(QtCore.QRect(120, 48, 58, 25))
        self.spinBox_6.setMinimum(15)
        self.spinBox_6.setMaximum(30)
        self.spinBox_6.setProperty("value", 18)
        self.spinBox_6.setObjectName("spinBox_6")
        self.label_8 = QtGui.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(10, 76, 111, 20))
        self.label_8.setObjectName("label_8")
        self.spinBox_7 = QtGui.QSpinBox(self.groupBox_5)
        self.spinBox_7.setGeometry(QtCore.QRect(120, 74, 58, 25))
        self.spinBox_7.setMinimum(15)
        self.spinBox_7.setMaximum(30)
        self.spinBox_7.setProperty("value", 18)
        self.spinBox_7.setObjectName("spinBox_7")
        self.groupBox_6 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 0, 481, 81))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_5 = QtGui.QLabel(self.groupBox_6)
        self.label_5.setGeometry(QtCore.QRect(10, 38, 111, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 40, 371, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.groupBox_7 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 180, 191, 103))
        self.groupBox_7.setObjectName("groupBox_7")
        self.spinBox_5 = QtGui.QSpinBox(self.groupBox_7)
        self.spinBox_5.setGeometry(QtCore.QRect(120, 22, 58, 25))
        self.spinBox_5.setMinimum(15)
        self.spinBox_5.setMaximum(30)
        self.spinBox_5.setProperty("value", 18)
        self.spinBox_5.setObjectName("spinBox_5")
        self.label_6 = QtGui.QLabel(self.groupBox_7)
        self.label_6.setGeometry(QtCore.QRect(10, 24, 111, 20))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtGui.QLabel(self.groupBox_7)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 111, 20))
        self.label_9.setObjectName("label_9")
        self.spinBox_8 = QtGui.QSpinBox(self.groupBox_7)
        self.spinBox_8.setGeometry(QtCore.QRect(120, 48, 58, 25))
        self.spinBox_8.setMinimum(15)
        self.spinBox_8.setMaximum(30)
        self.spinBox_8.setProperty("value", 18)
        self.spinBox_8.setObjectName("spinBox_8")
        self.label_10 = QtGui.QLabel(self.groupBox_7)
        self.label_10.setGeometry(QtCore.QRect(10, 76, 111, 20))
        self.label_10.setObjectName("label_10")
        self.spinBox_9 = QtGui.QSpinBox(self.groupBox_7)
        self.spinBox_9.setGeometry(QtCore.QRect(120, 74, 58, 25))
        self.spinBox_9.setMinimum(15)
        self.spinBox_9.setMaximum(30)
        self.spinBox_9.setProperty("value", 18)
        self.spinBox_9.setObjectName("spinBox_9")
        self.tabWidget.addTab(self.tab_3, "")
        self.runButton = QtGui.QPushButton(msatcommander)
        self.runButton.setGeometry(QtCore.QRect(290, 510, 115, 32))
        self.runButton.setObjectName("runButton")
        self.cancelButton = QtGui.QPushButton(msatcommander)
        self.cancelButton.setGeometry(QtCore.QRect(400, 510, 115, 32))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(msatcommander)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), msatcommander.close)
        QtCore.QObject.connect(self.runButton, QtCore.SIGNAL("clicked()"), msatcommander.accept)
        QtCore.QMetaObject.connectSlotsByName(msatcommander)
        msatcommander.setTabOrder(self.tagPrimersCheckBox, self.mononucSpinBox)
        msatcommander.setTabOrder(self.mononucSpinBox, self.dinucCheckBox)
        msatcommander.setTabOrder(self.dinucCheckBox, self.combineLociCheckBox)
        msatcommander.setTabOrder(self.combineLociCheckBox, self.trinucCheckBox)
        msatcommander.setTabOrder(self.trinucCheckBox, self.hexanucCheckBox)
        msatcommander.setTabOrder(self.hexanucCheckBox, self.tetranucCheckBox)
        msatcommander.setTabOrder(self.tetranucCheckBox, self.designPrimersCheckBox)
        msatcommander.setTabOrder(self.designPrimersCheckBox, self.dinucSpinBox)
        msatcommander.setTabOrder(self.dinucSpinBox, self.trinucSpinBox)
        msatcommander.setTabOrder(self.trinucSpinBox, self.pigtailsPrimersCheckBox)
        msatcommander.setTabOrder(self.pigtailsPrimersCheckBox, self.cagTagCheckBox)
        msatcommander.setTabOrder(self.cagTagCheckBox, self.m13rCheckBox)
        msatcommander.setTabOrder(self.m13rCheckBox, self.mononucCheckBox)
        msatcommander.setTabOrder(self.mononucCheckBox, self.customTagCheckBox)
        msatcommander.setTabOrder(self.customTagCheckBox, self.customTagLineEdit)
        msatcommander.setTabOrder(self.customTagLineEdit, self.useMultiprocessingCheckBox)
        msatcommander.setTabOrder(self.useMultiprocessingCheckBox, self.checkBox_16)
        msatcommander.setTabOrder(self.checkBox_16, self.checkBox_17)
        msatcommander.setTabOrder(self.checkBox_17, self.checkBox_18)
        msatcommander.setTabOrder(self.checkBox_18, self.checkBox_19)
        msatcommander.setTabOrder(self.checkBox_19, self.commaSeparatedRadioButton)
        msatcommander.setTabOrder(self.commaSeparatedRadioButton, self.radioButton_2)
        msatcommander.setTabOrder(self.radioButton_2, self.radioButton_3)
        msatcommander.setTabOrder(self.radioButton_3, self.spinBox_4)
        msatcommander.setTabOrder(self.spinBox_4, self.spinBox_6)
        msatcommander.setTabOrder(self.spinBox_6, self.spinBox_7)
        msatcommander.setTabOrder(self.spinBox_7, self.lineEdit_2)
        msatcommander.setTabOrder(self.lineEdit_2, self.spinBox_5)
        msatcommander.setTabOrder(self.spinBox_5, self.spinBox_8)
        msatcommander.setTabOrder(self.spinBox_8, self.spinBox_9)
        msatcommander.setTabOrder(self.spinBox_9, self.perfectRepeatsCheckBox)
        msatcommander.setTabOrder(self.perfectRepeatsCheckBox, self.tabWidget)
        msatcommander.setTabOrder(self.tabWidget, self.runButton)
        msatcommander.setTabOrder(self.runButton, self.cancelButton)
        msatcommander.setTabOrder(self.cancelButton, self.pentanucCheckBox)
        msatcommander.setTabOrder(self.pentanucCheckBox, self.tetranucSpinBox)
        msatcommander.setTabOrder(self.tetranucSpinBox, self.pentanucSpinBox)
        msatcommander.setTabOrder(self.pentanucSpinBox, self.hexanucSpinBox)

    def retranslateUi(self, msatcommander):
        msatcommander.setWindowTitle(QtGui.QApplication.translate("msatcommander", "msatcommander-1.0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("msatcommander", "Search Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.dinucCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Dinucleotide", None, QtGui.QApplication.UnicodeUTF8))
        self.pentanucCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Pentanucleotide", None, QtGui.QApplication.UnicodeUTF8))
        self.trinucCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Trinucleotide", None, QtGui.QApplication.UnicodeUTF8))
        self.hexanucCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Hexanucleotide", None, QtGui.QApplication.UnicodeUTF8))
        self.tetranucCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Tetranucleotide", None, QtGui.QApplication.UnicodeUTF8))
        self.combineLociCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Combine Loci", None, QtGui.QApplication.UnicodeUTF8))
        self.perfectRepeatsCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Perfect Repeats", None, QtGui.QApplication.UnicodeUTF8))
        self.mononucCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Mononucleotide", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("msatcommander", "Primer Design", None, QtGui.QApplication.UnicodeUTF8))
        self.designPrimersCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Design Primers", None, QtGui.QApplication.UnicodeUTF8))
        self.tagPrimersCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Tag Primers", None, QtGui.QApplication.UnicodeUTF8))
        self.pigtailsPrimersCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Pigtail (GTTT) Primers", None, QtGui.QApplication.UnicodeUTF8))
        self.cagTagCheckBox.setText(QtGui.QApplication.translate("msatcommander", "CAG Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.m13rCheckBox.setText(QtGui.QApplication.translate("msatcommander", "M13R Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.customTagCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Custom Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("msatcommander", "Multiprocessing", None, QtGui.QApplication.UnicodeUTF8))
        self.useMultiprocessingCheckBox.setText(QtGui.QApplication.translate("msatcommander", "Use Multiprocessing", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("msatcommander", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_16.setText(QtGui.QApplication.translate("msatcommander", "Repeats", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_17.setText(QtGui.QApplication.translate("msatcommander", "Combined Repeats", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_18.setText(QtGui.QApplication.translate("msatcommander", "Primers", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_19.setText(QtGui.QApplication.translate("msatcommander", "Tagged Primers", None, QtGui.QApplication.UnicodeUTF8))
        self.commaSeparatedRadioButton.setText(QtGui.QApplication.translate("msatcommander", "Comma-Separated", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("msatcommander", "Tab-Delimited", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("msatcommander", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("msatcommander", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("msatcommander", "Primer Sizes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("msatcommander", "Primer Min Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("msatcommander", "Primer Opt Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("msatcommander", "Primer Max Size", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("msatcommander", "Product Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("msatcommander", "Product Size", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("msatcommander", "Primer Tms", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("msatcommander", "Primer Min Tm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("msatcommander", "Primer Opt Tm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("msatcommander", "Primer Max Tm", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("msatcommander", "Advanced", None, QtGui.QApplication.UnicodeUTF8))
        self.runButton.setText(QtGui.QApplication.translate("msatcommander", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("msatcommander", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
