import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageResizer(Node):
    def __init__(self):
        super().__init__('image_resizer')
        self.subscription = self.create_subscription(
            Image, 'input_image_topic', self.image_callback, 10)
        self.publisher_ = self.create_publisher(
            Image, 'output_image_topic', 10)
        self.cv_bridge = CvBridge()

    def image_callback(self, msg):
        try: # converting to cv2 image
            cv_image = self.cv_bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            self.get_logger().error('Error converting image: %s' % str(e))
            return

        resized_image = cv2.resize(cv_image, (300, 300))

        try:
            resized_msg = self.cv_bridge.cv2_to_imgmsg(resized_image, "bgr8")
            self.publisher_.publish(resized_msg)
        except Exception as e:
            self.get_logger().error('Error publishing resized image: %s' % str(e))

def main(args=None):
    rclpy.init(args=args)
    node = ImageResizer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

