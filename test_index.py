from index import Calc


class TestCalc:
    def test_addition(self):
        assert 4 == Calc.add(2, 2)
        assert 10 == Calc.add(5, 5)

    def test_sub(self):
        assert 2 == Calc.sub(4, 2)
        assert 10 == Calc.sub(20, 10)
