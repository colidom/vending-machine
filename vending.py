# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


# Leer el archivo de operaciones
def read_operations(input_path: Path) -> list:
    with open(input_path, "r") as f:
        operations = [tuple(line.strip().split()) for line in f]
        return operations


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


# Actualizar un producto existente
def update_existing_product(operation: list, product: tuple, op_type: str) -> tuple:
    if op_type == "R":
        return  # algo
    else:
        return  # algo


# Agregar un nuevo producto
def create_product(operation: list, op_type: str) -> tuple:
    if op_type == "R":
        return  # algo
    else:
        return  # algo


# Actualizar la información de un producto
def update_product(operation: list, products: dict, op_type: str) -> dict:
    prod_code = operation[1]
    if prod_code in products:
        products[prod_code] = update_existing_product(operation, products[prod_code], op_type)
    elif op_type == "R":
        products[prod_code] = create_product(operation, op_type)
    return products


# Reponer dinero
def restock_money(operation: list, money: int) -> int:
    money += int(operation[1])
    return money


# Escribe operaciones en fichero de salida
def write_status_file(path: Path, products: dict, money: int):
    with open(path, "w") as f:
        f.write(f"{money}\n")
        for code, details in sorted(products.items()):
            f.write(f"{code} {details['stock']} {details['price']}\n")


# Función rincipal
def run(operations_path: Path) -> bool:
    status_path = "data/vending/status.dat"

    operations = read_operations(operations_path)
    products = {}
    money = 0

    for operation in operations:
        op_type = operation[0]
        match operation[0]:
            case "O":
                money = order(operation, products, money)
            case "R":
                update_product(operation, money, op_type)
            case "P":
                update_product(operation, money, op_type)
            case "M":
                money = restock_money(operation, money)

    # Finalmente escribimos en fichero de salida
    write_status_file(status_path, products, money)

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    print(run("data/vending/operations.dat"))
