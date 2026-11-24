import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar
from PySide6.QtGui import QIcon, QAction, QKeySequence

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Markdown Forge")
        self.setCentralWidget(QLabel("IN BUILDING... COMING SOON"))
        self.setFixedSize(QSize(1000, 600))




        toolBar = QToolBar("ToolBar")
        self.addToolBar(toolBar)

        button_create = QAction("Nouveau", self)
        button_create.setStatusTip("En construction")
        button_create.triggered.connect(self.toolbar_button_clicked)
        toolBar.addAction(button_create)

        button_open = QAction("Open", self)
        button_open.setStatusTip("En construcion")
        button_open.triggered.connect(self.toolbar_button_clicked)
        toolBar.addAction(button_open)

        button_save = QAction("Save", self)
        button_save.setStatusTip("En construcion")
        button_save.triggered.connect(self.toolbar_button_clicked)
        toolBar.addAction(button_save)

        menu = self.menuBar()

        fileMenu = menu.addMenu("&File")
        fileMenu.addAction(QAction(button_create))

        editMenu = menu.addMenu("&Edit")
        editMenu.addAction(QAction(button_create))

        styleMenu = menu.addMenu("&Affichage")
        styleMenu.addAction(QAction(button_create))

        helpMenu = menu.addMenu("&Help")
        helpMenu.addAction(QAction(button_create))



    def toolbar_button_clicked(self, s):
        print("click", s)






app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())




