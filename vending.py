# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


# Hacer un pedido
def order(stock, money, code):
    product_code = code[:3]
    product_qty = int(code[3])
    product_price = float(code[4:])

    if product_code in stock and stock[product_code] >= product_qty:
        total_price = product_price * product_qty
        if money >= total_price:
            change = money - total_price
            stock[product_code] -= product_qty
            return (True, change)
        else:
            return (False, 0)
    else:
        return (False, 0)


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
def write_status(output_path: Path, sales: dict, balance: int) -> str:
    with open(output_path, "w") as f:
        f.write(f"{balance}")
        for sale in sales:
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
    sales = {}
    balance = 0

    for operation in operations:
        match operation[0]:
            case "O":
                order(operation, sales, balance)
            case "R":
                restock_product(operation, sales)
            case "P":
                change_product_price(operation, sales)
            case "M":
                restock_money(operation, balance)

    # Finalmente escribimos en fichero de salida
    write_status(status_path, sales, balance)

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    print(run("data/vending/operations.dat"))
