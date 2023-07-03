from typing import Optional

import typer
from typing_extensions import Annotated
try:
    from .example_module_1 import func1
except ImportError as e:
    from example_module_1 import func1

def cli(
        input1:
            Annotated[
                int,
                typer.Option(help="Option help message")
            ] = 20,
        input2:
            Annotated[
                int,
                typer.Argument(help="Argument help message")
            ] = 10
):
    func1(input1, input2)

def main():
    return typer.run(cli)

if __name__ == "__main__":
    typer.run(cli)