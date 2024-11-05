import rclpy as rp
from rclpy.action import ActionServer
from rclpy.node import Node

from robot_msgs.action import RobotOrder

import sys
import math
import time
import queue
import datetime
import random
import traceback
import threading
from xarm import version
from xarm.wrapper import XArmAPI

class RobotMain(object):
    """Robot Main Class"""
    def __init__(self, robot, **kwargs):
        self.alive = True
        self._arm = robot
        self._tcp_speed = 100
        self._tcp_acc = 2000
        self._angle_speed = 20
        self._angle_acc = 500
        self._vars = {}
        self._funcs = {}
        self._robot_init()

    # Robot init
    def _robot_init(self):
        self._arm.clean_warn()
        self._arm.clean_error()
        self._arm.motion_enable(True)
        self._arm.set_mode(0)
        self._arm.set_state(0)
        time.sleep(1)
        self._arm.register_error_warn_changed_callback(self._error_warn_changed_callback)
        self._arm.register_state_changed_callback(self._state_changed_callback)
        if hasattr(self._arm, 'register_count_changed_callback'):
            self._arm.register_count_changed_callback(self._count_changed_callback)

    # Register error/warn changed callback
    def _error_warn_changed_callback(self, data):
        if data and data['error_code'] != 0:
            self.alive = False
            self.pprint('err={}, quit'.format(data['error_code']))
            self._arm.release_error_warn_changed_callback(self._error_warn_changed_callback)

    # Register state changed callback
    def _state_changed_callback(self, data):
        if data and data['state'] == 4:
            self.alive = False
            self.pprint('state=4, quit')
            self._arm.release_state_changed_callback(self._state_changed_callback)

    # Register count changed callback
    def _count_changed_callback(self, data):
        if self.is_alive:
            self.pprint('counter val: {}'.format(data['count']))

    def _check_code(self, code, label):
        if not self.is_alive or code != 0:
            self.alive = False
            ret1 = self._arm.get_state()
            ret2 = self._arm.get_err_warn_code()
            self.pprint('{}, code={}, connected={}, state={}, error={}, ret1={}. ret2={}'.format(label, code, self._arm.connected, self._arm.state, self._arm.error_code, ret1, ret2))
        return self.is_alive

    @staticmethod
    def pprint(*args, **kwargs):
        try:
            stack_tuple = traceback.extract_stack(limit=2)[0]
            print('[{}][{}] {}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), stack_tuple[1], ' '.join(map(str, args))))
        except:
            print(*args, **kwargs)

    @property
    def arm(self):
        return self._arm

    @property
    def VARS(self):
        return self._vars

    @property
    def FUNCS(self):
        return self._funcs

    @property
    def is_alive(self):
        if self.alive and self._arm.connected and self._arm.error_code == 0:
            if self._arm.state == 5:
                cnt = 0
                while self._arm.state == 5 and cnt < 5:
                    cnt += 1
                    time.sleep(0.1)
            return self._arm.state < 4
        else:
            return False
        
    def motion_home(self):

        code = self._arm.set_cgpio_analog(0, 0)
        if not self._check_code(code, 'set_cgpio_analog'):
            return
        code = self._arm.set_cgpio_analog(1, 0)
        if not self._check_code(code, 'set_cgpio_analog'):
            return
        
        #press_up
        code = self._arm.set_cgpio_digital(0, 0, delay_sec=0)
        if not self._check_code(code, 'set_cgpio_digital'):
            return
        
        # Joint Motion
        self._angle_speed = 80
        self._angle_acc = 200

        print('motion_home start')
        # designed home
        # code = self._arm.set_servo_angle(angle=[179.0, -17.9, 17.7, 176.4, 61.3, 5.4], speed=self._angle_speed,
        #                                  mvacc=self._angle_acc, wait=True, radius=10.0)
        # if not self._check_code(code, 'set_servo_angle'):
        #     return
        code = self._arm.set_servo_angle(angle=[179.2, -42.1, 7.4, 186.7, 41.5, -1.6], speed=self._angle_speed,
                                         mvacc=self._angle_acc, wait=True, radius=0.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        print('motion_home finish')


    def motion_grab_capsule(self):

        code = self._arm.set_cgpio_analog(0, 5)
        if not self._check_code(code, 'set_cgpio_analog'):
            return
        code = self._arm.set_cgpio_analog(1, 5)
        if not self._check_code(code, 'set_cgpio_analog'):
            return

        # Joint Motion
        self._angle_speed = 100
        self._angle_acc = 100
        
        self._tcp_speed = 100
        self._tcp_acc = 1000

        code = self._arm.close_lite6_gripper()
        if not self._check_code(code, 'close_lite6_gripper'):
            return
        time.sleep(1)
        code = self._arm.open_lite6_gripper()
        if not self._check_code(code, 'open_lite6_gripper'):
            return
        time.sleep(1)
        code = self._arm.stop_lite6_gripper()
        if not self._check_code(code, 'stop_lite6_gripper'):
            return
        time.sleep(1)

        #code = self._arm.set_servo_angle(angle=[175.4, 28.7, 23.8, 84.5, 94.7, -5.6], speed=self._angle_speed,
        #                                 mvacc=self._angle_acc, wait=True, radius=0.0)
        #if not self._check_code(code, 'set_servo_angle'):
        #    return
        
        if self.order_msg['makeReq']['jigNum'] in ['A']:
            code = self._arm.set_servo_angle(angle=[166.1, 30.2, 25.3, 75.3, 93.9, -5.4], speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=0.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            #code = self._arm.set_position(*[-162.5, -21.0, 187.6, -7.7, 84.8, -97.3], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=0.0, wait=True)
            #if not self._check_code(code, 'set_position'):
            #    return
        else :
            
            code = self._arm.set_servo_angle(angle=[166.1, 30.2, 25.3, 75.3, 93.9, -5.4], speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=0.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            
        code = self._arm.open_lite6_gripper()
        if not self._check_code(code, 'open_lite6_gripper'):
            return
        time.sleep(1)
        
        if self.order_msg['makeReq']['jigNum'] == 'A':
            code = self._arm.set_servo_angle(angle=[179.5, 33.5, 32.7, 113.0, 93.1, -2.3], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=0.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            # code = self._arm.set_position(*[-255.4, -139.3, 193.5, -12.7, 87.2, -126.1], speed=self._tcp_speed,
            #                              mvacc=self._tcp_acc, radius=0.0, wait=True)
            # if not self._check_code(code, 'set_position'):
            #    return
            
            code = self._arm.set_position(*[-257.3, -138.3, 192.1, 68.3, 86.1, -47.0], speed=self._tcp_speed,
                                          mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return

        elif self.order_msg['makeReq']['jigNum'] == 'B':

            code = self._arm.set_position(*[-152.3, -129.0, 192.8, 4.8, 89.0, -90.7], speed=self._tcp_speed,
                                          mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return

        elif self.order_msg['makeReq']['jigNum'] == 'C':
            code = self._arm.set_servo_angle(angle=[182.6, 27.8, 27.7, 55.7, 90.4, -6.4], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=0.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            #code = self._arm.set_position(*[-77.1, -147.4, 193.7, -83.8, 85.8, -138.3], speed=self._tcp_speed,
            #                              mvacc=self._tcp_acc, radius=0.0, wait=True)
            #if not self._check_code(code, 'set_position'):
            #    return
            code = self._arm.set_position(*[-76.6, -144.6, 194.3, 5.7, 88.9, -50.1], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return
        
        code = self._arm.close_lite6_gripper()
        if not self._check_code(code, 'close_lite6_gripper'):
            return
        
        time.sleep(1)

        if self.order_msg['makeReq']['jigNum'] == 'C':
            code = self._arm.set_position(z=150, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                          wait=False)
            if not self._check_code(code, 'set_position'):
                return
            
            code = self._arm.set_tool_position(*[0.0, 0.0, -90.0, 0.0, 0.0, 0.0], speed=self._tcp_speed, mvacc=self._tcp_acc, wait=True)
            if not self._check_code(code, 'set_position'):
                return
        else:
            code = self._arm.set_position(z=100, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                          wait=False)
            if not self._check_code(code, 'set_position'):
                return
        self._angle_speed = 160
        self._angle_acc = 200
        code = self._arm.set_servo_angle(angle=[146.1, -10.7, 10.9, 102.7, 92.4, 24.9], speed=self._angle_speed,
                                         mvacc=self._angle_acc, wait=False, radius=20.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
    def motion_place_capsule(self):
        code = self._arm.set_servo_angle(angle=[81.0, -10.8, 6.9, 103.6, 88.6, 9.6], speed=self._angle_speed,
                                         mvacc=self._angle_acc, wait=False, radius=40.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        code = self._arm.set_servo_angle(angle=[10, -20.8, 7.1, 106.7, 79.9, 26.0], speed=self._angle_speed, mvacc=self._angle_acc, wait=False, radius=50.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        #code = self._arm.set_servo_angle(angle=[27.0, -24.9, 7.2, 108.0, 76.4, 32.7], speed=self._angle_speed,
        #                                 mvacc=self._angle_acc, wait=False, radius=40.0)
        #if not self._check_code(code, 'set_servo_angle'):
        #    return
        #code = self._arm.set_servo_angle(angle=[-0.9, -24.9, 10.4, 138.3, 66.0, 19.1], speed=self._angle_speed,
        #                                 mvacc=self._angle_acc, wait=False, radius=40.0)
        #if not self._check_code(code, 'set_servo_angle'):
        #    return
        code = self._arm.set_servo_angle(angle=[8.4, -42.7, 23.7, 177.4, 31.6, 3.6], speed=self._angle_speed,
                                         mvacc=self._angle_acc, wait=False, radius=40.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        # code = self._arm.set_servo_angle(angle=[8.4, -33.1, 51.8, 100.6, 29.8, 77.3], speed=self._angle_speed,
        #                                 mvacc=self._angle_acc, wait=True, radius=0.0)
        # if not self._check_code(code, 'set_servo_angle'):
        #    return
        code = self._arm.set_servo_angle(angle=[8.4, -32.1, 55.1, 96.6, 29.5, 81.9], speed=self._angle_speed,
                                         mvacc=self._angle_acc, wait=True, radius=0.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        # code = self._arm.set_position(*[241.7, 122.5, 487.8, -140, 86.1, -52.4], speed=self._tcp_speed,
        #                              mvacc=self._tcp_acc, radius=0.0, wait=True)
        # if not self._check_code(code, 'set_position'):
        #    return
        # code = self._arm.set_position(*[241.7, 122.5, 467.8, -140, 86.1, -52.4], speed=self._tcp_speed,
        #                              mvacc=self._tcp_acc, radius=0.0, wait=True)
        # if not self._check_code(code, 'set_position'):
        #    return
        code = self._arm.set_position(*[234.9, 135.9, 486.5, 133.6, 87.2, -142.1], speed=self._tcp_speed,
                                      mvacc=self._tcp_acc, radius=0.0, wait=True)
        if not self._check_code(code, 'set_position'):
            return
        code = self._arm.set_position(*[234.9, 135.9, 462.9, 133.6, 87.2, -142.1], speed=self._tcp_speed,
                                      mvacc=self._tcp_acc, radius=20.0, wait=False)
        if not self._check_code(code, 'set_position'):
            return
        code = self._arm.set_cgpio_analog(0, 0)
        if not self._check_code(code, 'set_cgpio_analog'):
            return
        code = self._arm.set_cgpio_analog(1, 5)
        if not self._check_code(code, 'set_cgpio_analog'):
            return
        code = self._arm.open_lite6_gripper()
        if not self._check_code(code, 'open_lite6_gripper'):
            return
        time.sleep(2)
        code = self._arm.stop_lite6_gripper()
        if not self._check_code(code, 'stop_lite6_gripper'):
            return
        time.sleep(0.5)
    
    def motion_grab_cup(self):

        code = self._arm.set_position(*[233.4, 10.3, 471.1, -172.2, 87.3, -84.5], speed=self._tcp_speed,
                                      mvacc=self._tcp_acc, radius=20.0, wait=False)
        if not self._check_code(code, 'set_position'):
            return
        code = self._arm.open_lite6_gripper()
        if not self._check_code(code, 'open_lite6_gripper'):
            return
        time.sleep(1)

        if self.order_msg['makeReq']['cupNum'] in ['A', 'B']:
            code = self._arm.set_servo_angle(angle=[-2.8, -2.5, 45.3, 119.8, -79.2, -18.8], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=False, radius=30.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            # code = self._arm.set_position(*[193.8, -100.2, 146.6, 135.9, -86.0, -55.3], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=0.0, wait=True)
            # if not self._check_code(code, 'set_position'):
            #    return
            code = self._arm.set_position(*[195.0, -96.5, 200.8, -168.0, -87.1, -110.5], speed=self._tcp_speed,
                                          mvacc=self._tcp_acc, radius=10.0, wait=False)
            if not self._check_code(code, 'set_position'):
                return
            #code = self._arm.set_position(*[195.0, -96.5, 145.8, -168.0, -87.1, -110.5], speed=self._tcp_speed,
            #                              mvacc=self._tcp_acc, radius=0.0, wait=True)
            #if not self._check_code(code, 'set_position'):
            #    return
            #code = self._arm.set_position(*[195.5, -96.6, 145.6, 179.0, -87.0, -97.1], speed=self._tcp_speed,
            #                              mvacc=self._tcp_acc, radius=0.0, wait=True)
            #if not self._check_code(code, 'set_position'):
            #    return
            code = self._arm.set_position(*[214.0, -100.2, 145.0, -25.6, -88.5, 95.8], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return
        code = self._arm.close_lite6_gripper()
        if not self._check_code(code, 'close_lite6_gripper'):
            return
        time.sleep(2)

        code = self._arm.set_position(z=120, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                      wait=True)
        if not self._check_code(code, 'set_position'):
            return
        code = self._arm.set_servo_angle(angle=[2.9, -31.0, 33.2, 125.4, -30.4, -47.2], speed=self._angle_speed,
                                         mvacc=self._angle_acc, wait=True, radius=0.0)
        if not self._check_code(code, 'set_servo_angle'):
            return

        code = self._arm.set_cgpio_analog(0, 5)
        if not self._check_code(code, 'set_cgpio_analog'):
            return
        code = self._arm.set_cgpio_analog(1, 5)
        if not self._check_code(code, 'set_cgpio_analog'):
            return

        time.sleep(0.5)
    
    def motion_topping(self):
        print('send')

        if self.order_msg['makeReq']['topping'] == '1':
            code = self._arm.set_servo_angle(angle=[36.6, -36.7, 21.1, 85.6, 59.4, 44.5], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=0.0)
            if not self._check_code(code, 'set_servo_angle'):
                return

            if self.order_msg['makeReq']['jigNum'] == 'C':
                code = self._arm.set_position(*[43.6, 137.9, 350.1, -92.8, 87.5, 5.3], speed=self._tcp_speed,
                                              mvacc=self._tcp_acc, radius=0.0, wait=True)
                if not self._check_code(code, 'set_position'):
                    return
                code = self._arm.set_cgpio_digital(2, 1, delay_sec=0)
                if not self._check_code(code, 'set_cgpio_digital'):
                    return
                code = self._arm.set_position(z=20, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                              wait=False)
                if not self._check_code(code, 'set_position'):
                    return
                code = self._arm.set_pause_time(4)
                if not self._check_code(code, 'set_pause_time'):
                    return
                code = self._arm.set_cgpio_digital(3, 1, delay_sec=0)
                if not self._check_code(code, 'set_cgpio_digital'):
                    return
                code = self._arm.set_pause_time(4)
                if not self._check_code(code, 'set_pause_time'):
                    return
                code = self._arm.set_cgpio_digital(2, 0, delay_sec=0)
                if not self._check_code(code, 'set_cgpio_digital'):
                    return
                
                code = self._arm.set_position(z=-20, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc,
                                              relative=True, wait=False)
                if not self._check_code(code, 'set_position'):
                    return

            elif self.order_msg['makeReq']['jigNum'] in ['B']:
                code = self._arm.set_servo_angle(angle=[55.8, -48.2, 14.8, 86.1, 60.2, 58.7], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=False, radius=20.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                # code = self._arm.set_servo_angle(angle=[87.5, -48.2, 13.5, 125.1, 44.5, 46.2], speed=self._angle_speed,
                #                                 mvacc=self._angle_acc, wait=True, radius=0.0)
                # if not self._check_code(code, 'set_servo_angle'):
                #    return
                code = self._arm.set_servo_angle(angle=[106.5, -39.7, 15.0, 158.7, 40.4, 16.9], speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=0.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_cgpio_digital(1, 1, delay_sec=0)
                if not self._check_code(code, 'set_cgpio_digital'):
                    return
                code = self._arm.set_position(z=20, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                              wait=True)
                if not self._check_code(code, 'set_position'):
                    return
                code = self._arm.set_pause_time(4)
                if not self._check_code(code, 'set_pause_time'):
                    return
                code = self._arm.set_cgpio_digital(3, 1, delay_sec=0)
                if not self._check_code(code, 'set_cgpio_digital'):
                    return
                code = self._arm.set_pause_time(4)
                if not self._check_code(code, 'set_pause_time'):
                    return
                code = self._arm.set_cgpio_digital(1, 0, delay_sec=0)
                if not self._check_code(code, 'set_cgpio_digital'):
                    return
                code = self._arm.set_position(z=-20, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc,
                                              relative=True, wait=False)
                if not self._check_code(code, 'set_position'):
                    return
                code = self._arm.set_servo_angle(angle=[87.5, -48.2, 13.5, 125.1, 44.5, 46.2], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=False, radius=10.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_position(*[43.6, 137.9, 350.1, -92.8, 87.5, 5.3], speed=self._tcp_speed,
                                              mvacc=self._tcp_acc, radius=10.0, wait=False)
                if not self._check_code(code, 'set_position'):
                    return

            elif self.order_msg['makeReq']['jigNum'] == 'A':
                code = self._arm.set_position(*[-200.3, 162.8, 359.9, -31.7, 87.8, 96.1], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=0.0, wait=True)
                if not self._check_code(code, 'set_position'):
                    return
                code = self._arm.set_cgpio_digital(0, 1, delay_sec=0)
                if not self._check_code(code, 'set_cgpio_digital'):
                    return
                code = self._arm.set_pause_time(6)
                if not self._check_code(code, 'set_pause_time'):
                    return
                code = self._arm.set_cgpio_digital(3, 1, delay_sec=0)
                if not self._check_code(code, 'set_cgpio_digital'):
                    return
                code = self._arm.set_pause_time(2)
                if not self._check_code(code, 'set_pause_time'):
                    return
                code = self._arm.set_cgpio_digital(0, 0, delay_sec=0)
                if not self._check_code(code, 'set_cgpio_digital'):
                    return
                code = self._arm.set_servo_angle(angle=[130.0, -33.1, 12.5, 194.3, 51.0, 0.0], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=0.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_position(*[-38.2, 132.2, 333.9, -112.9, 86.3, -6.6], speed=self._tcp_speed,
                                              mvacc=self._tcp_acc, radius=10.0, wait=False)
                if not self._check_code(code, 'set_position'):
                    return
                code = self._arm.set_position(*[43.6, 137.9, 350.1, -92.8, 87.5, 5.3], speed=self._tcp_speed,
                                              mvacc=self._tcp_acc, radius=10.0, wait=False)
                if not self._check_code(code, 'set_position'):
                    return
            #code = self._arm.set_position(*[165.1, 162.9, 362.5, -31.7, 86.6, 9.5], speed=self._tcp_speed,
            #                              mvacc=self._tcp_acc, radius=0.0, wait=True)
            #if not self._check_code(code, 'set_position'):
            #    return
            code = self._arm.set_position(*[168.7, 175.6, 359.5, 43.9, 88.3, 83.3], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return
        else:
            #code = self._arm.set_servo_angle(angle=[45.8, -17.9, 33.5, 186.9, 41.8, -7.2], speed=self._angle_speed,
            #                                 mvacc=self._angle_acc, wait=True, radius=0.0)
            #if not self._check_code(code, 'set_servo_angle'):
            #    return
            code = self._arm.set_cgpio_digital(3, 1, delay_sec=0)
            if not self._check_code(code, 'set_cgpio_digital'):
                return
            code = self._arm.set_servo_angle(angle=[48.4, -13.8, 36.3, 193.6, 42.0, -9.2], speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=0.0)
            if not self._check_code(code, 'set_servo_angle'):
                return

        time.sleep(0.5)
    
    def motion_make_icecream(self):
        if self.order_msg['makeReq']['topping'] in ['1','2','3']:
            time.sleep(6)
        else:
            time.sleep(9)

        time.sleep(4)
        code = self._arm.set_position(z=-20, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                      wait=True)
        if not self._check_code(code, 'set_position'):
            return
        time.sleep(4)
        code = self._arm.set_position(z=-10, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                      wait=True)
        if not self._check_code(code, 'set_position'):
            return
        if not self._check_code(code, 'set_pause_time'):
            return
        code = self._arm.set_position(z=-50, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                      wait=True)
        if not self._check_code(code, 'set_position'):
            return
        time.sleep(1)
        code = self._arm.set_cgpio_digital(3, 0, delay_sec=0)
        if not self._check_code(code, 'set_cgpio_digital'):
            return

        time.sleep(0.5)

    def motion_serve(self):
        code = self._arm.set_servo_angle(angle=[18.2, -12.7, 8.3, 90.3, 88.1, 23.6], speed=self._angle_speed,
                                         mvacc=self._angle_acc, wait=False, radius=20.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        code = self._arm.set_servo_angle(angle=[146.9, -12.7, 8.3, 91.0, 89.3, 22.1], speed=self._angle_speed,
                                         mvacc=self._angle_acc, wait=True, radius=0.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        
        self._tcp_speed = 100
        self._tcp_acc = 1000
        
        if self.order_msg['makeReq']['jigNum'] == 'A':
            #code = self._arm.set_position(*[-251.2, -142.1, 213.7, -28.1, 88.8, -146.0], speed=self._tcp_speed,
            #                              mvacc=self._tcp_acc, radius=0.0, wait=True)
            #if not self._check_code(code, 'set_position'):
            #    return
            #code = self._arm.set_position(*[-250.3, -138.3, 213.7, 68.3, 86.1, -47.0], speed=self._tcp_speed,
            #                              mvacc=self._tcp_acc, radius=0.0, wait=True)
            #if not self._check_code(code, 'set_position'):
            #    return
            code = self._arm.set_position(*[-258.7, -136.4, 208.2, 43.4, 88.7, -72.2], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return
            
            code = self._arm.set_position(z=-18, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                          wait=True)
            if not self._check_code(code, 'set_position'):
                return
            code = self._arm.open_lite6_gripper()
            if not self._check_code(code, 'open_lite6_gripper'):
                return
            time.sleep(1)
            code = self._arm.set_position(*[-256.2, -126.6, 204.1, -179.2, 77.2, 66.9], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return
            code = self._arm.stop_lite6_gripper()
            if not self._check_code(code, 'stop_lite6_gripper'):
                return
            time.sleep(0.5)
            code = self._arm.set_position(*[-242.8, -96.3, 205.5, -179.2, 77.2, 66.9], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return
            #code = self._arm.set_tool_position(*[0.0, 0.0, -30, 0.0, 0.0, 0.0], speed=self._tcp_speed, mvacc=self._tcp_acc, wait=True)
            #if not self._check_code(code, 'set_position'):
            #    return
            code = self._arm.set_position(*[-189.7, -26.0, 193.3, -28.1, 88.8, -146.0], speed=self._tcp_speed,
                                          mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return

        elif self.order_msg['makeReq']['jigNum'] == 'B':
            code = self._arm.set_servo_angle(angle=[201.1, 24.4, 27.2, 109.5, 89.6, 2.1], speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=0.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_position(z=-15, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                          wait=True)
            if not self._check_code(code, 'set_position'):
                return
            code = self._arm.open_lite6_gripper()
            if not self._check_code(code, 'open_lite6_gripper'):
                return
            time.sleep(1)
            code = self._arm.set_position(*[-165.0, -122.7, 195.7, -178.7, 80.7, 92.5], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return
            code = self._arm.stop_lite6_gripper()
            if not self._check_code(code, 'stop_lite6_gripper'):
                return
            time.sleep(0.5)
            code = self._arm.set_position(*[-165.9, -81.9, 195.4, -178.7, 80.7, 92.5], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return
            #code = self._arm.set_tool_position(*[0.0, 0.0, -30, 0.0, 0.0, 0.0], speed=self._tcp_speed, mvacc=self._tcp_acc, wait=True)
            #if not self._check_code(code, 'set_position'):
            #    return
            code = self._arm.set_position(*[-168.5, -33.2, 192.8, -92.9, 86.8, -179.3], speed=self._tcp_speed,
                                          mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return
        elif self.order_msg['makeReq']['jigNum'] == 'C':
            code = self._arm.set_servo_angle(angle=[171.0, 13.7, 13.5, 73.9, 92.3, -2.9], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=0.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_position(*[-63.1, -138.2, 199.5, -45.5, 88.1, -112.1], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return
            code = self._arm.set_position(z=-12, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                          wait=True)
            if not self._check_code(code, 'set_position'):
                return
            code = self._arm.open_lite6_gripper()
            if not self._check_code(code, 'open_lite6_gripper'):
                return
            time.sleep(1)
            code = self._arm.set_position(*[-78.5, -132.8, 203.6, -176.8, 76.1, 123.0], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return
            code = self._arm.stop_lite6_gripper()
            if not self._check_code(code, 'stop_lite6_gripper'):
                return
            time.sleep(0.5)
            code = self._arm.set_position(*[-93.0, -107.5, 205.5, -176.8, 76.1, 123.0], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return
            #code = self._arm.set_tool_position(*[0.0, 0.0, -30, 0.0, 0.0, 0.0], speed=self._tcp_speed, mvacc=self._tcp_acc, wait=True)
            #if not self._check_code(code, 'set_position'):
            #    return
            code = self._arm.set_position(*[-98.1, -52.1, 191.4, -68.4, 86.4, -135.0], speed=self._tcp_speed,
                                          mvacc=self._tcp_acc, radius=0.0, wait=True)
            if not self._check_code(code, 'set_position'):
                return
            
        time.sleep(0.5)
        code = self._arm.set_servo_angle(angle=[169.6, -8.7, 13.8, 85.8, 93.7, 19.0], speed=self._angle_speed,
                                         mvacc=self._angle_acc, wait=True, radius=10.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        
        self._tcp_speed = 100
        self._tcp_acc = 1000
    
    def motion_trash_capsule(self):
        self._angle_speed = 150
        self._angle_acc = 300
        code = self._arm.set_servo_angle(angle=[51.2, -8.7, 13.8, 95.0, 86.0, 17.0], speed=self._angle_speed,
                                         mvacc=self._angle_acc, wait=False, radius=50.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        code = self._arm.set_servo_angle(angle=[-16.2, -19.3, 42.7, 82.0, 89.1, 55.0], speed=self._angle_speed,
                                         mvacc=self._angle_acc, wait=True, radius=0.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        code = self._arm.open_lite6_gripper()
        if not self._check_code(code, 'open_lite6_gripper'):
            return
        code = self._arm.set_servo_angle(angle=[-19.9, -19.1, 48.7, 87.2, 98.7, 60.0], speed=self._angle_speed,
                                         mvacc=self._angle_acc, wait=True, radius=0.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        code = self._arm.set_position(*[222.8, 0.9, 470.0, -153.7, 87.3, -68.7], speed=self._tcp_speed,
                                      mvacc=self._tcp_acc, radius=0.0, wait=True)
        if not self._check_code(code, 'set_position'):
            return
        code = self._arm.set_position(*[234.2, 129.8, 464.5, -153.7, 87.3, -68.7], speed=self._tcp_speed,
                                      mvacc=self._tcp_acc, radius=0.0, wait=True)
        if not self._check_code(code, 'set_position'):
            return
        code = self._arm.close_lite6_gripper()
        if not self._check_code(code, 'close_lite6_gripper'):
            return
        time.sleep(1)
        code = self._arm.set_position(z=30, radius=-1, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                      wait=True)
        if not self._check_code(code, 'set_position'):
            return
        self._tcp_speed = 100
        self._tcp_acc = 1000
        code = self._arm.set_position(*[221.9, -9.5, 500.4, -153.7, 87.3, -68.7], speed=self._tcp_speed,
                                      mvacc=self._tcp_acc, radius=0.0, wait=True)
        if not self._check_code(code, 'set_position'):
            return
        self._angle_speed = 60
        self._angle_acc = 100
        code = self._arm.set_servo_angle(angle=[-10.7, -2.4, 53.5, 50.4, 78.1, 63.0], speed=self._angle_speed,
                                         mvacc=self._angle_acc, wait=False, radius=10.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        # code = self._arm.set_position(*[217.1, 125.8, 250.1, 170.8, 50.2, -99.2], speed=self._tcp_speed,
        #                              mvacc=self._tcp_acc, radius=0.0, wait=True)
        # if not self._check_code(code, 'set_position'):
        #    return
        self._angle_speed = 160
        self._angle_acc = 1000
        code = self._arm.set_servo_angle(angle=[18.0, 11.2, 40.4, 90.4, 58.7, -148.8], speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=0.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        code = self._arm.open_lite6_gripper()
        if not self._check_code(code, 'open_lite6_gripper'):
            return
        #time.sleep(2)
        code = self._arm.set_servo_angle(angle=[25.2, 15.2, 42.7, 83.2, 35.0, -139.8], speed=self._angle_speed, mvacc=self._angle_acc, wait=False, radius=0.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        code = self._arm.set_servo_angle(angle=[18.0, 11.2, 40.4, 90.4, 58.7, -148.8], speed=self._angle_speed, mvacc=self._angle_acc, wait=False, radius=0.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        code = self._arm.set_servo_angle(angle=[25.2, 15.2, 42.7, 83.2, 35.0, -139.8], speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=0.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        code = self._arm.stop_lite6_gripper()
        if not self._check_code(code, 'stop_lite6_gripper'):
            return
        self._angle_speed = 120
        self._angle_acc = 1000
        code = self._arm.set_servo_angle(angle=[28.3, -9.0, 12.6, 85.9, 78.5, 20.0], speed=self._angle_speed,
                                         mvacc=self._angle_acc, wait=False, radius=30.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        #code = self._arm.set_servo_angle(angle=[116.8, -9.0, 10.0, 107.1, 78.3, 20.0], speed=self._angle_speed,
        #                                mvacc=self._angle_acc, wait=False, radius=30.0)
        #if not self._check_code(code, 'set_servo_angle'):
        #    return
        code = self._arm.set_servo_angle(angle=[149.3, -9.4, 10.9, 114.7, 69.1, 26.1], speed=self._angle_speed, mvacc=self._angle_acc, wait=False, radius=50.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        #code = self._arm.set_servo_angle(angle=[179.0, -17.9, 17.7, 176.4, 61.3, 0.0], speed=self._angle_speed,
        #                                 mvacc=self._angle_acc, wait=True, radius=0.0)
        #if not self._check_code(code, 'set_servo_angle'):
        #    return
        code = self._arm.set_servo_angle(angle=[179.2, -42.1, 7.4, 186.7, 41.5, -1.6], speed=self._angle_speed,
                                         mvacc=self._angle_acc, wait=True, radius=0.0)
        if not self._check_code(code, 'set_servo_angle'):
            return
        time.sleep(0.5)




    # Robot Main Run
    def run(self):
        try:
            self.motion_home()
            self.order_msg = {'makeReq': {'jigNum': 'A'}}
            self.motion_grab_capsule()
            self.motion_place_capsule()
            self.order_msg['makeReq']['cupNum'] = 'B'
            self.motion_grab_cup()
            self.order_msg['makeReq']['topping'] = '1'
            self.motion_topping()
            self.motion_make_icecream()
            self.motion_serve()
            self.motion_trash_capsule()
            self.motion_home()
            print('icecream finish')


        except Exception as e:
            self.pprint('MainException: {}'.format(e))
        self.alive = False
        self._arm.release_error_warn_changed_callback(self._error_warn_changed_callback)
        self._arm.release_state_changed_callback(self._state_changed_callback)
        if hasattr(self._arm, 'release_count_changed_callback'):
            self._arm.release_count_changed_callback(self._count_changed_callback)


class RobotActionServer(Node):
    def __init__(self):
        super().__init__('robot_control_action_server')
        self.action_server = ActionServer(self, RobotOrder, 'robot_order', self.execute_callback)

        RobotMain.pprint('xArm-Python-SDK Version:{}'.format(version.__version__))
        self.arm = XArmAPI('192.168.1.192', baud_checkset=False)
        self.robot_main = RobotMain(self.arm)

        self.robot_main.order_msg = {}
        self.robot_main.order_msg = {'makeReq': {'jigNum': 'A'}}
        self.robot_main.order_msg['makeReq']['cupNum'] = 'B'
        self.robot_main.order_msg['makeReq']['topping'] = '1'

    def execute_callback(self, goal_handle):
        feedback_msg = RobotOrder.Feedback()
        feedback_msg.message = 'start making icecream'
        goal_handle.publish_feedback(feedback_msg)

        order = goal_handle.request.order
        if order == 'icecreaming':
            print('making icecream')
            # --------------icecream start--------------------
            
            self.robot_main.motion_home()

            feedback_msg.message = 'grab capsule'
            goal_handle.publish_feedback(feedback_msg)

            self.robot_main.motion_grab_capsule()

            feedback_msg.message = 'place capsule'
            goal_handle.publish_feedback(feedback_msg)

            self.robot_main.motion_place_capsule()

            feedback_msg.message = 'grab cup'
            goal_handle.publish_feedback(feedback_msg)

            self.robot_main.motion_grab_cup()

            feedback_msg.message = 'put topping'
            goal_handle.publish_feedback(feedback_msg)

            self.robot_main.motion_topping()

            feedback_msg.message = 'make icecream'
            goal_handle.publish_feedback(feedback_msg)

            self.robot_main.motion_make_icecream()

            feedback_msg.message = 'serving'
            goal_handle.publish_feedback(feedback_msg)

            self.robot_main.motion_serve()

            feedback_msg.message = 'trash capsule'
            goal_handle.publish_feedback(feedback_msg)

            self.robot_main.motion_trash_capsule()

            feedback_msg.message = 'back home'
            goal_handle.publish_feedback(feedback_msg)

            self.robot_main.motion_home()
            print('icecream finish')


        goal_handle.succeed()
        result = RobotOrder.Result()
        result.result = 'successfully finished'
        print('successfully made icecream')
        return result


def main(args=None):
    rp.init(args=args)

    robot_action_server = RobotActionServer()
    rp.spin(robot_action_server)

    robot_action_server.destroy_node()
    rp.shutdown()


if __name__ == '__main__':
    main()
