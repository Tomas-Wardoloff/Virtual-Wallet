from src.check_input import check_len_user_input

def test_check_len_user_input_success(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "UserName")
    assert check_len_user_input("") == "UserName"
    
def test_check_len_user_input_shorter(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Er")
    assert check_len_user_input("") is None
    
def test_check_len_user_input_longer(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "InvalidLenghtInputOverFiftyXXXXXXXXXXXXXXXXXXXXXXX")
    assert check_len_user_input("") is None