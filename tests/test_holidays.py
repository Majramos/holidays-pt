#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_holidays.py
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

from holidays.holidays import Holidays, _convert_codes, _calc_holiday_date


class TestHolidays(unittest.TestCase):

    def setUp(self):
        self.hol = Holidays('2020-01-01', '2021-12-31')

    def test_convert_codes_f(self):
        self.assertEqual(_convert_codes(2022, 'f', [1,1,0]),
                         datetime(2022, 1, 1, 0, 0))

    def test_convert_codes_m(self):
        self.assertEqual(_convert_codes(2022, 'm', [8, 2,0]),
                         datetime(2022, 8, 15, 0, 0))

    def test__calc_holiday_date(self):
        to_check = [
            {'extent': 'national',
             'label': 'Ano Novo',
             'calculate': 'january 1st',
             'date': datetime(2022, 1, 1, 0, 0)}
        ]
        source = _calc_holiday_date([2022], [{
            'extent': 'national', 'label': 'Ano Novo', 'type': 'f',
            'codes': [1, 1, 0], 'calculate': 'january 1st'
        }])
        self.assertEqual(source, to_check)

    def test_list_national(self):
        to_check = {
            'extent': 'national',
            'label': 'Ano Novo',
            'calculate': 'january 1st',
            'date': '2022-01-01'
        }
        self.assertEqual(Holidays.ls(extent='national')[0], to_check)

    def test_list_regional(self):
        to_check = {
            'extent': 'regional',
            'label': 'Sao Geraldo',
            'calculate': 'monday after pentacost sunday',
            'date': '2022-06-06'
        }
        self.assertEqual(Holidays.ls(extent='regional')[0], to_check)

    def test__str__(self):
        to_check = 'Holidays(start_date=2020-01-01, end_date=2021-12-31)'
        self.assertEqual(str(self.hol), to_check)

    def test_leap_years(self):
        self.assertEqual(self.hol.leap_years(), {2020: True, 2021: False})

    def test_date_in_timeframe(self):
        self.assertTrue('2021-06-15' in self.hol)

    def test_date_not_in_timeframe(self):
        self.assertFalse('2019-01-01' in self.hol)

    def test_as_list(self):
        to_check = [
            {'extent': 'national',
             'label': 'Ano Novo',
             'calculate': 'january 1st',
             'date': datetime(2020, 1, 1, 0, 0)},
            {'extent': 'national',
             'label': 'Carnaval',
             'calculate': '47 days before easter sunday on a tuesday',
             'date': datetime(2020, 2, 25, 0, 0)}
        ]
        self.assertEqual(self.hol.calculate().as_list()[:2], to_check)

    def test_date_str(self):
        to_check = [
            {'extent': 'national',
             'label': 'Ano Novo',
             'calculate': 'january 1st',
             'date': '2020-01-01'},
            {'extent': 'national',
             'label': 'Carnaval',
             'calculate': '47 days before easter sunday on a tuesday',
             'date': '2020-02-25'}
        ]
        self.assertEqual(self.hol.calculate().date_str().as_list()[:2], to_check)

    def test_drop(self):
        to_check = [
            {'extent': 'national',
             'label': 'Ano Novo',
             'date': datetime(2020, 1, 1, 0, 0)},
            {'extent': 'national',
             'label': 'Carnaval',
             'date': datetime(2020, 2, 25, 0, 0)}
        ]
        self.assertEqual(self.hol.calculate().drop(['calculate']).as_list()[:2], to_check)


if __name__ == '__main__':
    unittest.main()