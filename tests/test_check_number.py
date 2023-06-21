from unittest.mock import patch
from src.check_input import check_number

def test_check_number_with_valid_input():
    with patch('builtins.input', return_value='123'):
        assert check_number('int') == 123

    with patch('builtins.input', return_value='3.14'):
        assert check_number('float') == 3.14
    
    
def test_check_number_with_invalid_input():
    with patch('builtins.input', side_effect=['abc', '123']):
        assert check_number('int') == 123

    with patch('builtins.input', side_effect=['xyz', '3.14']):
        assert check_number('float') == 3.14
