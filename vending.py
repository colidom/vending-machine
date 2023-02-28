# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


def operations(input_path: Path) -> list:
    with open(input_path, "r") as f:
        data = [line.strip() for line in f]
        return data


def status_machine(output_path: Path) -> str:
    with open(output_path, "w") as f:
        data = "Hello World"
        f.write(f"{data}")


def run(operations_path: Path) -> bool:
    status_path = "data/vending/status.dat"
    # TU CÓDIGO AQUÍ

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    operations("data/vending/operations.dat")
    status_machine("data/vending/status.dat")
