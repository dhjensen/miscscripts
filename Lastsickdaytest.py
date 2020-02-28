import unittest
from lastsickday import add_days_to_date
from datetime import date

class test_add_days_to_date(unittest.TestCase):
    
    def test_ValueError_returns_none(self):
        im_none = add_days_to_date(1983, 13, 25, 5)
        #self.assertRaises(ValueError, add_days_to_date, 1983, 13, 25, 5)
        self.assertIsNone(im_none, 'I should be None')
    
    def test_return_date(self):
        my_birthday_plus_five_days = date(1983, 5, 30)
        function_return_date = add_days_to_date(1983, 5, 25, 5)
        self.assertEqual(function_return_date, my_birthday_plus_five_days, 'Bleh')
        
        
if __name__ == '__main__':
    unittest.main()