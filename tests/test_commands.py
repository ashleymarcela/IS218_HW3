from commands.add import AddCommand
from commands.subtract import SubtractCommand
from commands.multiply import MultiplyCommand
from commands.divide import DivideCommand
import pytest

def test_add_command():
    command = AddCommand(10, 5)
    assert command.execute() == 15

def test_subtract_command():
    command = SubtractCommand(10, 5)
    assert command.execute() == 5

def test_multiply_command():
    command = MultiplyCommand(10, 5)
    assert command.execute() == 50

def test_divide_command():
    command = DivideCommand(10,0)
    with pytest.raises(ZeroDivisionError):
        command.execute()