import os

import requests
from dotenv import load_dotenv


load_dotenv()


def convert_currency(transaction: dict) -> float:
    """Конвертирует сумму транзакции в рубли."""

    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    api_key = os.getenv("API_KEY")

    url = "https://api.apilayer.com/exchangerates_data/convert"

    params = {
        "to": "RUB",
        "from": currency,
        "amount": amount,
    }

    headers = {
        "apikey": api_key,
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
    )

    data = response.json()

    return float(data["result"])
