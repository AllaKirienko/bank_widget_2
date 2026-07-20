from src.utils import normalize_transaction, read_json_file


def test_read_json_file():
    """Проверяет чтение JSON файла."""

    result = read_json_file("data/operations.json")

    assert isinstance(result, list)
    assert len(result) > 0


def test_read_empty_json_file(tmp_path):
    """Проверяет пустой JSON файл."""

    file = tmp_path / "empty.json"
    file.write_text("")

    result = read_json_file(str(file))

    assert result == []


def test_read_not_found_file():
    """Проверяет отсутствие файла."""

    result = read_json_file("data/no_file.json")

    assert result == []


def test_normalize_json_transaction():
    """Проверяет преобразование JSON транзакции."""

    transaction = {
        "id": 1,
        "state": "EXECUTED",
        "date": "2023-01-01",
        "operationAmount": {
            "amount": "1000",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод",
        "from": "Card",
        "to": "Account"
    }

    result = normalize_transaction(transaction)

    assert result["amount"] == 1000.0
    assert result["currency_code"] == "RUB"


def test_normalize_csv_transaction():
    """Проверяет преобразование CSV/Excel транзакции."""

    transaction = {
        "id": 2,
        "state": "EXECUTED",
        "date": "2023-01-01",
        "amount": 500,
        "currency_name": "USD",
        "currency_code": "USD",
        "description": "Перевод",
        "from": "Card",
        "to": "Account"
    }

    result = normalize_transaction(transaction)

    assert result["amount"] == 500.0
    assert result["currency_code"] == "USD"
