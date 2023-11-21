import unittest

def funcOne():
    return 1

class TestFuncOne(unittest.TestCase):
    def testFunc(self):
        # 테스트 케이스 정의
        # 예상되는 값 =1
        # 실제 함수가 호출되면 1이 나오는가?
        # 호출된 함수 funcOne ==1 ?

        self.assertEqual(funcOne(), 1)
        # fail 테스트
        # self.assertEqual(funcOne(), 0)

if __name__ == '__main__':
    # print("Hi~")
    unittest.main(exit=False)
    # print("Bye~")