# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import table_widget_definition_type
except ImportError:
    table_widget_definition_type = sys.modules[
        'datadog_api_client.v1.model.table_widget_definition_type']
try:
    from datadog_api_client.v1.model import table_widget_request
except ImportError:
    table_widget_request = sys.modules[
        'datadog_api_client.v1.model.table_widget_request']
try:
    from datadog_api_client.v1.model import widget_text_align
except ImportError:
    widget_text_align = sys.modules[
        'datadog_api_client.v1.model.widget_text_align']
try:
    from datadog_api_client.v1.model import widget_time
except ImportError:
    widget_time = sys.modules[
        'datadog_api_client.v1.model.widget_time']
from datadog_api_client.v1.model.table_widget_definition import TableWidgetDefinition


class TestTableWidgetDefinition(unittest.TestCase):
    """TableWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTableWidgetDefinition(self):
        """Test TableWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TableWidgetDefinition()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
