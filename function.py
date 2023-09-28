import unittest

def check(num):
    return num >= 100

class TestCheck(unittest.TestCase):
    def test(self):
        self.assertTrue(check(50))

if __name__=="__main__":
    unittest.main()