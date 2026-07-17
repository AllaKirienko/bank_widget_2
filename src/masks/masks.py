from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    number = str(card_number).replace(" ", "")

    if len(number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def get_mask_account(account_number: Union[str, int]) -> str:
    number = str(account_number).replace(" ", "")

    if len(number) < 4:
        raise ValueError("Некорректный номер счета")

    return f"**{number[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("1234567812345678"))
    print(get_mask_account("1234567890"))
