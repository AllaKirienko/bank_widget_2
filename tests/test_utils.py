from src.utils import read_json_file


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
