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
            self.assertEqual(headers, ['Date', 'Product', 'Quantity', 'Price', 'Total'])