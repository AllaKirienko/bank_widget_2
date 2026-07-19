import logging
from typing import Union

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    "logs/masks.log",
    mode="w",
    encoding="utf-8"
)

file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str, int]) -> str:
    number = str(card_number).replace(" ", "")

    if len(number) != 16:
        logger.error("Некорректный номер карты")
        raise ValueError("Номер карты должен содержать 16 цифр")

    result = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    logger.debug("Маска номера карты успешно создана")

    return result


def get_mask_account(account_number: Union[str, int]) -> str:
    number = str(account_number).replace(" ", "")

    if len(number) < 4:
        logger.error("Некорректный номер счета")
        raise ValueError("Некорректный номер счета")

    result = f"**{number[-4:]}"
    logger.debug("Маска номера счета успешно создана")

    return result


if __name__ == "__main__":
    print(get_mask_card_number("1234567812345678"))
    print(get_mask_account("1234567890"))
