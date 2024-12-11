cmake_minimum_required(VERSION 3.8)
project(my_astra_camera)

# Encuentra las dependencias necesarias
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(OpenCV REQUIRED)

# Instalación de los scripts Python
install(
  PROGRAMS
    CameraCapture.py
    DepthMeasurement.py
  DESTINATION lib/${PROJECT_NAME}
)

# Exporta dependencias
ament_export_dependencies(rclpy sensor_msgs cv_bridge OpenCV)

# Finaliza la configuración del paquete
ament_package()
