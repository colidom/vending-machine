# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path

E1 = "PRODUCT NOT FOUND"
E2 = "UNAVAILABLE STOCK"
E3 = "NOT ENOUGH USER MONEY"


# Hacer un pedido
def order(operation: list, products: dict) -> tuple:
    return


# Reponer un producto
def restock_product(product_code: str, qty_restocked: int):
    return


# Cambiar el precio de un producto
def change_product_price(product_code: str, new_price: int):
    return


# Reponer dinero
def restock_money(money_amount: int):
    return


# Lee fichero de entrada
def read_operations(input_path: Path) -> list:
    with open(input_path, "r") as f:
        operations = [line.strip().split() for line in f]
        return operations


# Escribe operaciones en fichero de salida
def status_machine(output_path: Path) -> str:
    with open(output_path, "w") as f:
        data = "Hello World"
        f.write(f"{data}")


# Principal
def run(operations_path: Path) -> bool:
    status_path = "data/vending/status.dat"
    # TU CÓDIGO AQUÍ

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    read_operations("data/vending/operations.dat")
    status_machine("data/vending/status.dat")
