from apriltag_trim.tag_trim_ros1.ImageConverter import ImageConverter

import message_filters
from message_filters import ApproximateTimeSynchronizer


from sensor_msgs.msg import Image, CameraInfo
from apriltag_msgs.msg import AprilTagDetectionArray

class ImageConverter_ros2(ImageConverter):
    def __init__(self,node):

        node.subscription = node.create_subscription(
            AprilTagDetectionArray,
            '/apriltag/detections',
            self.listener_callback,
            10)
        node.subscription  # prevent unused variable warning

        sub1 = message_filters.Subscriber(node, Image,"image_topic")
        sub2 = message_filters.Subscriber(node, CameraInfo,"camera_info_topic")
        ts = ApproximateTimeSynchronizer([sub1, sub2], 10, 0.1)
        ts.registerCallback(self.imageConvCallback)

    def cb_collector_2msg(self, msg1, msg2):
        self.collector.append((msg1, msg2))
    def listener_callback(self,msg):
        print("heard")
    def imageConvCallback(self,img,info):
        print("conv")
