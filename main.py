import unittest



class TestStringUpper(unittest.TestCase):
    def testUpeer(self):
        self.assertEqual('abc'.upper(), 'ABC')
        self.assertEqual('Ab'.upper(), 'AB')
        self.assertEqual('d'.upper(), 'D')
        

if __name__ == '__main__':
    # 'foo'.upper()
    # print('abc'.upper())
    unittest.main(exit=False)
    