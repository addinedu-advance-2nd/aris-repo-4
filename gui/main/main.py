import sys
import rclpy as rp
from admin_page import AdminPage
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QObject, QThread
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox
from robot_msgs.msg import UserOrder
from robot_msgs.msg import RobotState

'''
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
'''


class RobotStateSubscriber(Node, QObject):
    msg_received = pyqtSignal(list)

    def __init__(self):
        Node.__init__(self, 'robot_state_subscriber_UI')
        QObject.__init__(self)

        self.subscription = self.create_subscription(RobotState, '/robot_state', self.robot_state_sub_callback, 10)
        self.subscription
    
    def robot_state_sub_callback(self, msg):
        # temperature_list = list(msg.temperatures)
        # self.msg_received.emit(temperature_list)
        msg_list = list(msg)
        self.msg_received.emit(msg_list)

class Ros2ExecutorThread(QThread):
    def __init__(self):
        super().__init__()
        self.executor = MultiThreadedExecutor()
        self.robot_state_subscriber = RobotStateSubscriber()
        self.executor.add_node(self.robot_state_subscriber)
    
    def run(self):
        
        self.executor.spin()
    
    def stop(self):
        self.executor.shutdown()
        


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
                
                if group_id == 1:
                    self.ice_button_buttons.append(button)
                elif group_id == 2:
                    self.topping.append(button)
                elif group_id == 3:
                    self.topping_type.append(button)
                
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

        rp.init()
        self.node = rp.create_node('ice_cream_selector')
        self.publisher = self.node.create_publisher(UserOrder, '/user_order',10)
        self.executor_thread = Ros2ExecutorThread()
        self.executor_thread.robot_state_subscriber.msg_received.connect(self.update_state)
        self.executor_thread.start()

        self.ice_cream_selected = None
        self.topping_selected = None
        self.topping_type_selected = None

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
        self.page2.select_complete.clicked.connect(lambda: (self.publish_selection(), self.show_page3()))
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
        
        
        # 페이지 전환 버튼 연결 (예시로 이미지 클릭 시 다른 페이지로 이동)
        self.page1.logo.mouseDoubleClickEvent = self.on_image_click


        # ROS2 Talker 노드 초기화
        #self.ros2_talker = Order_ice_cream()

        # 창을 최대화된 상태로 표시
        self.showMaximized()



        # mouseDoubleClickEvent를 재정의하여 로고 더블클릭 시 이벤트 처리
    def mouseDoubleClickEvent(self, event):
        # 더블클릭이 로고에서 발생한 경우에만 처리
        if event.source() == self.page1.logo:
            print("로고 클릭! 관리자 페이지로 전환합니다.")
            self.show_page5()  # 관리자 페이지로 전환

        

        
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
        self.update_selection(button_group, selected_button)
        self.check_selection_complete()
    
    def update_selection(self, button_group, selected_button):
        # 선택 상태를 업데이트
        if button_group == self.ice_cream_buttons:
            self.ice_cream_selected = selected_button.text()  # 예: "초코 아이스크림"
        elif button_group == self.topping_buttons:
            self.topping_selected = selected_button.text()    # 예: "초코볼"
        elif button_group == self.method_buttons:
            self.method_selected = selected_button.text()     # 예: "가운데"

    def reset_button_colors(self):
        # 모든 선택 버튼 색상 초기화 및 'select_complete' 비활성화
        for button in self.ice_cream_buttons + self.topping_buttons + self.method_buttons:
        #for button in self.ice_cream_buttons + self.method_buttons:
            button.setStyleSheet("background-color: lightgray; color: black;")
        self.page2.select_complete.setEnabled(False)
        self.ice_cream_selected = None
        self.topping_selected = None
        self.method_selected = None

    def check_selection_complete(self):
        # 모든 그룹의 선택 상태 확인
        ice_cream_selected = any(button.styleSheet() == "background-color: magenta; color: black;" for button in self.ice_cream_buttons)
        topping_selected = any(button.styleSheet() == "background-color: orange; color: black;" for button in self.topping_buttons)
        method_selected = any(button.styleSheet() == "background-color: cyan; color: black;" for button in self.method_buttons)

        # 모든 그룹이 선택되었을 때 'select_complete' 버튼 활성화
        self.page2.select_complete.setEnabled(ice_cream_selected and topping_selected and method_selected)

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
    
    def publish_selection(self):
        # ROS2 메시지에 선택 상태를 설정하고 발행
        msg = UserOrder()
        msg.action = 'icecreaming'
        msg.icecream = self.ice_cream_selected
        msg.topping = self.topping_selected
        msg.topping_type = self.method_selected
        self.publisher.publish(msg)
        self.node.get_logger().info(f"Ice Cream: {self.ice_cream_selected}, Topping: {self.topping_selected}, Topping_type: {self.method_selected}")

    def robot_state_sub_callback(self, msg):
        print(msg.temperatures)
    
    def update_state(self, msg):
        print(msg)

    def closeEvent(self, event):
        self.executor_thread.stop()
        self.robot_state_subscriber.destroy_node()
        rp.shutdown()
        event.accept()

# 메인 함수 정의
def main(args=None):
    #rp.init(args=args)  # ROS 2 초기화

    # PyQt 애플리케이션 초기화
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # PyQt 애플리케이션 실행
    sys.exit(app.exec_())

# 스크립트 실행 시 main() 함수 호출
if __name__ == "__main__":
    main()