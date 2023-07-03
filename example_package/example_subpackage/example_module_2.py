import argparse


def func2(a):
    print(f"func2 input: {a}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    )
    parser.add_argument('-input1', default='default cl value')
    args = parser.parse_args()
    func2(args.input1)