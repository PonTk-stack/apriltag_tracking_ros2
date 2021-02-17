import  launch
from launch import LaunchDescription
from launch_ros.actions import Node, ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


# detect all 16h5 tags
cfg_16h5 = {
    "image_transport": "raw",
    "family": "16h5",
    "size": 0.162,
    "max_hamming": 0,
    "z_up": True
}


'''
remappings=[
    ('image_topic', '/usb_cam/image_raw'),
    ('camera_info_topic', '/camera_info')]
'''
def generate_launch_description():
    tag_trim = Node(
        package='apriltag_trim',
        executable='tag_trim',
        #name='tag_trim',
        output='screen'
        )

    '''
    composable_node = ComposableNode(
        name='apriltag',
        package='apriltag_ros', plugin='AprilTagNode',
        remappings=[("/apriltag/image", "/usb_cam/image_raw"), ("/apriltag/camera_info", "/usb_cam/camera_info")],
        parameters=[cfg_16h5])
    container = ComposableNodeContainer(
        name='tag_container',
        namespace='apriltag',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[composable_node],
#        output='screen'
    )
    '''

    return LaunchDescription([
        tag_trim,
        #container,

                launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=tag_trim,
                on_exit=[launch.actions.EmitEvent(
                    event=launch.events.Shutdown())],
            )),
    ])
