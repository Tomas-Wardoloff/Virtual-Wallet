from src.check_input import check_email

def test_check_email_success(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "username@example.com")
    assert check_email() == "username@example.com"

def test_check_email_error(monkeypatch):
    # Create a list with all the inputs
    invalid_emails = [
        "example.com", # missing @ symbol
        "test@.com", # missing domain name
        "test@example", # missing top-level domain
        "test@com" # missing dto separator
    ]
    index = 0
    
    def mock_input(_):
        nonlocal index
        value = invalid_emails[index]
        index += 1
        return value
    
    monkeypatch.setattr('builtins.input', mock_input)
    assert check_email() is None