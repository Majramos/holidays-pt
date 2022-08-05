#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_regions.py
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

from holidays.regions import _check_exists, ls_districts, select



class TestRegions(unittest.TestCase):

    def test_check_exists_pass(self):
        self.assertIsNone(_check_exists(ls_districts, ['aveiro']))

    def test_check_exists_fail(self):
        self.assertRaises(Exception, lambda: _check_exists(ls_districts, ['fail']))

    def test_select(self):
        to_check = {
            'ptr0001', 'ptr0002', 'ptr0003', 'ptr0004', 'ptr0005', 'ptr0006',
            'ptr0007', 'ptr0008', 'ptr0009', 'ptr0010', 'ptr0011', 'ptr0012',
            'ptr0013', 'ptr0014', 'ptr0015', 'ptr0016', 'ptr0031'
        }
        self.assertEqual(select(district=['aveiro'], county=['braganca']), to_check)


if __name__ == '__main__':
    unittest.main()
