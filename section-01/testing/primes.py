# generate_primes
# takes in an upper bound and prints all primes less than that bound

# is_prime
# take in a number and return true if prime, false otherwise
def is_prime(num):
    if num == 1:
        return False
    for d in range(2,num//2+1):
        # if the remainder of num / d is 0,
        # then num is divisible by d and is not prime
        if num % d == 0:
            return False
    # if there are no divisors, then num is prime
    return True
    