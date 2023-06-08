import hashlib 
from src.check_input import hash_password

def test_hash_password():
    password = "password123"
    expected_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    assert hash_password(password) == expected_hash
    
    empty_password = ""
    expected_empty_hash = hashlib.sha256(empty_password.encode("utf-8")).hexdigest()
    assert hash_password(empty_password) == expected_empty_hash
    
    special_password = "!@#$%^&*"
    expected_special_password = hashlib.sha256(special_password.encode("utf-8")).hexdigest()
    assert hash_password(special_password) == expected_special_password