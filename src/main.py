from pathlib import Path

from src.readers import read_csv, read_excel
from src.services import format_transaction, process_bank_search
from src.utils import read_json_file


def main() -> None:
    """Основная логика программы."""

    print(
        "Привет! Добро пожаловать в программу работы "
        "с банковскими транзакциями."
    )

    print(
        "\nВыберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    choice = input("\nВведите номер пункта: ")

    if choice == "1":
        print("Для обработки выбран JSON-файл.")

        file_path = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "operations.json"
        )

        transactions = read_json_file(str(file_path))

    elif choice == "2":
        print("Для обработки выбран CSV-файл.")

        transactions = read_csv("data/transactions.csv")

    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")

        transactions = read_excel("data/transactions_excel.xlsx")

    else:
        print("Неверный пункт меню.")
        return

    print(f"Загружено транзакций: {len(transactions)}")

    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print(
            "\nВведите статус, по которому необходимо выполнить фильтрацию."
        )
        print(
            "Доступные для фильтровки статусы: "
            "EXECUTED, CANCELED, PENDING"
        )

        status = input().upper()

        if status in available_statuses:
            break

        print(f'Статус операции "{status}" недоступен.')

    filtered_transactions = [
        transaction
        for transaction in transactions
        if transaction.get("state", "").upper() == status
    ]

    print(f'Операции отфильтрованы по статусу "{status}"')

    sort_by_date = input(
        "\nОтсортировать операции по дате? Да/Нет: "
    ).lower()

    if sort_by_date == "да":
        sort_order = input(
            "Отсортировать по возрастанию или по убыванию? "
        ).lower()

        reverse = sort_order == "по убыванию"

        filtered_transactions.sort(
            key=lambda transaction: transaction.get("date", ""),
            reverse=reverse
        )

    rub_only = input(
        "\nВыводить только рублевые транзакции? Да/Нет: "
    ).lower()

    if rub_only == "да":
        filtered_transactions = [
            transaction
            for transaction in filtered_transactions
            if transaction.get("currency_code") == "RUB"
        ]

    search_by_description = input(
        "\nОтфильтровать список транзакций по определенному "
        "слову в описании? Да/Нет: "
    ).lower()

    if search_by_description == "да":
        search = input(
            "Введите слово для поиска в описании: "
        )

        filtered_transactions = process_bank_search(
            filtered_transactions,
            search
        )

    if not filtered_transactions:
        print(
            "\nНе найдено ни одной транзакции, подходящей "
            "под ваши условия фильтрации."
        )
        return

    print("\nРаспечатываю итоговый список транзакций...")
    print(
        f"\nВсего банковских операций в выборке: "
        f"{len(filtered_transactions)}\n"
    )

    for transaction in filtered_transactions:
        print(format_transaction(transaction))
        print()


if __name__ == "__main__":
    main()
