"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""

import sys
import click
from src.calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""

    try:
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "power":
            result = power(num1, num2)
        elif operation == "sqrt":
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Format result: int if whole, else 2 decimals
        if isinstance(result, float) and result.is_integer():
            click.echo(int(result))
        elif isinstance(result, float):
            click.echo(f"{result:.2f}")
        else:
            click.echo(result)

    except ValueError as e:
        # Specifically handle divide by zero
        if "zero" in str(e).lower():
            click.echo("Cannot divide by zero")
        else:
            click.echo(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()
