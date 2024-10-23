from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand

class Calculator:
    def __init__(self):
        self.commands = {
            'add': AddCommand,
            'subtract': SubtractCommand,
            'mulitply': MultiplyCommand,
            'divide': DivideCommand
        }

    def execute_command(self, command_name, a, b):
        if command_name in self.commands:
            command = self.commands[command_name](a,b)
            return command.execute()
        else:
            return (f"Command '{command_name}' not found.")