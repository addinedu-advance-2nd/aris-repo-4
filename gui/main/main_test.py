# pip install PyQt5==5.14.2

import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from admin_page import AdminPage

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 각 페이지 UI 파일 로드
        self.page1 = uic.loadUi("./main_page.ui")
        self.page2 = uic.loadUi("./select_ice_cream_page.ui")
        self.page3 = uic.loadUi("./payment_information_page.ui")
        self.page4 = uic.loadUi("./wait_page_page.ui")
        self.page5 = AdminPage()

        # 스택 위젯 생성 및 중앙 위젯으로 설정
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # 각 페이지를 스택 위젯에 추가
        self.stacked_widget.addWidget(self.page1)  # 메인 페이지
        self.stacked_widget.addWidget(self.page2)  # 아이스크림 선택 페이지
        self.stacked_widget.addWidget(self.page3)  # 결제 대기 페이지
        self.stacked_widget.addWidget(self.page4)  # 아이스크림 만들기 대기 페이지
        self.stacked_widget.addWidget(self.page5)  # 관리자 페이지

        # 이미지 추가 (그래픽 뷰에 이미지 삽입)
        self.add_image_to_label("./image/last_pic.png", self.page4.last_pic)
        self.add_image_to_label("./image/logo.png", self.page1.logo)
        self.add_image_to_label("./image/main_pic.png", self.page1.main_pic)

        # 페이지 전환을 위한 버튼 클릭 이벤트 설정
        self.page1.select_ice_cream.clicked.connect(self.show_page2)
        self.page2.back_button.clicked.connect(self.show_page1)
        self.page2.select_complete.clicked.connect(self.show_page3)
        self.page3.back_button.clicked.connect(self.show_page2)

        # 페이지3에서 페이지4로 1초 후에 이동하도록 타이머 설정
        self.timer = QtCore.QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.show_page4)

        # 버튼 그룹 설정 (색상 설정 포함)
        self.ice_cream_buttons = [self.page2.chocolate_ice_cream, self.page2.strawberry_ice_cream, self.page2.vanilla_ice_cream]
        self.topping_buttons = [self.page2.chocoball_topping, self.page2.caramel_button, self.page2.strawberry_button]
        self.method_buttons = [self.page2.middle_button, self.page2.bottom_button]
        
        self.setup_button_group(self.ice_cream_buttons, "magenta", multi_select=False)
        self.setup_button_group(self.topping_buttons, "orange", multi_select=True)
        self.setup_button_group(self.method_buttons, "cyan", multi_select=False)

        # 페이지 전환 버튼 연결 (예시로 이미지 클릭 시 다른 페이지로 이동)
        self.page1.logo.mouseDoubleClickEvent = self.on_image_click

        # 창을 최대화된 상태로 표시
        self.showMaximized()

    def add_image_to_label(self, pic_link, graphics_view):
        # QGraphicsView에 이미지를 로드하고 자동으로 크기를 조정
        scene = QtWidgets.QGraphicsScene(self)
        pixmap = QtGui.QPixmap(pic_link)
        if not pixmap.isNull():  # 이미지가 유효한지 확인
            item = scene.addPixmap(pixmap)
            graphics_view.setScene(scene)
            graphics_view.setRenderHint(QtGui.QPainter.Antialiasing)
            graphics_view.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)
            graphics_view.setAlignment(QtCore.Qt.AlignCenter)
            self.fit_image_to_graphics_view(graphics_view, item)
        else:
            print("이미지를 로드할 수 없습니다:", pic_link)

    def fit_image_to_graphics_view(self, graphics_view, pixmap_item):
        # QGraphicsView의 크기에 맞춰 이미지를 비율에 맞게 조정
        graphics_view.fitInView(pixmap_item, QtCore.Qt.KeepAspectRatio)
        #최소 크기 설정 및 이미지 확대
        min_size = 500 # 최소 크기 지정
        view_rect = graphics_view.rect()

            # fitInView 사용 후, 크기가 너무 작으면 scale을 사용하여 이미지 크기 확대
        graphics_view.fitInView(pixmap_item, QtCore.Qt.KeepAspectRatio)
        if pixmap_item.pixmap().width() < min_size or pixmap_item.pixmap().height() < min_size:
            scale_factor = max(min_size / pixmap_item.pixmap().width(), min_size / pixmap_item.pixmap().height())
            graphics_view.scale(scale_factor, scale_factor)

    def on_image_click(self, event):
        # 이미지 더블클릭 시 관리자 페이지로 전환
        print("Logo clicked! Switching to AdminPage.")
        #self.stacked_widget.setCurrentWidget(self.page5)  # 기존 페이지 5를 AdminPage로 전환
        if not hasattr(self, 'admin_page_window'):  # 이미 창이 열려 있는지 확인
            self.admin_page_window = AdminPage()  # AdminPage 객체 생성
            self.admin_page_window.show()  # AdminPage 창 열기


    def resizeEvent(self, event):
        # 창 크기가 변경될 때마다 각 QGraphicsView의 이미지 크기 자동 조정
        for page, view_attr in [(self.page1, 'logo'), (self.page1, 'main_pic'), (self.page4, 'last_pic')]:
            graphics_view = getattr(page, view_attr, None)
            if graphics_view and graphics_view.scene():
                pixmap_item = graphics_view.scene().items()[0]
                self.fit_image_to_graphics_view(graphics_view, pixmap_item)
        super().resizeEvent(event)

    def setup_button_group(self, buttons, selected_color, multi_select):
        # 각 버튼 그룹의 초기 색상 설정 및 클릭 시 색상 변경
        for button in buttons:
            button.setStyleSheet("background-color: lightgray; color: black;")
            button.clicked.connect(lambda _, btn=button: self.select_button(buttons, btn, selected_color, multi_select))


    def show_page2(self):
        self.stacked_widget.setCurrentWidget(self.page2)

    def show_page1(self):
        self.stacked_widget.setCurrentWidget(self.page1)
        self.reset_button_colors()  # 페이지 전환 시 버튼 색상 초기화

    def show_page3(self):
        self.stacked_widget.setCurrentWidget(self.page3)
        self.timer.start(1000)  # 1초 후에 show_page4 호출

    def show_page4(self):
        self.stacked_widget.setCurrentWidget(self.page4)

    def show_page5(self):
        self.stacked_widget.setCurrentWidget(self.page5)

    def select_button(self, button_group, selected_button, color, multi_select):
        # 단일 선택 그룹의 경우 기존 선택을 초기화
        if not multi_select:
            for button in button_group:
                button.setStyleSheet("background-color: lightgray; color: black;")
        
        # 선택된 버튼의 색상을 지정된 색상으로 설정
        current_color = selected_button.styleSheet()
        selected_button.setStyleSheet(
            f"background-color: lightgray; color: black;" if "background-color: " + color in current_color else f"background-color: {color}; color: black;"
        )
        self.check_selection_complete()

    def reset_button_colors(self):
        # 모든 선택 버튼 색상 초기화 및 'select_complete' 비활성화
        for button in self.ice_cream_buttons + self.topping_buttons + self.method_buttons:
        #for button in self.ice_cream_buttons + self.method_buttons:
            button.setStyleSheet("background-color: lightgray; color: black;")
        self.page2.select_complete.setEnabled(False)

    def check_selection_complete(self):
        # 모든 그룹의 선택 상태 확인
        ice_cream_selected = any(button.styleSheet() == "background-color: magenta; color: black;" for button in self.ice_cream_buttons)
        topping_selected = any(button.styleSheet() == "background-color: orange; color: black;" for button in self.topping_buttons)
        method_selected = any(button.styleSheet() == "background-color: cyan; color: black;" for button in self.method_buttons)

        # 모든 그룹이 선택되었을 때 'select_complete' 버튼 활성화
        self.page2.select_complete.setEnabled(ice_cream_selected and topping_selected and method_selected)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
