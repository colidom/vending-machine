from pathlib import Path


def init_info(input_path: Path) -> list:
    with open(input_path, "r") as f:
        data = [line.strip() for line in f]
        return data


def operations(input_path: Path) -> list:
    with open(input_path, "r") as f:
        data = [line.strip() for line in f]
        return data


if __name__ == "__main__":
    init_info("input_data/vending.dat")
    operations("input_data/operations.dat")
