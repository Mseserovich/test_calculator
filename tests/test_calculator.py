from simple_calculator.calculator import add, multiply

def test_add_output():
    output = add(1,2,3,4)
    assert output == 10 , "output value is incorrect"

def test_mult_output():
    output = multiply(1,2,3,4)
    assert output == 24, "output is incorrect"