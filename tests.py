import unittest

from surreal import dali, shorthand, Surreal as S, BadlyFormed

class DaliTests(unittest.TestCase):
    def testZero(self):
        self.assertEquals(S(set(), set()), dali(0))
    def testOne(self):
        self.assertRuleForPositiveIntegers(1)
    def testSetOfPositiveIntegers(self):
        for x in range(1, 100):
            self.assertRuleForPositiveIntegers(x)
    def testMinusOne(self):
        self.assertRuleForNegativeIntegers(1)
    def testSetOfNegativeIntegers(self):
        for x in range(-1, -100):
            self.assertRuleForNegativeIntegers(x)

    def assertRuleForPositiveIntegers(self, x):
        self.assertEquals(dali(x-1), dali(x))
    def assertRuleForNegativeIntegers(self, x):
        self.assertEquals(dali(x+1), dali(x))

class SurrealTests(unittest.TestCase):
    well_formed = ((set(), set()),)

    def test_well_formed_numbers(self):
        for left, right in self.well_formed:
            S(left, right)

    def test_inequality_of_zero(self):
        assert S(set(), set()) <= S(set(), set())

class ShorthandTests(unittest.TestCase):
    equivalent_symbols = (('{|}',  0),
                          ('{0|}', 1),
                          ('{1|}', 2),
                          ('{|0}', -1),
                          )

    well_formed = ('{|}', '0', '{0|}', '{|0}')
    not_well_formed = ('{0|0}',)
    le_inequalities = (('{|}', '{0|}'),
                       ('{0|}', '{0|}'))

    def test_well_formed_shorthands(self):
        for sh in self.well_formed:
            try:
                assert type(shorthand(sh)) == S
            except BadlyFormed:
                self.fail("%s should be well-formed" % sh)

    def test_not_well_formed_shorthands(self):
        for sh in self.not_well_formed:
            try:
                shorthand(sh)
                self.fail("%s should raise a BadlyFormed exception" % sh)
            except BadlyFormed:
                pass

    def test_le_inequalities(self):
        for left, right in self.le_inequalities:
            self.assertTrue(shorthand(left) <= shorthand(right))

    def _test_equivalent_symbols(self):
        for left, right in self.equivalent_symbols:
            leftSurreal = shorthand(left)
            rightSurreal = shorthand(right)
            self.assertTrue(leftSurreal == rightSurreal, 
                    "%s should equal %s (Surreal: %s == %s)" % 
                    (left, right, leftSurreal, rightSurreal))

if __name__ == '__main__':
    unittest.main()