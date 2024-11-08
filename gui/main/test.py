import sys
import cv2
import mediapipe as mp
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QImage, QPainter, QColor

class MovingCircle(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("관절 각도 감지로 클릭")  # 창 제목 설정
        self.setGeometry(100, 100, 800, 600)  # 창 위치와 크기 설정

        # Mediapipe 손 인식 초기화
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.capture = cv2.VideoCapture(0)  # 카메라 캡처 객체 생성

        # 초기 원의 위치와 픽셀 임계값
        self.circle_position = QPoint(400, 300)
        self.prev_position = self.circle_position
        self.pixel_threshold = 10  # 픽셀 임계값 설정 (미세한 움직임 무시)

        # 버튼 리스트와 상태
        self.buttons = []
        self.button_states = [False] * 5
        for i in range(5):
            button = QPushButton(f"Button {i + 1}", self)
            # 버튼을 화면에 중앙에 배치 (가로로 배치)
            button.setGeometry(50 + i * 120, 400, 100, 50)
            button.setStyleSheet("background-color: red; color: white;")  # 버튼 색깔 설정
            button.clicked.connect(self.button_clicked)
            self.buttons.append(button)

        # 각도 변수 초기화
        self.angle_pip_dip = 0
        self.angle_dip_tip = 0
        self.angle_mcp_pip = 0

        # 손바닥 방향 각도 초기화
        self.roll_angle = 0
        self.pitch_angle = 0
        self.yaw_angle = 0

        # 타이머 설정
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        ret, frame = self.capture.read()
        if not ret:
            return

        # Mediapipe 손 인식
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                # 손가락 각도 계산 및 버튼 클릭 감지
                self.calculate_angles(landmarks)

        # 이미지 표시
        self.display_frame(frame)

    def calculate_angles(self, landmarks):
        # 각도 계산 (예시로 첫 번째 손가락의 관절 각도 계산)
        self.angle_pip_dip = self.calculate_angle(landmarks[0], landmarks[1], landmarks[2])
        self.angle_dip_tip = self.calculate_angle(landmarks[1], landmarks[2], landmarks[3])
        self.angle_mcp_pip = self.calculate_angle(landmarks[2], landmarks[3], landmarks[4])

        # 각도를 이용하여 버튼 클릭 여부 결정
        if self.angle_pip_dip < 30:  # 예시로 각도에 따른 클릭
            self.click_button(0)  # 첫 번째 버튼 클릭

    def calculate_angle(self, p1, p2, p3):
        # 두 벡터 사이의 각도 계산 (단순 예시)
        angle = 0
        # 계산 로직 추가
        return angle

    def click_button(self, index):
        if 0 <= index < len(self.buttons):
            self.buttons[index].click()

    def button_clicked(self):
        sender = self.sender()
        index = self.buttons.index(sender)
        print(f"Button {index + 1} clicked")

    def display_frame(self, frame):
        # OpenCV 이미지를 PyQt 화면에 표시
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame_rgb.shape
        bytes_per_line = ch * w
        qimage = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        painter = QPainter(self)
        painter.drawImage(0, 0, qimage)
        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovingCircle()
    window.show()
    sys.exit(app.exec_())
