#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_utils.py
#
#  Copyright 2022 Marco Ramos <majramos@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


import unittest
from datetime import datetime

from holidays.utils import easter, flatten


class TestUtils(unittest.TestCase):

    def test_easter(self):
        self.assertEqual(easter(2020), datetime(2020, 4, 12, 0, 0))

    def test_flatten(self):
        self.assertEqual(flatten([['a', 'b'], ['c', 'd']]), ['a', 'b', 'c', 'd'])


if __name__ == '__main__':
    unittest.main()
