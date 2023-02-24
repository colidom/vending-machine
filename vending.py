from pathlib import Path


def init_info(input_path: Path) -> bool:

    with open(input_path, "r") as f:
        for line in f:
            print(line.strip())


if __name__ == "__main__":
    init_info("input_data/vending.dat")
