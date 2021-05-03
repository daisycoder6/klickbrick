import argparse


def main():
    """
    main entry point to script
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('hello')

    args=parser.parse_args()

    if args.hello:
        print("Hello World")
    else:
        pass


if __name__ == "__main__":
    main()