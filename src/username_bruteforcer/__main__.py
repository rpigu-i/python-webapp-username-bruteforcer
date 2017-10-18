import argparse
from gen_logo import Logo
from username_bruteforcer import UsernameBruteforcer



def main():
    logo = Logo()
    logo.generate_logo()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "yaml",
        help="a YAML configuration file")
    args = parser.parse_args()
    username_bruteforcer = UsernameBruteforcer(args.yaml)


if __name__ == "__main__":
    main()
