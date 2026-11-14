"""
UMRT Base Station Launch File
"""

"""
Imports
"""
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy 
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

"""
Generate Launch Description
"""
def generate_launch_description():

    """
    Parameters
    """
    # Path to this package's launch dir
    launch_dir = os.path.join(
        get_package_share_directory('umrt-serial-cam-ros'), 'launch')
    
    """
    External Launch Files
    """
    # Decode Rover Camera 0
    """rover_decoder = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_dir, 'decode.launch.py')
        ), 
        launch_arguments={
            'namespace': 'rover',
            'in_ffmpeg': '/rover/ffmpeg',
            'out_raw': '/rover/decoded'
        }.items()
    )"""

    # Decode Arm Camera 0
    arm0_decoder = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_dir, 'decode.launch.py')
        ), 
        launch_arguments={
            'namespace': 'arm0',
            'in_ffmpeg': '/arm0/image_raw/ffmpeg',
            'out_raw': '/arm0/decoded'
        }.items()
    )

    # Decode Arm Camera 1
    arm1_decoder = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_dir, 'decode.launch.py')
        ), 
        launch_arguments={
            'namespace': 'arm1',
            'in_ffmpeg': '/arm1/image_raw/ffmpeg',
            'out_raw': '/arm1/decoded'
        }.items()
    ) 

    # Decode Rover Camera 0
    rover0_decoder = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_dir, 'decode.launch.py')
        ), 
        launch_arguments={
            'namespace': 'rover0',
            'in_ffmpeg': '/rover0/image_raw/ffmpeg',
            'out_raw': '/rover0/decoded'
        }.items()
    )

    # Decode Rover Camera 1
    rover1_decoder = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_dir, 'decode.launch.py')
        ), 
        launch_arguments={
            'namespace': 'rover1',
            'in_ffmpeg': '/rover1/image_raw/ffmpeg',
            'out_raw': '/rover1/decoded'
        }.items()
    )

    """
    Launch
    """
    decoders = [
        #rover_decoder,
        arm0_decoder,
        arm1_decoder,
        rover0_decoder,
        rover1_decoder
    ]


    return LaunchDescription(decoders)  
