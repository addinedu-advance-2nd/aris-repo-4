# pip install PyQt5==5.14.2

import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # 첫 번째 페이지 UI 파일 로드
        self.page1 = uic.loadUi("./main.ui")
        
        # 두 번째 페이지 UI 파일 로드
        self.page2 = uic.loadUi("./select_ice_cream.ui")

        # 세 번째 페이지 UI 파일 로드
        self.page3 = uic.loadUi("./payment_information.ui")

        # 네 번째 페이지 UI 파일 로드
        self.page4 = uic.loadUi("./wait_page.ui")
                
        
        # 스택 위젯 생성
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)
        
        # 페이지를 스택 위젯에 추가
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)
        self.stacked_widget.addWidget(self.page4)

        # 이미지 추가
        self.add_image_to_label()


        
        # 버튼 클릭 시 페이지 전환 연결
        self.page1.select_ice_cream.clicked.connect(self.show_page2)
        self.page2.back_button.clicked.connect(self.show_page1)
        self.page2.select_complete.clicked.connect(self.show_page3)
        self.page3.back_button.clicked.connect(self.show_page2)


        # 페이지3에서 5초 후에 페이지4로 이동하기 위한 타이머 설정
        self.timer = QtCore.QTimer(self)
        self.timer.setSingleShot(True)  # 단 한번만 실행
        self.timer.timeout.connect(self.show_page4)


        # 각 그룹의 버튼을 설정
        self.ice_cream_buttons = [self.page2.chocolate_ice_cream, self.page2.strawberry_ice_cream, self.page2.vanilla_ice_cream]
        self.topping_buttons = [self.page2.chocoball_topping, self.page2.caramel_button, self.page2.strawberry_button]
        self.method_buttons = [self.page2.middle_button, self.page2.bottom_button]
        
        # 각 버튼 초기화 및 클릭 연결 설정
        self.setup_button_group(self.ice_cream_buttons, "magenta")
        self.setup_button_group(self.topping_buttons, "orange")
        self.setup_button_group(self.method_buttons, "cyan")

        # 창을 최대화된 상태로 표시
        self.showMaximized()

    def add_image_to_label(self):
        # QGraphicsScene 생성
        scene = QtWidgets.QGraphicsScene(self)
        
        # QPixmap 생성
        pixmap = QtGui.QPixmap("./image/image.png")  # 이미지 파일 경로
        if not pixmap.isNull():  # 이미지가 유효한지 확인
            # QPixmap을 QGraphicsPixmapItem으로 변환하여 scene에 추가
            scene.addPixmap(pixmap)
            # QGraphicsView에 Scene 설정
            self.page4.graphicsView.setScene(scene)
            self.page4.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)
            self.page4.graphicsView.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)
        else:
            print("이미지를 로드할 수 없습니다.")



    def setup_button_group(self, buttons, selected_color):
        # 그룹의 모든 버튼 초기 색상 설정 및 클릭 시 선택 상태 설정
        for button in buttons:
            button.setStyleSheet("background-color: lightgray; color: black;")
            button.clicked.connect(lambda _, btn=button: self.select_button(buttons, btn, selected_color))

    def show_page2(self):
        self.stacked_widget.setCurrentWidget(self.page2)

    def show_page1(self):
        self.stacked_widget.setCurrentWidget(self.page1)
        self.reset_button_colors() #페이지 전환 시 버튼 색상 초기화

    def show_page3(self):
        self.stacked_widget.setCurrentWidget(self.page3)
        self.timer.start(1000)  # 5초 후에 show_page4 호출
    
    def show_page4(self):
        self.stacked_widget.setCurrentWidget(self.page4)

    def select_button(self, button_group, selected_button, color):
        # 선택된 그룹의 모든 버튼을 기본 색상으로 리셋
        for button in button_group:
            button.setStyleSheet("background-color: lightgray; color: black;")
        # 선택된 버튼을 지정된 색상으로 설정
        selected_button.setStyleSheet(f"background-color: {color}; color: black;")
        self.check_selection_complete()  # 선택 상태 확인

    def reset_button_colors(self):
        # 모든 아이스크림, 토핑, 방법 버튼의 색상을 초기화
        for button in self.ice_cream_buttons + self.topping_buttons + self.method_buttons:
            button.setStyleSheet("background-color: lightgray; color: black;")
        self.page2.select_complete.setEnabled(False)


    def check_selection_complete(self):
        # 모든 버튼 그룹의 선택 여부 확인
        ice_cream_selected = any(button.styleSheet() == "background-color: magenta; color: black;" for button in self.ice_cream_buttons)
        topping_selected = any(button.styleSheet() == "background-color: orange; color: black;" for button in self.topping_buttons)
        method_selected = any(button.styleSheet() == "background-color: cyan; color: black;" for button in self.method_buttons)

        # 모든 선택이 되었을 경우 select_complete 버튼 활성화
        if ice_cream_selected and topping_selected and method_selected:
            self.page2.select_complete.setEnabled(True)
        else:
            self.page2.select_complete.setEnabled(False)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
