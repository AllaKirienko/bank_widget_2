import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

file_handler = logging.FileHandler(
    LOG_DIR / "utils.log",
    mode="w",
    encoding="utf-8"
)

file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def read_json_file(file_path: str) -> list[dict]:
    """Читает JSON-файл и возвращает список словарей с данными."""

    try:
        with Path(file_path).open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            logger.debug("JSON файл успешно прочитан")
            return [
                normalize_transaction(item)
                for item in data
                if item
            ]

        logger.error("JSON файл содержит не список")
        return []

    except FileNotFoundError:
        logger.error("JSON файл не найден")
        return []

    except json.JSONDecodeError:
        logger.error("Ошибка чтения JSON файла")
        return []


def normalize_transaction(transaction: dict) -> dict:
    """Приводит транзакцию к единому формату."""

    if "operationAmount" in transaction:
        return {
            "id": transaction["id"],
            "state": transaction["state"],
            "date": transaction["date"],
            "amount": float(transaction["operationAmount"]["amount"]),
            "currency_name": (
                transaction["operationAmount"]["currency"]["name"]
            ),
            "currency_code": (
                transaction["operationAmount"]["currency"]["code"]
            ),
            "description": transaction["description"],
            "from": transaction.get("from"),
            "to": transaction.get("to"),
        }

    return {
        "id": transaction["id"],
        "state": transaction["state"],
        "date": transaction["date"],
        "amount": float(transaction["amount"]),
        "currency_name": transaction["currency_name"],
        "currency_code": transaction["currency_code"],
        "description": transaction["description"],
        "from": transaction.get("from"),
        "to": transaction.get("to"),
    }
