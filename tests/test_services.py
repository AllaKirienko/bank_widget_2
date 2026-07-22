from src.services import (format_transaction, process_bank_operations,
                          process_bank_search)


def test_process_bank_search() -> None:
    """Проверяет поиск операций по описанию."""

    data = [
        {
            "description": "Перевод организации",
            "amount": 1000,
        },
        {
            "description": "Открытие вклада",
            "amount": 5000,
        },
        {
            "description": "Перевод с карты на карту",
            "amount": 2000,
        },
    ]

    result = process_bank_search(data, "перевод")

    assert len(result) == 2
    assert result[0]["description"] == "Перевод организации"
    assert result[1]["description"] == "Перевод с карты на карту"


def test_process_bank_search_no_results() -> None:
    """Проверяет поиск при отсутствии совпадений."""

    data = [
        {
            "description": "Открытие вклада",
            "amount": 5000,
        }
    ]

    result = process_bank_search(data, "перевод")

    assert result == []


def test_process_bank_operations() -> None:
    """Проверяет подсчёт операций по категориям."""

    data = [
        {"description": "Перевод организации"},
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
    ]

    categories = [
        "Перевод организации",
        "Открытие вклада",
        "Перевод с карты на карту",
    ]

    result = process_bank_operations(data, categories)

    assert result == {
        "Перевод организации": 2,
        "Открытие вклада": 1,
        "Перевод с карты на карту": 1,
    }


def test_format_transaction_with_from_and_to() -> None:
    """Проверяет форматирование операции с отправителем и получателем."""

    transaction = {
        "date": "2019-12-08T10:00:00",
        "description": "Перевод с карты на карту",
        "amount": 1000.5,
        "currency_code": "RUB",
        "from": "Карта 1234",
        "to": "Счет 5678",
    }

    result = format_transaction(transaction)

    assert result == (
        "2019-12-08 Перевод с карты на карту\n"
        "Карта 1234 -> Счет 5678\n"
        "Сумма: 1000.5 RUB"
    )


def test_format_transaction_with_to_only() -> None:
    """Проверяет форматирование операции только с получателем."""

    transaction = {
        "date": "2019-12-08",
        "description": "Открытие вклада",
        "amount": 5000,
        "currency_code": "RUB",
        "to": "Счет 5678",
    }

    result = format_transaction(transaction)

    assert result == (
        "2019-12-08 Открытие вклада\n"
        "Счет 5678\n"
        "Сумма: 5000 RUB"
    )


def test_format_transaction_without_accounts() -> None:
    """Проверяет форматирование операции без счетов."""

    transaction = {
        "date": "2019-12-08",
        "description": "Пополнение",
        "amount": 100,
        "currency_code": "RUB",
    }

    result = format_transaction(transaction)

    assert result == (
        "2019-12-08 Пополнение\n"
        "Сумма: 100 RUB"
    )
