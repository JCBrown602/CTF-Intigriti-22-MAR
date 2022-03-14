
from sympy import prime, isprime

primes = []
codes = []
mids = []

for x in range(256):
    if isprime(x) == True:
        print '-------'
        print ' This is prime! ', x
        print prime(x)
        code = (prime(x) ^ 0x1337)
        print ' The code is: ', code
        decode = (code ^ 0x1337)
        print ' And back... ', decode
        primes.append(x)
        codes.append(code)
        mids.append(prime(x))
    else:
        print ' This is not: ', x

print primes
print mids
print codes
