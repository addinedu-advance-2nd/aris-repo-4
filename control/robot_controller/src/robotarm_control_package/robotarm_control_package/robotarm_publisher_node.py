import rclpy as rp
from rclpy.action import ActionClient
from rclpy.node import Node
from robot_msgs.action import RobotOrder

class TestPublisher(Node):
    def __init__(self):
        super().__init__('testPublisher')
        # 'test_topic'이라는 토픽에 String 메시지 타입을 발행
        self.action_client = ActionClient(self, RobotOrder, 'robot_order')
        # 1초 간격으로 타이머 설정

    def send_goal(self, msg):
        goal_msg = RobotOrder.Goal()
        goal_msg.order = 'icecreaming'

        self.action_client.wait_for_server()

        self.send_goal_future = self.action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

        self.send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            print('goal rejected')
            return

        print('goal accepted')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        print(result)
        rp.shutdown

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        print(feedback)

def main(args=None):
    rp.init(args=args)
    test_publisher = TestPublisher()

    goal_msg = RobotOrder.Goal()
    goal_msg.order = 'asdf'
    test_publisher.send_goal(goal_msg)
    try:
        rp.spin(test_publisher)  # 노드 실행
    except KeyboardInterrupt:
        pass
    finally:
        test_publisher.destroy_node()
        rp.shutdown()

if __name__ == '__main__':
    main()