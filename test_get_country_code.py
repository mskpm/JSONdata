import unittest
from country_codes import get_country_code

class Test_test_get_country_code(unittest.TestCase):
    def test_if_none(self):
        answer = get_country_code('xyz')
        self.assertEqual(answer, None)
    
    def test_for_poland(self):
        answer = get_country_code('Poland')
        self.assertEqual(str(answer), 'pl')

if __name__ == '__main__':
    unittest.main()
