import sys
import unittest
import os
import csv
from datetime import datetime
from main import SalesRecorder


class TestSalesRecorder(unittest.TestCase):
    """"""
    def setUp(self) -> None:
        self.test_filename = 'test_sales_data.csv'
        self.recorder = SalesRecorder(filename=self.test_filename)

    def tearDown(self) -> None:
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_create_csv(self):
        # Проверяем, что файл создается и содержит правильные заголовки
        self.recorder.create_csv()
        with open(self.test_filename, mode='r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=';')
            headers = next(csv_reader)
            print(headers)
            self.assertEqual(headers, ['Date', 'Product', 'Spent' 'Sold', 'Net profit'])

    def test_add_sale(self):
        self.recorder.add_sale('Guitar', 2000, 3400)
        with open(self.test_filename, mode='r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=';')
            headers = next(csv_reader)  # Пропускаем заголовки
            sale = next(csv_reader)
            sale = next(csv_reader)

            print('Sale: ', sale)
            self.assertEqual(len(sale), 5)
            self.assertEqual(sale[1], 'Guitar')
            self.assertEqual(float(sale[2]), 2000)
            self.assertEqual(float(sale[3]), 3400)
            self.assertEqual(float(sale[4]), 3400 - 2000)