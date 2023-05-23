from src.check_input import check_date

def test_check_date_success(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2023-5-21")
    assert check_date() == "2023-5-21"


def test_check_date_error(monkeypatch):
    # Create a list with all the inputs
    inputs = ["2023/5/21", "21-5-2023", "5-21-2023", "2023-64-21", "2023-5-64"]
    index = 0
    
    def mock_input(_):
        nonlocal index
        value = inputs[index]
        index += 1
        return value
    
    monkeypatch.setattr('builtins.input', mock_input)
    assert check_date() is None