#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_codes.py
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

from holidays.codes import  select


class TestCodes(unittest.TestCase):

    def test_select(self):
        to_check = [
            {'extent': 'national', 'label': 'Ano Novo', 'type': 'f',
              'codes': [1, 1, 0], 'calculate': 'january 1st'},
             {'extent': 'national', 'label': 'Sexta-Feira Santa', 'type': 'e',
              'codes': [-2, 0, 0], 'calculate': 'friday right before easter sunday'},
             {'extent': 'regional',  'label': 'Sao Tome', 'type': 'f',
              'codes': [7, 25, 0], 'calculate': 'july 25th'},
             {'extent': 'regional', 'label': 'Elevacao Sines a vila (1362)',
              'type': 'f', 'codes': [11, 24, 0], 'calculate': 'november 24th'}
        ]

        self.assertEqual(select(codes=['ptn0001', 'ptn0003', 'ptr0051', 'ptr0136']), to_check)


if __name__ == '__main__':
    unittest.main()
