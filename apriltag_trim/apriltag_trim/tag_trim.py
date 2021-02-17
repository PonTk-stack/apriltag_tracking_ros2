import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from apriltag_msgs.msg import AprilTagDetectionArray

from apriltag_trim.ImageConverter_ros2 import *

class TagTrim(Node):

    def __init__(self):
        super().__init__('tag_trim')
        print('.***************Hi from apriltag_trim.***************',flush=True)
        """
        self.subscription = self.create_subscription(
            AprilTagDetectionArray,
            '/apriltag/detections',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        """

        icr = ImageConverter_ros2(self)
        print("aa",flush=True)
    def listener_callback(self, msg):
        print("heard")
        #self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):

    rclpy.init(args=args)

    node = TagTrim()

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':

    main()
