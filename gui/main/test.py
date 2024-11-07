import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox

# Order_ice_cream 클래스 정의
class Order_ice_cream(Node):
    def __init__(self):
        super().__init__('Order_ice_cream')
        self.publisher_ = self.create_publisher(String, 'order', 10)

    def publish_message(self):
        msg = String()
        msg.data = 'Hello, ROS 2!'
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.publisher_.publish(msg)

# DynamicButtonWidget 정의
class DynamicButtonWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('DB에서 동적으로 버튼 생성')
        self.setGeometry(30, 150, 1700, 500)

        # 버튼들을 관리할 리스트
        self.ice_button_buttons = []
        self.topping = []
        self.topping_type = []

        # DB에서 가져온 예시 데이터 (버튼 이름들)
        button_groups = {
            1: ['Chocolate', 'Vanilla', 'Strawberry'],  # 그룹 1
            2: ['Chocoball', 'Caramel', 'Strawberry Topping'],  # 그룹 2
            3: ['Middle', 'Bottom']  # 그룹 3
        }

        # 페이지 2의 레이아웃 생성
        self.page_layout = QHBoxLayout(self)

        # 각 그룹을 반복하면서 버튼 그룹을 생성
        for group_id, buttons in button_groups.items():
            # 각 그룹에 대해 그룹 박스를 생성
            group_box = QGroupBox(f'그룹 {group_id}')
            group_layout = QVBoxLayout()

            # 버튼을 생성하여 레이아웃에 추가
            for button_name in buttons:
                button = QPushButton(button_name)
                button.setFixedSize(200, 120)
                group_layout.addWidget(button, alignment=Qt.AlignCenter)
                button.setObjectName(f"{button_name.lower()}_button")
                for group, buttons in button_groups.items():
                    if group == 1:
                        for button in buttons:
                            self.ice_button_buttons.append(button)
                    elif group == 2:
                        for button in buttons:
                            self.topping.append(button)
                    elif group == 3:
                        for button in buttons:
                            self.topping_type.append(button)  # 버튼을 리스트에 추가
                button.clicked.connect(lambda _, b=button_name: self.on_button_click(b))  # 버튼 클릭 시 이벤트 연결
                group_layout.addWidget(button)
            
            group_box.setLayout(group_layout)
            self.page_layout.addWidget(group_box)

        self.setLayout(self.page_layout)

    def on_button_click(self, button_name):
        print(f"클릭된 버튼: {button_name}")

# MainWindow 클래스 정의
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 각 페이지 UI 파일 로드
        self.page1 = uic.loadUi("./main_page.ui")
        self.page2 = uic.loadUi("./select_ice_cream_page.ui")
        self.page3 = uic.loadUi("./payment_information_page.ui")
        self.page4 = uic.loadUi("./wait_page_page.ui")
        self.page5 = AdminPage()

        # DynamicButtonWidget 인스턴스 생성
        self.dynamic_button_widget = DynamicButtonWidget()
        self.page2.layout().addWidget(self.dynamic_button_widget)  # page2에 동적 버튼 위젯 추가

        # 스택 위젯 설정
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)
        self.stacked_widget.addWidget(self.page4)
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
        

        # 그룹별 버튼 설정
        self.ice_cream_buttons = self.dynamic_button_widget.ice_button_buttons  # DynamicButtonWidget에서 생성한 버튼 리스트 참조
        self.topping_buttons = self.dynamic_button_widget.topping
        self.method_buttons = self.dynamic_button_widget.topping_type

        # 단일,다중 선택
        self.setup_button_group(self.ice_cream_buttons, "magenta", multi_select=False)
        self.setup_button_group(self.topping_buttons, "orange", multi_select=True)
        self.setup_button_group(self.method_buttons, "cyan", multi_select=False)
        

        # ROS2 Talker 노드 초기화
        self.ros2_talker = Order_ice_cream()

        # 창을 최대화된 상태로 표시
        self.showMaximized()

    def setup_button_group(self, buttons, selected_color, multi_select):
        for button in buttons:
            button.setStyleSheet("background-color: lightgray; color: black;")
            button.clicked.connect(lambda _, btn=button: self.select_button(buttons, btn, selected_color, multi_select))

    def select_button(self, button_group, selected_button, color, multi_select):
        if not multi_select:
            for button in button_group:
                button.setStyleSheet("background-color: lightgray; color: black;")
        
        current_color = selected_button.styleSheet()
        selected_button.setStyleSheet(
            f"background-color: lightgray; color: black;" if "background-color: " + color in current_color else f"background-color: {color}; color: black;"
        )
        self.check_selection_complete()

    def check_selection_complete(self):
        # 모든 그룹의 선택 상태 확인
        ice_cream_selected = any(button.styleSheet() == "background-color: magenta; color: black;" for button in self.ice_cream_buttons)

        # 'select_complete' 버튼 활성화
        self.page2.select_complete.setEnabled(ice_cream_selected)

    def show_page2(self):
        self.stacked_widget.setCurrentWidget(self.page2)

    def show_page1(self):
        self.stacked_widget.setCurrentWidget(self.page1)

    def show_page3(self):
        self.stacked_widget.setCurrentWidget(self.page3)

    def show_page4(self):
        self.stacked_widget.setCurrentWidget(self.page4)

# 메인 함수 정의
def main(args=None):
    rclpy.init(args=args)  # ROS 2 초기화

    # PyQt 애플리케이션 초기화
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # PyQt 애플리케이션 실행
    sys.exit(app.exec_())

# 스크립트 실행 시 main() 함수 호출
if __name__ == "__main__":
    main()
