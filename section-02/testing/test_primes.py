from primes import *

def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(37) == True
    assert is_prime(39) == False
    assert is_prime(103) == True
    assert is_prime(21577) == True
    assert is_prime(1000000007) == True
