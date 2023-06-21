from unittest.mock import patch
from src.check_input import check_len_user_input

def test_check_len_user_input_success(monkeypatch):
    with patch('builtins.input', return_value="UserName"):
        assert check_len_user_input(1, 8, '') == "UserName"
  
def test_check_len_user_invalid_input():
    with patch('builtins.input', side_effect=["LongerInput", "ValidInput"]):
        assert check_len_user_input(1, 10, '') == "ValidInput"
        
    with patch('builtins.input', side_effect=['ShorterInput', "ValidInputXXXX"]):
        assert check_len_user_input(13, 15, '') == "ValidInputXXXX"    
