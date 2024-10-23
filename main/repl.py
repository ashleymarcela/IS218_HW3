from calculator import Calculator
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def repl():
    calc = Calculator()

    while True:
        command_name = input("Enter command (add, subtract, multiply, divide) or 'exit' to quit: ").lower()

        if command_name == 'exit':
            print('Exiting...')
            break

        try:
            a = float(input('Enter first number: '))
            b = float(input('Enter second number:'))
            result = calc.execute_command(command_name, a, b)
            print('Result: ', result)
        except ZeroDivisionError as e: 
            print(f'Error: {e}')
        except ValueError:
            print('Invalid Input. Please enter valid numbers.')
        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    repl()