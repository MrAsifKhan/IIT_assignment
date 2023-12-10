import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='image_processing_pkg',
            executable='node1',
            name='image_resizer',
            output='screen'
        ),
        Node(
            package='image_processing_pkg',
            executable='node2',
            name='image_processor',
            output='screen'
        ),
    ])
