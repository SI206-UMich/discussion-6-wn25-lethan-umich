import unittest
import os
import csv
import statistics

from collections import defaultdict

def load_csv(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) years, values are dicts
        inner keys are (str) months, values are (str) integers
    
    Note: Don't strip or otherwise modify strings. Don't change datatypes from strings. 
    '''

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    # use this 'full_path' variable as the file that you open
    data = defaultdict(dict)
    with open(full_path) as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            data[headers[1]][row[0]] = row[1]
            data[headers[2]][row[0]] = row[2]
            data[headers[3]][row[0]] = row[3]
    return data

def get_annual_max(d: dict[str, dict[str, str]]):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: year (str), month (str), and max (int) 
        max is the maximum value for a month in that year, month is the corresponding month

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary.
        You'll have to change vals to int to compare them. 
    '''
    data = []
    for k, v in d.items():
        max_val = 0
        max_month = ""
        for month, value in v.items():
            num = int(value)
            if num > max_val:
                max_month = month
                max_val = num
        data.append((k, max_month, max_val))
    
    return data
def get_month_avg(d: dict[str, dict[str, str]]):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are years and vals are floats rounded to nearest whole num or int
        vals are the average vals for months in the year

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary. 
        You'll have to make the vals int or float here and round the avg to pass tests.
    '''
    data = {}
    for year, year_data in d.items():
        data[year] = statistics.mean(map(int, year_data.values()))

    return data

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
