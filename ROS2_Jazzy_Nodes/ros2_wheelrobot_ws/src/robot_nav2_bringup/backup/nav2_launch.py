from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            name='map',
            default_value='/home/fk/ros2_wheelrobot_ws/src/robot_nav2_bringup/map/my_map.yaml',
            description='Full path to map YAML file'
        ),
        DeclareLaunchArgument(
            name='params_file',
            default_value='/home/fk/ros2_wheelrobot_ws/src/robot_nav2_bringup/config/robot_nav2_params.yaml',
            description='Full path to the nav2 parameters file'
        ),
        DeclareLaunchArgument(
            name='use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'
        ),

        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=[LaunchConfiguration('params_file'), {'yaml_filename': LaunchConfiguration('map')}]
        ),

        Node(
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            output='screen',
            parameters=[LaunchConfiguration('params_file')]
        ),

        Node(
            package='nav2_bt_navigator',
            executable='bt_navigator',
            name='bt_navigator',
            output='screen',
            parameters=[LaunchConfiguration('params_file')]
        ),

        Node(
            package='nav2_controller',
            executable='controller_server',
            name='controller_server',
            output='screen',
            parameters=[LaunchConfiguration('params_file')]
        ),

        Node(
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            parameters=[LaunchConfiguration('params_file')]
        ),

        Node(
            package='nav2_behaviors',
            executable='behavior_server',
            name='behavior_server',
            output='screen',
            parameters=[LaunchConfiguration('params_file')]
        ),

        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_navigation',
            output='screen',
            parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time'),
                         'autostart': True,
                         'node_names': [
                             'map_server',
                             'amcl',
                             'planner_server',
                             'controller_server',
                             'bt_navigator',
                             'behavior_server'
                         ]}]
        ),
    ])
