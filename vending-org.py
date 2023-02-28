from pathlib import Path


# def init_info(input_path: Path) -> list:
#     with open(input_path, "r") as f:
#         data = [line.strip() for line in f]
#         return data


def operations(input_path: Path) -> list:
    with open(input_path, "r") as f:
        data = [line.strip() for line in f]
        print(data)


def status_machine(output_path: Path) -> str:
    with open(output_path, "w") as f:
        data = "Hello World"
        f.write(f"{data}")


if __name__ == "__main__":
    operations("data/vending/operations.dat")
    status_machine("data/vending/status.dat")
