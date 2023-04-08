A, B = map(int, input().split())

def eratosthenes_sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    until = int(n ** 0.5)
    for i in range(until + 1):
        if sieve[i] is True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False

    return [i for i in range(n + 1) if sieve[i] is True]


def is_prime(prime_number, n):
    count = 0
    for prime in prime_number:
        if n == 1:
            break

        while n % prime == 0:
            n = n // prime
            count += 1

    return count

def is_under_prime(number):
    if number == 1:
        return False

    until = int(number ** 0.5)
    for i in range(2, until + 1):
        if number % i == 0:
            return False
    return True


prime_number = eratosthenes_sieve(B)
answer = 0
for i in range(A, B+1):
    if is_under_prime(is_prime(prime_number,i)):
        answer += 1

print(answer)



