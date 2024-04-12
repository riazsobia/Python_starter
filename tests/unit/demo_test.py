"""
'demo_test.py'

The following tests, check if operation works properly or not.

Copyright (c) 2016-2023 EncoreSky Ltd. All rights reserved.
"""

import unittest
from flask_boilerplate.core.operations.addition import addition


class TestDemo(unittest.TestCase):

    def test_01_addition_operation(self):
        sum = addition(value_1=10, value_2=10)
        self.assertEqual(20, sum)
        