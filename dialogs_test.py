#!/usr/bin/env python


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAction, QApplication, QMainWindow, QMessageBox, QTextEdit, QDialog)


class TestDialog(QDialog):

    def __init__(self, parent, *, set_window_flags=False, no_parent=False):
        print(f'set_window_flags={set_window_flags}, no_parent={no_parent}')
        if no_parent:
            #super(TestDialog, self).__init__(parent=None)
            QDialog.__init__(self)
        else:
            super(TestDialog, self).__init__(parent=parent)
        self.setWindowTitle(f'Test Dialog: {set_window_flags}, {no_parent}')
        self.setMinimumWidth(640)
        self.setMinimumHeight(480)
        if set_window_flags:
            flags = self.windowFlags()
            flags = flags & ~Qt.Dialog
            flags = flags | Qt.Window
            flags = flags | Qt.WindowMinimizeButtonHint
            flags = flags | Qt.WindowMaximizeButtonHint
            self.setWindowFlags(flags)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.createMenus()
        self.statusBar().showMessage("Ready")

    def about(self):
        QMessageBox.about(
            self, "About Application",
            "The <b>Application</b> example demonstrates how to write "
            "modern GUI applications using Qt, with a menu bar, "
            "toolbars, and a status bar.")

    def dialog_test(self):
        d = TestDialog(self)
        d.show()

    def dialog_test_as_window(self):
        d = TestDialog(self, set_window_flags=True)
        d.show()

    def dialog_test_no_parent(self):
        self.d = d = TestDialog(self, no_parent=True)
        d.show()

    def createMenus(self):
        self.exitAct = QAction(
            "E&xit", self, shortcut="Ctrl+Q",
            statusTip="Exit the application",
            triggered=self.close)

        self.dialogAct = QAction(
            "Dialog test", self,
            statusTip="Show test QDialog",
            triggered=self.dialog_test)

        self.dialogActW = QAction(
            "Dialog test as Window", self,
            statusTip="Show test QDialog",
            triggered=self.dialog_test_as_window)

        self.dialogActNP = QAction(
            "Dialog test no parent", self,
            statusTip="Show test QDialog",
            triggered=self.dialog_test_no_parent)

        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.exitAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.dialogAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.dialogActW)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.dialogActNP)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
