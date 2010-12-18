import unittest

from surreal import Surreal as S

class SurrealTests(unittest.TestCase):
    equivalent_symbols = (('{|}', 0),
                          ('{1|}', 1))

    def test_equivalent_symbols(self):
        for left, right in self.equivalent_symbols:
            self.assertTrue(S(left) == S(right), "%s should equal %s" % (left, right))

if __name__ == '__main__':
    unittest.main()