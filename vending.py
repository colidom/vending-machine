# ******************
# MAQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


def read_operations(input_path: str) -> list:
    with open(input_path, "r") as f:
        operations = [tuple(line.strip().split()) for line in f]
        return operations


def order(operation: tuple, products: dict[str, tuple], money: int) -> int:
    product_code = operation[1]
    ordered_qty = int(operation[2])
    inserted_money = int(operation[3])

    if product_code not in products:
        return money

    stock, price = products[product_code]

    if ordered_qty > stock or ordered_qty * price > inserted_money:
        return money

    change = int(inserted_money) - price * ordered_qty
    money += int(inserted_money) - change
    products[product_code] = (stock - ordered_qty, price)

    return money


def modify_product(operation: tuple, product: tuple, op_type: str) -> tuple[int, int]:
    restocked_qty = int(operation[2])
    if op_type == "R":
        return (product[0] + restocked_qty, product[1])
    return (product[0], restocked_qty)


def create_product(operation: tuple) -> tuple[int, int]:
    restocked_qty = int(operation[2])
    return restocked_qty, 0


def update_product(operation: tuple, products: dict[str, tuple], op_type: str) -> dict[str, tuple]:
    prod_code = operation[1]
    if prod_code in products:
        products[prod_code] = modify_product(operation, products[prod_code], op_type)
    elif op_type == "R":
        products[prod_code] = create_product(operation)
    return products


def restock_money(operation: tuple, money: int) -> int:
    money += int(operation[1])
    return money


def write_status_file(file_path: str, products: dict, money: int):
    with open(file_path, "w") as f:
        f.write(f"{money}\n")

        prod_codes = sorted(products.keys())
        for prod_code in prod_codes:
            stock, price = products[prod_code]
            f.write(f"{prod_code} {stock} {price}\n")


def run(operations_path: str) -> bool:
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

    write_status_file(status_path, products, money)

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    operations_path = "data/vending/operations.dat"
    run(operations_path)
