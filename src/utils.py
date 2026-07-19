import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    "logs/utils.log",
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
            return data

        logger.error("JSON файл содержит не список")
        return []

    except FileNotFoundError:
        logger.error("JSON файл не найден")
        return []

    except json.JSONDecodeError:
        logger.error("Ошибка чтения JSON файла")
        return []
