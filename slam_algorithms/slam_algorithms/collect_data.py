import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry

class DataCollectorNode(Node):
    """
    Collects odom and lidar data as the robot moves and writes it to a file.
    Using this to test out initial working of algorithms without having to worry about real-time processing
    """
    def __init__(self):
        
        super().__init__('data_collector')
        
        self.get_logger().info('Data collector node initialized')
        
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

        self._latest_laser_scan = None
        self._latest_odom = None
    
        self.odom_data = open('/home/ws/log/state.txt', 'w')
        self.laser_data = open('/home/ws/log/lidar.txt', 'w')    
    
    def laser_scan_callback(self, msg):

        timestamp = msg.header.stamp.sec + msg.header.stamp.nanosec / 1e9
        ranges = msg.ranges
        self.laser_data.write(f"{timestamp} {ranges}\n")
        self._latest_laser_scan = msg
        
    def odom_callback(self, msg):

        timestamp = msg.header.stamp.sec + msg.header.stamp.nanosec / 1e9
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        theta = msg.pose.pose.orientation.z
        self.odom_data.write(f"{timestamp} {x} {y} {theta}\n")
        self._latest_odom = msg

    @property
    def latest_laser_scan(self):
        return self._latest_laser_scan

    @property
    def latest_odom(self):
        return self._latest_odom

    def process_data(self):

        self.get_logger().info(f"Latest laser scan: {self.latest_odom}")

def main(args=None):

    rclpy.init(args=args)

    subscriber = DataCollectorNode()

    while rclpy.ok():
        rclpy.spin_once(subscriber)
        subscriber.process_data()

    subscriber.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()