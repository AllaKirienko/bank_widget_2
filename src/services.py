import re
from collections import Counter


def process_bank_operations(
    data: list[dict],
    categories: list[str]
) -> dict[str, int]:
    """Подсчитывает количество операций по категориям."""

    descriptions = [
        transaction.get("description", "")
        for transaction in data
    ]

    counter = Counter(descriptions)

    return {
        category: counter[category]
        for category in categories
    }


def process_bank_search(
    data: list[dict],
    search: str
) -> list[dict]:
    """Ищет транзакции по строке в поле description."""

    pattern = re.compile(search, re.IGNORECASE)

    return [
        transaction
        for transaction in data
        if pattern.search(transaction.get("description", ""))
    ]


def format_transaction(transaction: dict) -> str:
    """Форматирует одну банковскую операцию для вывода."""

    date = transaction.get("date", "")
    date = date[:10]

    description = transaction.get("description", "")
    amount = transaction.get("amount", 0)
    currency = transaction.get("currency_code", "")

    from_account = transaction.get("from")
    to_account = transaction.get("to")

    result = (
        f"{date} {description}\n"
    )

    if from_account and to_account:
        result += f"{from_account} -> {to_account}\n"
    elif to_account:
        result += f"{to_account}\n"
    elif from_account:
        result += f"{from_account}\n"

    result += f"Сумма: {amount:g} {currency}"

    return result
