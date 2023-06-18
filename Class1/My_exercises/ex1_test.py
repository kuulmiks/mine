import ex1

def test_add():
    assert ex1.Calc.add(3, 3) == 6
def test_sub():
    assert ex1.Calc.sub(3, 3) == 0
def test_mul():
    assert ex1.Calc.mul(3, 3) == 0
def test_div():
    assert ex1.Calc.div(3, 3) == 1

