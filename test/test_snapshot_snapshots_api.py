# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 8
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_2_1
from isi_sdk_8_2_1.api.snapshot_snapshots_api import SnapshotSnapshotsApi  # noqa: E501
from isi_sdk_8_2_1.rest import ApiException


class TestSnapshotSnapshotsApi(unittest.TestCase):
    """SnapshotSnapshotsApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_2_1.api.snapshot_snapshots_api.SnapshotSnapshotsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_snapshot_lock(self):
        """Test case for create_snapshot_lock

        """
        pass

    def test_delete_snapshot_lock(self):
        """Test case for delete_snapshot_lock

        """
        pass

    def test_delete_snapshot_locks(self):
        """Test case for delete_snapshot_locks

        """
        pass

    def test_get_snapshot_lock(self):
        """Test case for get_snapshot_lock

        """
        pass

    def test_list_snapshot_locks(self):
        """Test case for list_snapshot_locks

        """
        pass

    def test_update_snapshot_lock(self):
        """Test case for update_snapshot_lock

        """
        pass


if __name__ == '__main__':
    unittest.main()
