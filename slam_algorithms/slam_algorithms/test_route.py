import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TestRouteNode(Node):
    """
    Publishes to /cmd_vel to make the robot move in an L shape
    To be used with the 'collect_data.py' script so we can collect data for testing
    """
    def __init__(self):
        super().__init__('test_route')
        self.get_logger().info('Test route node initialized')

        self.cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)

    def publish_cmd_vel(self):
        cmd_vel = Twist()
        cmd_vel.linear.y = -1
        self.cmd_vel_publisher.publish(cmd_vel)


def main(args=None):
    
    rclpy.init(args=args)
    test_route_node = TestRouteNode()
    
    while rclpy.ok():
        test_route_node.publish_cmd_vel()
        rclpy.spin_once(test_route_node)
    
    test_route_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()