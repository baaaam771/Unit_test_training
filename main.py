import unittest

def add(a, b):
    return a+b

def sub(a,b):
    return a-b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertNotEqual(add(2, 4), 7)

class TestSub(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(sub(7, 3), 4)

if __name__ == '__main__':

    suite = unittest.TestSuite()

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAdd))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSub))

    unittest.TextTestRunner().run(suite)
   
    # unittest.main(exit=False)
    