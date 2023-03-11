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
def order(operation: tuple[str], products: dict[str, tuple], money: int) -> int:
    # Ejemplo de entrada
    operation = ["O", "D12", 7, 21]

    product_code = operation[1]
    product_qty = int(operation[2])
    product_price = int(operation[3])

    # Comprobar si prod_code no está en diccionario de products retornar money
    # Desempaquetado de dict products(entrada) concretamente sobre el producto que estamos iterando en este momento (prod_code)
    # Comprobar si el precio * cantidad orneada es mayor que el dinero insertado o el stock es menor que la cantidad ordenada, retornar money
    # Obtener el cambio, producto de la operación dinero insertado - precio  multiplicado por cantidad ordenada(ordered_qty)
    # Sumar a money el dinero insertado - el cambio
    # Actualizar los productos pero recuerda, con el ((stock - la cantidad ordenada), el precio) recuerda siempre actuando sobre el índice que corresponde en cada iteración products[prod_code]
    # Finalmente retornamos money donde ya habremos sumado el resultado de la operación

    if product_code in products and products[product_code] >= product_qty:
        total_price = product_price * product_qty
        if money >= total_price:
            change = money - total_price
            products[product_code] -= product_qty
    # Debe retornar 14 ya que es el total de la primera operación 7 unidades * 2€
    return money


# Actualizar un producto existente
def modify_product(operation: list[str | int], product: tuple, op_type: str) -> tuple[int]:
    restocked_qty = int(operation[2])
    if op_type == "R":
        return (product[0] + restocked_qty, product[1])
    else:
        return (product[0], restocked_qty)


# Agregar un nuevo producto
def create_product(operation: tuple[str], op_type: str) -> tuple[int]:
    restocked_qty = int(operation[2])
    if op_type == "R":
        return (restocked_qty, 0)
    else:
        return (0, restocked_qty)


# Actualizar la información de un producto
def update_product(operation: tuple[str], products: dict[str, tuple], op_type: str) -> dict[str, tuple]:
    prod_code = operation[1]
    if prod_code in products:
        products[prod_code] = modify_product(operation, products[prod_code], op_type)
    elif op_type == "R":
        products[prod_code] = create_product(operation, op_type)
    return products


# Reponer dinero
def restock_money(operation: list[str], money: int) -> int:
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
def run(operations_path: Path, status_path: Path, expected_path: Path) -> bool:
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

    return filecmp.cmp(status_path, expected_path, shallow=False)


if __name__ == "__main__":
    status_path = "data/vending/status.dat"
    operations_path = "data/vending/operations.dat"
    expected_path = "data/vending/.expected"
    print(run(operations_path, status_path, expected_path))
