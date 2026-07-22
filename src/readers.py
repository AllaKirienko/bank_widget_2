from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent


def read_csv(file_path: str) -> list[dict]:
    """Считывает финансовые операции из CSV-файла.

    Args:
        file_path: Путь к CSV-файлу.

    Returns:
        Список словарей с транзакциями.
    """
    path = BASE_DIR / file_path
    data = pd.read_csv(path, sep=";")
    return data.to_dict(orient="records")


def read_excel(file_path: str) -> list[dict]:
    """Считывает финансовые операции из Excel-файла.

    Args:
        file_path: Путь к Excel-файлу.

    Returns:
        Список словарей с транзакциями.
    """
    path = BASE_DIR / file_path
    data = pd.read_excel(path)
    return data.to_dict(orient="records")
