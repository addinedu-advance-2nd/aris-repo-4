import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore


class AdminPage(QtWidgets.QMainWindow):  # QMainWindow로 변경
    def __init__(self):
        super().__init__()

        # UI 로드 및 스택 위젯 설정
        self.page5 = uic.loadUi("./admin_page.ui")

        # 스택 위젯 생성 및 중앙 위젯으로 설정
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # 페이지를 스택 위젯에 추가
        self.stacked_widget.addWidget(self.page5)  # 관리자 페이지

        # 창을 최대화된 상태로 표시
        self.showMaximized()

        # 콤보박스 설정
        #print(selectIceCream())

        ice_cream_list = (" ", "초코 아이스크림", "딸기 아이스크림", "바닐라 아이스크림", "품절")
       # ice_cream_list = str(selectIceCream())
        topping_list = (" ", "초코", "캬라멜", "딸기", "품절")
        self.setup_combo_box(self.page5.ice_cream_combobox_1, ice_cream_list, "아이스크림 1")
        self.setup_combo_box(self.page5.ice_cream_combobox_2, ice_cream_list, "아이스크림 2")
        self.setup_combo_box(self.page5.ice_cream_combobox_3, ice_cream_list, "아이스크림 3")
        self.setup_combo_box(self.page5.topping_combobox_1, topping_list, "토핑 1")
        self.setup_combo_box(self.page5.topping_combobox_2, topping_list, "토핑 2")
        self.setup_combo_box(self.page5.topping_combobox_3, topping_list, "토핑 3")
        
        # 이미지 추가 (그래픽 뷰에 이미지 삽입)
        self.add_image_to_label("./image/lite6.png", self.page5.lite6)

        # QLabel 딕셔너리 설정
        self.labels = {
            "J1_angle": self.page5.findChild(QtWidgets.QLabel, "J1_angle"),
            "J2_angle": self.page5.findChild(QtWidgets.QLabel, "J2_angle"),
            "J3_angle": self.page5.findChild(QtWidgets.QLabel, "J3_angle"),
            "J4_angle": self.page5.findChild(QtWidgets.QLabel, "J4_angle"),
            "J5_angle": self.page5.findChild(QtWidgets.QLabel, "J5_angle"),
            "J6_angle": self.page5.findChild(QtWidgets.QLabel, "J6_angle"),
        }

        # data 딕셔너리를 사용하여 QLabel 업데이트
        data = {
            "J1": 10,
            "J2": 20,
            "J3": 30,
            "J4": 40,
            "J5": 50,
            "J6": 60
        }
        self.update_labels(data)

         # Close button 연결
        self.page5.admin_page_close_button.clicked.connect(self.close_with_data)

    def setup_combo_box(self, combo_box, items, combo_box_name):
        """콤보박스를 설정하고 선택된 항목 출력 연결"""
        combo_box.addItems(items)
        combo_box.currentTextChanged.connect(lambda: self.on_combo_box_change(combo_box, combo_box_name))

    def on_combo_box_change(self, combo_box, combo_box_name):
        """콤보박스에서 선택된 값 출력"""
        selected_menu = combo_box.currentText()
        #print(f"{combo_box_name}에서 선택된 메뉴는: {selected_menu}")

    def update_labels(self, data):
        """data 딕셔너리의 값을 각 QLabel에 업데이트"""
        for joint, value in data.items():
            label_name = f"{joint}_angle"
            if label_name in self.labels and self.labels[label_name] is not None:
                self.labels[label_name].setText(str(value)+"°C")

    def show_page5(self):
        """page5를 표시"""
        self.stacked_widget.setCurrentWidget(self.page5)

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


    def close_with_data(self):
    #콤보박스 선택 상태를 딕셔너리에 저장하고 출력한 후 창을 닫음
        combo_box_data = {
            "ice_cream_1": self.page5.ice_cream_combobox_1.currentText(),
            "ice_cream_2": self.page5.ice_cream_combobox_2.currentText(),
            "ice_cream_3": self.page5.ice_cream_combobox_3.currentText(),
            "topping_1": self.page5.topping_combobox_1.currentText(),
            "topping_2": self.page5.topping_combobox_2.currentText(),
            "topping_3": self.page5.topping_combobox_3.currentText(),
        }
        print("콤보박스 선택 상태:", combo_box_data)
        self.close()  # 창 닫기


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AdminPage()  # MainWindow에서 AdminPage로 수정
    window.show()
    sys.exit(app.exec_())
