import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import matplotlib.pyplot as plt

class DataVisualizerNode(Node):
    """
    Plots the lidar data as the robot moves. 
    """
    def __init__(self):
        
        super().__init__('data_visualizer')
        
        self.get_logger().info('Laser scan plotter node initialized')
        
        self.laser_scan_subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.laser_scan_callback,
            10
        )

        self.odom_subscription = self.create_subscription(
            Odometry,
            'odom',
            self.odom_callback,
            10
        )
    
    def laser_scan_callback(self, msg):

        self.get_logger().info(f'Received scan data')
        
        self.get_logger().info(f'{len(msg.ranges)} ranges')
        
        return msg

    def odom_callback(self, msg):

        self.get_logger().info(f'Received odom data')
        
        return msg

def main(args=None):

    rclpy.init(args=args)

    subscriber = DataVisualizerNode()

    rclpy.spin(subscriber)

    subscriber.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()