import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class ColorChangeButton(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # 레이아웃 설정
        layout = QVBoxLayout()
        
        # 버튼 생성
        self.button = QPushButton('Click me', self)
        self.button.setStyleSheet("background-color: lightgray; color: black;")  # 초기 색상 설정
        self.button.clicked.connect(self.change_color)  # 클릭 시 색상 변경 연결
        
        # 레이아웃에 버튼 추가
        layout.addWidget(self.button)
        self.setLayout(layout)
        
        # 창 설정
        self.setWindowTitle('Color Change Button')
        self.setGeometry(300, 300, 200, 100)
        
    def change_color(self):
        # 클릭할 때마다 색상 토글
        if self.button.styleSheet() == "background-color: lightgray; color: black;":
            self.button.setStyleSheet("background-color: lightblue; color: white;")
        else:
            self.button.setStyleSheet("background-color: lightgray; color: black;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ColorChangeButton()
    ex.show()
    sys.exit(app.exec_())
