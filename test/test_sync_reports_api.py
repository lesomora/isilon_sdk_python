# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 3
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_0
from isi_sdk_8_0.api.sync_reports_api import SyncReportsApi  # noqa: E501
from isi_sdk_8_0.rest import ApiException


class TestSyncReportsApi(unittest.TestCase):
    """SyncReportsApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_0.api.sync_reports_api.SyncReportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_report_subreport(self):
        """Test case for get_report_subreport

        """
        pass

    def test_get_report_subreports(self):
        """Test case for get_report_subreports

        """
        pass


if __name__ == '__main__':
    unittest.main()