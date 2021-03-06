"""
    uCentral gateway API

    A process to manage configuration for devices.  # noqa: E501

    The version of the OpenAPI document: 0.0.8
    Contact: ucentralsupport@arilia.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.commands_api import CommandsApi  # noqa: E501


class TestCommandsApi(unittest.TestCase):
    """CommandsApi unit test stubs"""

    def setUp(self):
        self.api = CommandsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_a_command(self):
        """Test case for delete_a_command

        Delete a specific command  # noqa: E501
        """
        pass

    def test_delete_commands(self):
        """Test case for delete_commands

        Delete some commands  # noqa: E501
        """
        pass

    def test_delete_device_capabilities(self):
        """Test case for delete_device_capabilities

        Delete the capabilities for a given device  # noqa: E501
        """
        pass

    def test_delete_device_health_checks(self):
        """Test case for delete_device_health_checks

        Delete some device health checks  # noqa: E501
        """
        pass

    def test_delete_device_logs(self):
        """Test case for delete_device_logs

        Delete some device logs  # noqa: E501
        """
        pass

    def test_delete_device_stats(self):
        """Test case for delete_device_stats

        Get the latest statistics for a given device  # noqa: E501
        """
        pass

    def test_event_queue_request(self):
        """Test case for event_queue_request

        Request a list of queued events  # noqa: E501
        """
        pass

    def test_execute_command(self):
        """Test case for execute_command

        Post a command to a device  # noqa: E501
        """
        pass

    def test_factory_reset(self):
        """Test case for factory_reset

        Factory reset a device a device  # noqa: E501
        """
        pass

    def test_get_a_command_details(self):
        """Test case for get_a_command_details

        Returns a specific command  # noqa: E501
        """
        pass

    def test_get_command_list(self):
        """Test case for get_command_list

        Returns a list of commands.  # noqa: E501
        """
        pass

    def test_get_device_capabilities(self):
        """Test case for get_device_capabilities

        Get the latest capabilities for a given device  # noqa: E501
        """
        pass

    def test_get_device_health_checks(self):
        """Test case for get_device_health_checks

        Get the latest health checks for a given device  # noqa: E501
        """
        pass

    def test_get_device_logs(self):
        """Test case for get_device_logs

        Get the latest logs for a given device  # noqa: E501
        """
        pass

    def test_get_device_stats(self):
        """Test case for get_device_stats

        Get the latest statistics for a given device  # noqa: E501
        """
        pass

    def test_get_device_status(self):
        """Test case for get_device_status

        Get the latest status for a given device  # noqa: E501
        """
        pass

    def test_get_rtty_session_info(self):
        """Test case for get_rtty_session_info

        Get the rtty parameters to initiate a session  # noqa: E501
        """
        pass

    def test_leds_request(self):
        """Test case for leds_request

        Blink the LEDs on a device  # noqa: E501
        """
        pass

    def test_message_request(self):
        """Test case for message_request

        Request a specific message  # noqa: E501
        """
        pass

    def test_reboot_device(self):
        """Test case for reboot_device

        Upgrade a device  # noqa: E501
        """
        pass

    def test_trace_request(self):
        """Test case for trace_request

        Launch a trace for a device  # noqa: E501
        """
        pass

    def test_update_configuration_for_a_device(self):
        """Test case for update_configuration_for_a_device

        Configura a device  # noqa: E501
        """
        pass

    def test_upgrade_device_firmware(self):
        """Test case for upgrade_device_firmware

        Upgrade a device  # noqa: E501
        """
        pass

    def test_wifiscan_request(self):
        """Test case for wifiscan_request

        Launch a wifi scan for a device  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
