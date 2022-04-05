# Copyright (c) 2020 Norwegian University of Science and Technology
# Copyright (c) 2019, Zivid AS
# Use of this source code is governed by the BSD 3-Clause license, see LICENSE

from zivid_interfaces.srv import Capture2D

import rclpy


def main(args=None):

    rclpy.init(args=args)

    node = rclpy.create_node("zivid_camera_client")

    capture_client = node.create_client(Capture2D, "/zivid/capture_2d")
    while not capture_client.wait_for_service(timeout_sec=1.0):
        print("service not available, waiting again...")

    request = Capture2D.Request()

    future = capture_client.call_async(request)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
