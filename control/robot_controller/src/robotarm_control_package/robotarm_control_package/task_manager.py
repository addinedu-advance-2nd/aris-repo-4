import rclpy as rp
from rclpy.action import ActionClient
from rclpy.node import Node
from robot_msgs.action import RobotOrder
from robot_msgs.msg import UserOrder

IcecreamDict = {'strawberry':1}
ToppingDict = {'a':1, 'b':2, 'c':3}
ToppingTypeDict = {'top':1, 'bottom':2}

class TaskManager(Node):
    def __init__(self):
        super().__init__('testPublisher')
        # 'test_topic'이라는 토픽에 String 메시지 타입을 발행
        self.action_client = ActionClient(self, RobotOrder, 'robot_order')
        self.order_subscriber = self.create_subscription(UserOrder, '/user_order', self.user_order_callback, 10)
        self.order_queue = []

    def user_order_callback(self, msg):
        action = msg.action
        icecream = IcecreamDict[msg.icecream]
        topping = ToppingDict[msg.topping]
        topping_type = ToppingTypeDict[msg.topping_type]

        if len(self.order_queue) == 0:
            self.order_queue.append([action, icecream, topping, topping_type])
            print('order queue :',len(self.order_queue))
            self.send_goal(self.order_queue[0])
        elif self.order_queue[0][0] == 'icecreaming' and action == 'icecreaming':
            self.order_queue.append([action, icecream, topping, topping_type])
            print('order queue :',len(self.order_queue))


    def send_goal(self, msg):
        goal_msg = RobotOrder.Goal()
        goal_msg.order_type = msg[0]    #action
        goal_msg.tray_num = 1
        goal_msg.topping_num = msg[2]  #topping
        goal_msg.topping_type = msg[3]    #topping_type
        print(goal_msg)

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

        self.order_queue.pop(0)
        print('order queue :',len(self.order_queue))

        if len(self.order_queue) > 0:
            self.send_goal(self.order_queue[0])
        

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        print(feedback)

def main(args=None):
    rp.init(args=args)
    task_manager = TaskManager()

    try:
        rp.spin(task_manager)  # 노드 실행

    finally:
        task_manager.destroy_node()
        rp.shutdown()

if __name__ == '__main__':
    main()