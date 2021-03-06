"""
    uCentral gateway API

    A process to manage configuration for devices.  # noqa: E501

    The version of the OpenAPI document: 0.0.8
    Contact: ucentralsupport@arilia.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.blacklist_api import BlacklistApi  # noqa: E501


class TestBlacklistApi(unittest.TestCase):
    """BlacklistApi unit test stubs"""

    def setUp(self):
        self.api = BlacklistApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_to_black_list(self):
        """Test case for add_to_black_list

        Adds to the blacklist  # noqa: E501
        """
        pass

    def test_delete_from_black_list(self):
        """Test case for delete_from_black_list

        Delete from the blacklist  # noqa: E501
        """
        pass

    def test_get_blacklist_device_list(self):
        """Test case for get_blacklist_device_list

        Returns a list blacklisted devices.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
