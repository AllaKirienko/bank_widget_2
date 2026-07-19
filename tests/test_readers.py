from unittest.mock import Mock, patch

from src.readers import read_csv, read_excel


def test_read_csv() -> None:
    """Проверяет чтение CSV-файла."""
    mock_data = Mock()
    mock_data.to_dict.return_value = [{"id": 1, "amount": 100}]

    with patch("src.readers.pd.read_csv", return_value=mock_data) as mock_read:
        result = read_csv("data/transactions.csv")

    mock_read.assert_called_once_with("data/transactions.csv", sep=";")
    assert result == [{"id": 1, "amount": 100}]


def test_read_excel() -> None:
    """Проверяет чтение Excel-файла."""
    mock_data = Mock()
    mock_data.to_dict.return_value = [{"id": 1, "amount": 100}]

    with patch(
        "src.readers.pd.read_excel",
        return_value=mock_data
    ) as mock_read:
        result = read_excel("data/transactions_excel.xlsx")

    mock_read.assert_called_once_with("data/transactions_excel.xlsx")
    assert result == [{"id": 1, "amount": 100}]
