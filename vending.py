# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path

E1 = "PRODUCT NOT FOUND"
E2 = "UNAVAILABLE STOCK"
E3 = "NOT ENOUGH USER MONEY"

mock_roberto = [["D12", 7, 21], ["D12", 7, 22]]


def order(product_code: str, qty: int, money_inserted: int):
    return


def restock_product(product_code: str, qty_restocked: int):
    return


def change_product_price(product_code: str, new_price: int):
    return


def restock_money(money_amount: int):
    return


def read_operations(input_path: Path) -> list:
    with open(input_path, "r") as f:
        operations = [line.strip().split() for line in f]
        return operations


def status_machine(output_path: Path) -> str:
    with open(output_path, "w") as f:
        data = "Hello World"
        f.write(f"{data}")


def run(operations_path: Path) -> bool:
    status_path = "data/vending/status.dat"
    # TU CÓDIGO AQUÍ

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    print(read_operations("data/vending/operations.dat"))
    status_machine("data/vending/status.dat")
    # order(mock_roberto)
