from unittest.mock import patch

from src.external_api import convert_currency


def test_convert_rub():
    """Проверяет конвертацию рублей."""

    transaction = {
        "operationAmount": {
            "amount": "1000",
            "currency": {
                "code": "RUB"
            }
        }
    }

    result = convert_currency(transaction)

    assert result == 1000.0


@patch("src.external_api.requests.get")
def test_convert_usd(mock_get):
    """Проверяет конвертацию долларов."""

    mock_get.return_value.json.return_value = {
        "result": 9000
    }

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {
                "code": "USD"
            }
        }
    }

    result = convert_currency(transaction)

    assert result == 9000.0
    mock_get.assert_called_once()
