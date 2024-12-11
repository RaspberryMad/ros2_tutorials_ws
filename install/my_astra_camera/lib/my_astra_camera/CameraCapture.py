import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraCapture(Node):
    def __init__(self):
        super().__init__('camera_capture')
        self.subscription = self.create_subscription(
            Image,
            '/camera/color/image_raw',  # Asegúrate de usar el tema correcto
            self.image_callback,
            10)
        self.bridge = CvBridge()
        self.get_logger().info("Camera node started. Waiting for images...")

    def image_callback(self, msg):
        self.get_logger().info('Received an image!')
        # Convertir el mensaje de ROS a una imagen de OpenCV
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        # Guardar la imagen en un archivo
        cv2.imwrite('captured_image.jpg', cv_image)
        self.get_logger().info('Image saved as captured_image.jpg')


def main(args=None):
    rclpy.init(args=args)
    node = CameraCapture()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Node stopped cleanly.')
    except Exception as e:
        node.get_logger().error(f'Error: {e}')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
