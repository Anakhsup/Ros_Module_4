import math

from geometry_msgs.msg import TransformStamped

import rclpy
from rclpy.node import Node

from tf2_ros import TransformBroadcaster


class DynamicFrameBroadcaster(Node):

    def __init__(self):
        super().__init__('tf2_broadcaster')
        self.tf_broadcaster = TransformBroadcaster(self)
        self.declare_parameter('radius', 2)
        self.declare_parameter('direction_of_rotation', 1)
        self.timer = self.create_timer(0.1, self.broadcast_timer_callback)


    def broadcast_timer_callback(self):
    
        seconds, n = self.get_clock().now().seconds_nanoseconds()
        r = self.get_parameter('radius').get_parameter_value().integer_value
        direction_of_r = self.get_parameter('direction_of_rotation').get_parameter_value().integer_value
        x = seconds * direction_of_r
        
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'turtle1'
        t.child_frame_id = 'carrot1'
        t.transform.translation.x = r*math.sin(x)
        t.transform.translation.y = r*math.cos(x)
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        self.tf_broadcaster.sendTransform(t)
        


def main():
    rclpy.init()
    node = DynamicFrameBroadcaster()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
