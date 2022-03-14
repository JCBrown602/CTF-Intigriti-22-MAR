# ENCRYPT.py

from sympy import isprime, prime

flag = '{tacotacotaco}'

def Ord(flag):
    x0r([ord(i) for i in flag])
    
def x0r(listt):
    ff = []
    for i in listt:
        if isprime(i) == True:
            ff.append(prime(i) ^ 0x1337)
        else:
            ff.append(i ^ 0x1337)
    b1n(ff)

def b1n(listt):
    ff = []
    for i in listt:
        ff.append(int(bin(i)[2:]))
    print(ff)
    
if __name__ == "__main__":
    Ord(flag)

'''
 OUTPUT :
[1001100000110, 1001100000100, 1001100000100, 1001100000000, 1001101100010, 1001101100111, 1001101001100, 1001101001111, 1001100000111, 1001101000101, 1001101101000, 1001100000011, 1001101011001, 1001101110011, 1001101101000, 1001101110101, 1001101011110, 1001101011001, 1001100000011, 1001011001010, 1001101100101, 1001101001110, 1001101101000, 1001101110010, 1001101011001, 1001001111100, 1001100000111, 1001101010011, 1001100000100, 1001101000101, 1001101101000, 1001100000011, 1001101000101, 1001100000100, 1001101101000, 1001101000011, 1001101111111, 1001100000100, 1001101101000, 1001101100000, 1001100000100, 1001100000011, 1000101111100, 1001100000100, 1001111000110, 1001101000011, 1001101101000, 1001100001111, 1001100000111, 1001100000000, 1001100001110, 1001100000111, 1001100000000, 1001111000110, 1001100000001, 1001101001010]
'''

