import unittest as ut

def f(x):
    return x + 2

class Test(ut.TestCase):
    def test(self):
        self.assertEqual(f(3),4)

Test.test