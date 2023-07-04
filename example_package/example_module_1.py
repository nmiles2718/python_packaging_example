"""
Example module
"""
def func1(*args):
    """ Example function

    Parameters
    ----------
    args

    Returns
    -------

    """
    for i, arg in enumerate(args):
        print(f"func1 input {i+1:0.0f}: {arg}")
