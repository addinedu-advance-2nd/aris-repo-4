import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi


from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("/home/abcd/Documents/GitHub/aris-repo-4/gui/main/main.ui", self)  # UI 파일 경로를 적어주세요

        # 버튼과 연결
        self.select_ice_cream.clicked.connect(self.print_one)
        self.log_in.clicked.connect(self.print_two)
        self.select_game.clicked.connect(self.print_three)

    def print_one(self):
        print("아이스크림 주문")

    def print_two(self):
        print("로그인")

    def print_three(self):
        print("게임 시작")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
