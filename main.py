import unittest



class TestStringUpper(unittest.TestCase):
    def testUpeer(self):
        self.assertEqual('abc'.upper(), 'ABC')
        self.assertEqual('Ab'.upper(), 'AB')
        self.assertEqual('d'.upper(), 'D')

    # 대문자에만 동작
    # 숫자, 특수문자 경우 false
    # 들어가 있는 문자가 다 대문자인경우 True (ABC123)

    def testUpperCase(self):
        self.assertTrue('ABC'.isupper())
        self.assertFalse('ABc'.isupper())

    def testNumberCase(self):
        self.assertFalse('123'.isupper())
        self.assertTrue('ABC123'.isupper())

    def testMarkCase(self):
        self.assertFalse('?'.isupper())

    def testSpecialCase(self):
        self.assertTrue('ABC123'.isupper())
        self.assertFalse(''.isupper())



if __name__ == '__main__':
    
   
    unittest.main(exit=False)
    