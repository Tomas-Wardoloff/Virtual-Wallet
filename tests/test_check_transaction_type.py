from src.check_input import check_transaction_type

def test_check_transaction_success(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "income")
    assert check_transaction_type() == "Income" 
    
    monkeypatch.setattr("builtins.input", lambda _: "expense")
    assert check_transaction_type() == "Expense" 
    
def test_check_transaction_error(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "NotATransactionType")
    assert check_transaction_type() is None 