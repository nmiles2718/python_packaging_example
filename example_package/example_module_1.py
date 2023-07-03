import argparse


def func1(a):
    print(f"func1 input: {a}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    )
    parser.add_argument('-input1', default='default cl value')
    args = parser.parse_args()
    func1(args.input1)