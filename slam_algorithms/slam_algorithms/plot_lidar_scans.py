import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import matplotlib.pyplot as plt

class LaserscanNode(Node):

    def __init__(self):
        
        super().__init__('laser_scan_plotter')
        
        self.get_logger().info('Laser scan plotter node initialized')
        
        self.laser_scan_subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.laser_scan_callback,
            10
        )
    
    def laser_scan_callback(self, msg):

        self.get_logger().info(f'Received scan data')
        
        self.get_logger().info(f'{len(msg.ranges)} ranges')
        
        return msg  

def main(args=None):

    rclpy.init(args=args)

    subscriber = LaserscanNode()

    rclpy.spin(subscriber)

    subscriber.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()