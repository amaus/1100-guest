# generate_primes takes in an upper bound and outputs all
# primes less than that upper bound

# is_prime takes in a number and returns True if prime, False otherwise
def is_prime(num):
    if num == 1:
        return False
    for d in range(2, num//2 + 1):
        if num % d == 0:
            return False
    return True