# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


# Hacer un pedido
def order(operation: list, products: dict, money: int) -> tuple:
    # Ejemplo de entrada
    operation = ["O", "D12", 7, 21]

    product_code = operation[1]
    product_qty = int(operation[2])
    product_price = int(operation[3])

    if product_code in products and products[product_code] >= product_qty:
        total_price = product_price * product_qty
        if money >= total_price:
            change = money - total_price
            products[product_code] -= product_qty
    # Debe retornar 14 ya que es el total de la primera operación 7 unidades * 2€
    return money


# Reponer un producto
def restock_product(operation: list, money: int):
    # Ejemplo de entrada
    operation = ["R", "F19", 9]
    return


# Cambiar el precio de un producto
def change_product_price(operation: list, new_price: int):
    # Ejemplo de entrada
    operation = ["P", "F10", 3]
    return


# Reponer dinero
def restock_money(operation: list, money: int) -> int:
    money += int(operation[1])
    return money


# Lee fichero de entrada
def read_operations(input_path: Path) -> list:
    with open(input_path, "r") as f:
        operations = [line.strip().split() for line in f]
        return operations


# Escribe operaciones en fichero de salida
def write_status(output_path: Path, products: dict, money: int) -> str:
    with open(output_path, "w") as f:
        f.write(f"{money}")


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

    operations = read_operations(operations_path)
    products = {}
    money = 0

    for operation in operations:
        match operation[0]:
            case "O":
                money = order(operation, products, money)
            case "R":
                restock_product(operation, money)
            case "P":
                change_product_price(operation, money)
            case "M":
                money = restock_money(operation, money)

    # Finalmente escribimos en fichero de salida
    write_status(status_path, products, money)

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    print(run("data/vending/operations.dat"))
