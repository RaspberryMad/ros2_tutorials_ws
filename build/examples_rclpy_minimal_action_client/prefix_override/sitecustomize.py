import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sener/ros2_tutorials_ws/install/examples_rclpy_minimal_action_client'
