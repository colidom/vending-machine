# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


def run(operations_path: Path) -> bool:
    status_path = 'data/vending/status.dat'
    # TU CÓDIGO AQUÍ

    return filecmp.cmp(status_path, 'data/vending/.expected', shallow=False)


if __name__ == '__main__':
    run('data/vending/operations.dat')