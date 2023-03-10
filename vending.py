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
def order(operation: list, products: dict, money: int) -> int:
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
def modify_product(operation: list, product: tuple, op_type: str) -> tuple:
    restocked_qty = int(operation[2])
    if op_type == "R":
        return (product[0] + restocked_qty, product[1])
    else:
        return (product[0], restocked_qty)


# Agregar un nuevo producto
def create_product(operation: list, op_type: str) -> tuple:
    restocked_qty = int(operation[2])
    if op_type == "R":
        return (restocked_qty, 0)
    else:
        return (0, restocked_qty)


# Actualizar la información de un producto
def update_product(operation: list, products: dict, op_type: str) -> dict:
    prod_code = operation[1]
    if prod_code in products:
        products[prod_code] = modify_product(operation, products[prod_code], op_type)
    elif op_type == "R":
        products[prod_code] = create_product(operation, op_type)
    return products


# Reponer dinero
def restock_money(operation: list, money: int) -> int:
    money += int(operation[1])
    return money


# Escribir el archivo de estado
def write_status_file(file_path: Path, products: dict, money: int):
    with open(file_path, "w") as f:
        f.write(f"{money}\n")

        prod_codes = sorted(products.keys())
        for prod_code in prod_codes:
            stock, price = products[prod_code]
            f.write(f"{prod_code} {stock} {price}\n")


# Función Principal
def run(operations_path: Path) -> bool:
    status_path = "data/vending/status.dat"

    operations = read_operations(operations_path)
    products = {}
    money = 0

    for operation in operations:
        op_type = operation[0]
        match op_type:
            case "O":
                money = order(operation, products, money)
            case "R" | "P":
                update_product(operation, products, op_type)
            case "M":
                money = restock_money(operation, money)

    # Finalmente escribimos en fichero de salida
    write_status_file(status_path, products, money)

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    print(run("data/vending/operations.dat"))
