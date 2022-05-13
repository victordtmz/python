

from tkinter import N


def get_prime_factor(no):
    factors = []
    divisor = 2
    while divisor <= no:
        if no % divisor == 0:
            factors.append(divisor)
            no = no//divisor
        else:
            divisor += 1
    return factors

factors = get_prime_factor(630)
print(factors)

