from src.check_input import check_currency

def test_check_currency_success(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "6")
    assert check_currency() == "CAD"
    
def test_check_currency_error(monkeypatch):
    # Create a list with all the inputs
    inputs = ["100", "-100", "NotANumber"]
    index = 0
    
    def mock_input(_):
        nonlocal index
        value = inputs[index]
        index += 1
        return value
    
    monkeypatch.setattr('builtins.input', mock_input)
    assert check_currency() is None
    