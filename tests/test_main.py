from unittest.mock import patch

from src.main import main


def test_main_json_file() -> None:
    """Проверяет обработку JSON-файла."""

    transactions = [
        {
            "state": "EXECUTED",
            "date": "2019-01-01",
            "currency_code": "RUB",
            "description": "Перевод",
            "amount": 100,
            "from": "Карта 1234",
            "to": "Счет 5678",
        }
    ]

    user_inputs = [
        "1",
        "executed",
        "нет",
        "нет",
        "нет",
    ]

    with patch(
        "src.main.read_json_file",
        return_value=transactions
    ), patch(
        "builtins.input",
        side_effect=user_inputs
    ):
        main()


def test_main_csv_file() -> None:
    """Проверяет обработку CSV-файла."""

    transactions = [
        {
            "state": "EXECUTED",
            "date": "2019-01-01",
            "currency_code": "RUB",
            "description": "Перевод",
            "amount": 100,
        }
    ]

    user_inputs = [
        "2",
        "executed",
        "нет",
        "нет",
        "нет",
    ]

    with patch(
        "src.main.read_csv",
        return_value=transactions
    ), patch(
        "builtins.input",
        side_effect=user_inputs
    ):
        main()


def test_main_invalid_menu_choice() -> None:
    """Проверяет неправильный пункт меню."""

    with patch(
        "builtins.input",
        return_value="5"
    ):
        main()


def test_main_invalid_status_then_valid() -> None:
    """Проверяет повторный ввод неправильного статуса."""

    transactions = [
        {
            "state": "EXECUTED",
            "date": "2019-01-01",
            "currency_code": "RUB",
            "description": "Перевод",
            "amount": 100,
        }
    ]

    user_inputs = [
        "1",
        "wrong",
        "executed",
        "нет",
        "нет",
        "нет",
    ]

    with patch(
        "src.main.read_json_file",
        return_value=transactions
    ), patch(
        "builtins.input",
        side_effect=user_inputs
    ):
        main()


def test_main_empty_result() -> None:
    """Проверяет сообщение при пустой выборке."""

    transactions = [
        {
            "state": "CANCELED",
            "date": "2019-01-01",
            "currency_code": "USD",
            "description": "Перевод",
            "amount": 100,
        }
    ]

    user_inputs = [
        "1",
        "executed",
        "нет",
        "нет",
        "нет",
    ]

    with patch(
        "src.main.read_json_file",
        return_value=transactions
    ), patch(
        "builtins.input",
        side_effect=user_inputs
    ):
        main()
