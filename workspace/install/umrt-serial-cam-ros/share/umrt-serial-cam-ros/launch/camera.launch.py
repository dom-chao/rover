"""
UMRT Camera Launch File
"""

# Imports 
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction, LogInfo
from launch.substitutions import LaunchConfiguration
import os


"""
Launch File for Camera and Encoders 
"""
def generate_launch_description():

    """
    Parameters
    """
    # We can declare some arguments that can be passed on but it's not used here
    
    rover0_arg = DeclareLaunchArgument('rover0', default_value=os.getenv('ROVERCAM0') or "/dev/null", description='Device path for rover camera 0')
    rover1_arg = DeclareLaunchArgument('rover1', default_value=os.getenv('ROVERCAM1') or "/dev/null", description='Device path for rover camera 1')
    arm0_arg = DeclareLaunchArgument('arm0', default_value=os.getenv('ARMCAM0') or "/dev/null", description='Device path for arm camera 0')
    arm1_arg = DeclareLaunchArgument('arm1', default_value=os.getenv('ARMCAM1') or "/dev/null", description='Device path for arm camera 1')


    arm0 = LaunchConfiguration('arm0')
    arm1 = LaunchConfiguration('arm1')
    rover0 = LaunchConfiguration('rover0')
    rover1 = LaunchConfiguration('rover1')

    # Config for all camera parameters
    config_path = os.path.join(
        get_package_share_directory('umrt-serial-cam-ros'),
        'config',
        'cam_params.yaml'
        )

    """
    Nodes
    """
    # Camera 1 - Arm Camera 0
    arm1_node = Node(
        package='usb_cam',
        executable='usb_cam_node_exe',
        output='screen',
        name='arm_cam0',
        namespace='arm0',
        parameters=[config_path, {'video_device': arm0}]
    )

    # Camera 2 - Arm Camera 1
    arm2_node = Node(
        package='usb_cam',
        executable='usb_cam_node_exe',
        output='screen',
        name='arm_cam1',
        namespace='arm1',
        parameters=[config_path, {'video_device': arm1}]
    )

    # Camera 3 - Rover Camera 0
    rover0_node = Node(
        package='usb_cam',
        executable='usb_cam_node_exe',
        output='screen',
        name='rover_cam0',
        namespace='rover0',
        parameters=[config_path, {'video_device': rover0}]
    )

    # Camera 4 - Rover Camera 1
    rover1_node = Node(
        package='usb_cam',
        executable='usb_cam_node_exe',
        output='screen',
        name='rover_cam1',
        namespace='rover1',
        parameters=[config_path, {'video_device': rover1}]
    )

    cam_rover_delayed = TimerAction(
        period=3.0,
        actions=[
            LogInfo(msg='Waiting 3s before starting rover1 node...'),
            rover1_node
        ]
    )

    """
    Launch
    """
    cameras = [
        arm0_arg,
        arm1_arg,
        arm1_node,
        arm2_node,
        rover0_arg,
        rover1_arg,
        rover0_node,
        cam_rover_delayed
    ]

    return LaunchDescription(cameras)