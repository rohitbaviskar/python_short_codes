def count_primes(num):
    prime_l = []
    prime_c = 0
    for x in range(2, num):
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            prime_l.append(x)
            prime_c += 1
        x += 1
    print(prime_l)
    return prime_c

print(count_primes(100))