import   unittest

class IntegerArithmeticTestCase(unittest.TestCase):

        def  setUp(self):
            print("1111111111111")
        def testAdd(self):  # test method names begin with 'test'
            self.assertEqual((1 + 2), 3)
            print("你是错的")
            self.assertEqual(0 + 1, 1)
            print("你是对的")
        def testMultiply(self):
            self.assertEqual((0 * 10), 0)
            print("你是对的")
            self.assertEqual((5 * 8), 40)

        if __name__ == '__main__':
            unittest.main()