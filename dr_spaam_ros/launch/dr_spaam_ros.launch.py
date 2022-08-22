import imp
import os
from ament_index_python.packages import get_package_share_directory
import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os
import yaml

def generate_launch_description():
    pkg_share=launch_ros.substitutions.FindPackageShare(package='dr_spaam_ros').find('dr_spaam_ros')
    spaam_config =os.path.join(pkg_share, 'config/dr_spaam_ros.yaml')
    rviz_path =os.path.join(pkg_share, 'config/example.rviz')

    with open(spaam_config, 'r') as f:
        params = yaml.safe_load(f)['dr_spaam_ros']['ros__parameters']

    spaam_node = launch_ros.actions.Node(
        package='dr_spaam_ros',
        executable='dr_spaam_ros',
        output='screen',
        parameters=[params],
    )
    # joint_state_publisher_node = launch_ros.actions.Node(
    #     package='joint_state_publisher',
    #     executable='joint_state_publisher',
    #     name='joint_state_publisher',
    #     output='screen',
    #     condition=launch.conditions.UnlessCondition(LaunchConfiguration('gui'))
    # )
    # joint_state_publisher_gui_node = launch_ros.actions.Node(
    #     package='joint_state_publisher_gui',
    #     executable='joint_state_publisher_gui',
    #     name='joint_state_publisher_gui',
    #     output='screen',
    #     condition=launch.conditions.IfCondition(LaunchConfiguration('gui'))
    # )
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_path]
    )
 
    return launch.LaunchDescription([
        spaam_node,
        rviz_node
    ])

