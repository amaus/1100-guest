from primes import is_prime

def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(692) == False
    assert is_prime(2000) == False
    assert is_prime(1000000439) == True