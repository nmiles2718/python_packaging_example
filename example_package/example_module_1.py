import argparse


def func1(*args):
    for i, arg in enumerate(args):
        print(f"func1 input {i+1:0.0f}: {arg}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    )
    parser.add_argument('-input1', default='default cl value')
    args = parser.parse_args()
    func1(args.input1)