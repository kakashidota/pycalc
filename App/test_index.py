from index import Calc


class TestCalc:
    def test_addition(self):
        assert 4 == Calc.add(2, 2)

    def test_sub(self):
        assert 2 == Calc.sub(4, 2)
