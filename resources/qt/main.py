# This Python file uses the following encoding: utf-8

import sys

# Pyqt5
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

# User Interface
from landing import Ui_searchUI as Ui
# Search Engine backend
from resources.backend.search_engine import search

# User interface
from settings import Ui_Form as settings_Ui
from update_confrim import Ui_Form as confrim_Ui


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])


# Landing page
class searchWindow(QMainWindow, Ui):
    def __init__(self, parent=None):
        print("Landing")  # Testing purpose
        super(searchWindow, self).__init__(parent)
        self.setupUi(self)

        self.exit.clicked.connect(self.exitButton)

        self.sendQuary.clicked.connect(self.searchQuaryButtonListener)

    def searchQuaryButtonListener(self):
        keyword = self.searchQuary.toPlainText()
        print(keyword)

        # TableView
        data = search(keyword)  # Testing purpose
        self.model = TableModel(data)
        self.tableView.setModel(self.model)
        self.tableView.show()

        rbt = self.sender()
        print(rbt.text())

    def exitButton(self):
        print("Close the app")
        self.close()

    def back_Button_three(self):
        self.close()


# Update UI
class updateConfirm_Ui(QDialog, confrim_Ui):
    def __init__(self, parent=None):
        super(updateConfirm_Ui, self).__init__(parent)
        self.setupUi(self)
        print("Update UI")

        self.pushButton_2.clicked.connect(self.back_Button_three)

    def back_Button_three(self):
        self.close()

    def exitButton_two(self):
        print("App closed")
        self.close()


# Settings page
class settingWindow_UI(QDialog, settings_Ui):
    def __init__(self, parent=None):
        super(settingWindow_UI, self).__init__(parent)
        self.setupUi(self)
        print("Settings UI")

        self.backButton.clicked.connect(self.back_Button)

        self.backButton_2.clicked.connect(self.updateButton)

    def updateButton(self):
        self.updateC = updateConfirm_Ui(self)
        self.updateC.exec_()

    def back_Button(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = searchWindow()
    form.show()
    app.exec_()
