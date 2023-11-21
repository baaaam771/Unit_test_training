import unittest

def concat_strings(a, b):
    return a+b

# "A" + "B" = "AB"
# "" + "B" = "B"
# "A" + "" = "A"
# "" + "" = ""

class TestConcat(unittest.TestCase):
    def testNomalCase(self):
        self.assertEqual(concat_strings("A", "B"), "AB")
        self.assertEqual(concat_strings("", "B"), "B")
        self.assertEqual(concat_strings("A", ""), "A")
        self.assertEqual(concat_strings("", ""), "")

    def testSpecialCase(self):
        self.assertEqual(concat_strings("123", "ABC"), "123ABC")
        self.assertEqual(concat_strings("123", "!@#"), "123!@#")

if __name__ == '__main__':
    unittest.main(exit=False)
    