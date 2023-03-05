# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


# Hacer un pedido
def order(operation: list, products_status: dict) -> tuple:
    return


# Reponer un producto
def restock_product(operation: list, qty_restocked: int):
    return


# Cambiar el precio de un producto
def change_product_price(operation: list, new_price: int):
    return


# Reponer dinero
def restock_money(operation: list, money_amount: int):
    return


# Lee fichero de entrada
def read_operations(input_path: Path) -> list:
    with open(input_path, "r") as f:
        operations = [line.strip().split() for line in f]
        return operations


# Escribe operaciones en fichero de salida
def write_status(output_path: Path, products_status: dict, balance: int) -> str:
    with open(output_path, "w") as f:
        f.write(f"{balance}")
        for product_status in products_status:
            pass


# Función auxiliar para informar errores
def set_error(error: str) -> dict:
    match error:
        case "E1":
            error_desc = {"code": "E1", "desc": "PRODUCT NOT FOUND"}
        case "E2":
            error_desc = {"code": "E2", "desc": "UNAVAILABLE STOCK"}
        case "E3":
            error_desc = {"code": "E3", "desc": "NOT ENOUGH USER MONEY"}
        case _:
            error_desc = {"code": "E0", "desc": "UNKNOWN ERROR"}

    return error_desc


# Función rincipal
def run(operations_path: Path) -> bool:
    status_path = "data/vending/status.dat"

    operations = []
    products_status = {}
    balance = 0

    for operation in operations:
        match operation[0]:
            case "O":
                order(operation, products_status, balance)
            case "R":
                restock_product(operation, products_status)
            case "P":
                change_product_price(operation, products_status)
            case "M":
                restock_money(operation, balance)

    # Finalmente escribimos en fichero de salida
    write_status(status_path, products_status, balance)

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    print(run("data/vending/operations.dat"))
