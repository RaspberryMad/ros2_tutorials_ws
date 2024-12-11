import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np

class DepthMeasurement(Node):
    def __init__(self):
        super().__init__('depth_measurement')
        self.subscription = self.create_subscription(
            Image,
            '/camera/depth/image_raw',  # Asegúrate de usar el tema correcto
            self.depth_callback,
            10)
        self.bridge = CvBridge()
        self.get_logger().info("Depth measurement node started. Waiting for depth images...")

    def depth_callback(self, msg):
        self.get_logger().info('Received a depth image!')
        # Convertir el mensaje de ROS a una imagen de OpenCV
        depth_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        # Obtener la distancia al punto central
        height, width = depth_image.shape
        center_distance_mm = depth_image[height // 2, width // 2]
        center_distance_m = center_distance_mm / 1000.0  # Convertir de milímetros a metros
        self.get_logger().info(f'Distance to center: {center_distance_m:.2f} meters')


def main(args=None):
    rclpy.init(args=args)
    node = DepthMeasurement()
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
