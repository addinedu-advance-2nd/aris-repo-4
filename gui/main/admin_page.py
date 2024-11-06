import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore

class AdminPage(QtWidgets.QMainWindow):  # QMainWindow로 변경
    def __init__(self):
        super().__init__()

        self.page5 = uic.loadUi("./admin_page.ui")

        # 스택 위젯 생성 및 중앙 위젯으로 설정
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # 페이지를 스택 위젯에 추가
        self.stacked_widget.addWidget(self.page5)  # 관리자 페이지

        # 창을 최대화된 상태로 표시
        self.showMaximized()


        ice_cream_list = (" ", "초코 아이스크림", "딸기 아이스크림", "바닐라 아이스크림", "품절")
        topping_list = (" ", "초코", "캬라멜", "딸기", "품절")
        self.setup_combo_box(self.page5.ice_cream_combobox_1, ice_cream_list, "아이스크림 1")
        self.setup_combo_box(self.page5.ice_cream_combobox_2, ice_cream_list, "아이스크림 2")
        self.setup_combo_box(self.page5.ice_cream_combobox_3, ice_cream_list, "아이스크림 3")
        self.setup_combo_box(self.page5.topping_combobox_1, topping_list, "토핑 1")
        self.setup_combo_box(self.page5.topping_combobox_2, topping_list, "토핑 2")
        self.setup_combo_box(self.page5.topping_combobox_3, topping_list, "토핑 3")

    def setup_combo_box(self, combo_box, items, combo_box_name):
        """콤보박스를 설정하고 선택된 항목 출력 연결"""
        combo_box.addItems(items)
        combo_box.currentTextChanged.connect(lambda: self.on_combo_box_change(combo_box, combo_box_name))

    def on_combo_box_change(self, combo_box, combo_box_name):
        """콤보박스에서 선택된 값 출력"""
        selected_menu = combo_box.currentText()
        print(f"{combo_box_name}에서 선택된 메뉴는: {selected_menu}")




    def show_page5(self):
        self.stacked_widget.setCurrentWidget(self.page5)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AdminPage()  # MainWindow에서 AdminPage로 수정
    window.show()
    sys.exit(app.exec_())
