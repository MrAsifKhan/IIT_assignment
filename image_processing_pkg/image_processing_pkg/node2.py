import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageProcessor(Node):
    def __init__(self):
        super().__init__('image_processor')
        self.subscription = self.create_subscription(
            Image, 'output_image_topic', self.image_callback, 10)
        self.publisher_ = self.create_publisher(
            Image, 'processed_image_topic', 10)
        self.cv_bridge = CvBridge()

    def image_callback(self, msg):
        try:
            cv_image = self.cv_bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            self.get_logger().error('Error converting image: %s' % str(e))
            return

        # converting to grayscale image
        processed_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

        try:
            processed_msg = self.cv_bridge.cv2_to_imgmsg(processed_image, "mono8")
            self.publisher_.publish(processed_msg)
        except Exception as e:
            self.get_logger().error('Error publishing processed image: %s' % str(e))

def main(args=None):
    rclpy.init(args=args)
    node = ImageProcessor()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

