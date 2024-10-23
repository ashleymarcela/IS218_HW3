import pytest
from main.calculator import Calculator 

def test_add_command():
    calc = Calculator()
    result = calc.execute_command('add', 5, 3)
    assert result == 8

def test_subtract_command():
      calc = Calculator()
    result = calc.execute_command('subtract', 5, 3)
    assert result == 2

def test_multiply_command():
    calc = Calculator()
    result = calc.execute_command('multiply', 5, 3)
    assert result == 15

def test_divide_command():
    calc = Calculator()
    result = calc.execute_command('divide', 6, 2)
    assert result == 3

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        celc.execute_command('divide', 5, 0)

def test_invalid_command():
    calc = Calculator()
    result = calc.execute_command('mod', 5, 3)
    assert result = "Command 'mod' not found."