import unittest

def getDataPoint(stock_data):
    
    name, date, open_price, high_price, low_price, volume = stock_data
    return {
        'name': name,
        'date': date,
        'open': open_price,
        'high': high_price,
        'low': low_price,
        'volume': volume
    }

def getRatio(price_a, price_b):
  
    if price_b == 0:
        return None 
    return price_a / price_b

class TestStockMethods(unittest.TestCase):

    def test_getDataPoint(self):
        stock_data = ('DEF', '2023-23-05', 100.0, 110.0, 105.0, 10000)
        expected_output = {
            'name': 'DEF',
            'date': '2023-23-05',
            'open': 100.0,
            'high': 110.0,
            'low': 105.0,
            'volume': 10000
        }
        result = getDataPoint(stock_data)
        self.assertEqual(result, expected_output)

    def test_getRatio(self):
        self.assertEqual(getRatio(100.0, 50.0), 2.0)
        self.assertEqual(getRatio(50.0, 100.0), 0.5)
        self.assertEqual(getRatio(10.0, 0), None)  
        self.assertEqual(getRatio(0, 10.0), 0.0)   

if __name__ == '__main__':
    unittest.main()
