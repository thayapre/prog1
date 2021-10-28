# 1.4 - Compute Pi
#
from math import sqrt, factorial

n = 0
sum = 0


def last_term(n):
    return (1103 + 26390 * n) / 396 ** (4 * n)


while last_term(n) >= 1e-15:
    sum += (factorial(4 * n) / factorial(n) ** 4) * (last_term(n))
    n += 1


# 1/pi
result = (2 * sqrt(2) / 9801) * sum

# pi
print("pi computation: ", result ** (-1))
