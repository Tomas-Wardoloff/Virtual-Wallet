from src.check_input import check_number


def test_check_number_valid_float(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3.14")
    assert check_number("float", "Enter a float: ") == float("3.14")


def test_check_number_valid_integer(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")
    assert check_number("int", "Enter a integer: ") == int("5")
    
    
def test_check_number_invalid_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "InvalidInput")
    assert check_number("int", "Enter a integer: ") == None
    

def test_check_number_invalid_data_type(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "15")
    assert check_number("NotADataType", "Enter a integer: ") == None
