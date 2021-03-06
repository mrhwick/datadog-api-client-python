# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import slo_history_metrics
except ImportError:
    slo_history_metrics = sys.modules[
        'datadog_api_client.v1.model.slo_history_metrics']
try:
    from datadog_api_client.v1.model import slo_history_sli_data
except ImportError:
    slo_history_sli_data = sys.modules[
        'datadog_api_client.v1.model.slo_history_sli_data']
try:
    from datadog_api_client.v1.model import slo_threshold
except ImportError:
    slo_threshold = sys.modules[
        'datadog_api_client.v1.model.slo_threshold']
try:
    from datadog_api_client.v1.model import slo_type
except ImportError:
    slo_type = sys.modules[
        'datadog_api_client.v1.model.slo_type']
try:
    from datadog_api_client.v1.model import slo_type_numeric
except ImportError:
    slo_type_numeric = sys.modules[
        'datadog_api_client.v1.model.slo_type_numeric']
from datadog_api_client.v1.model.slo_history_response_data import SLOHistoryResponseData


class TestSLOHistoryResponseData(unittest.TestCase):
    """SLOHistoryResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOHistoryResponseData(self):
        """Test SLOHistoryResponseData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOHistoryResponseData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
