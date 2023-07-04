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
            ],
        input2:
            Annotated[
                int,
                typer.Option(help="Argument help message")
            ]
):
    """Entry point for the CLI
    
    The point of this function is define the CL arguments and pass them to the
    desired function. 
    
    Parameters
    ----------
    input1 : str
        The first input for the CLI
        
    input2 : str
        The second input for the CLI
    Returns
    -------

    """
    func1(input1, input2)

def main():
    return typer.run(cli)

if __name__ == "__main__":
    main()