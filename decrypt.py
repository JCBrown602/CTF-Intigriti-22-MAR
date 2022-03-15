# ENCRYPT.py

from sympy import isprime, prime

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]
codes = [4916, 4914, 4924, 4902, 4904, 4894, 4876, 4980, 4964, 4954, 4936, 5034, 4996, 5000, 5092, 5062, 4642, 4652, 4732, 4694, 4696, 4774, 4760, 4858, 4810, 4372, 4356, 4476, 4448, 4446, 4594, 4564, 4146, 4138, 4204, 4186, 4256, 4336, 4328, 5936, 5904, 5896, 6070, 6052, 6022, 6134, 5670, 5814, 5806, 5776, 5768, 5868, 5828, 5386]

flag = '<REDACTED>'
flagStr = '1001100000110, 1001100000100, 1001100000100, 1001100000000, 1001101100010, 1001101100111, 1001101001100, 1001101001111, 1001100000111, 1001101000101, 1001101101000, 1001100000011, 1001101011001, 1001101110011, 1001101101000, 1001101110101, 1001101011110, 1001101011001, 1001100000011, 1001011001010, 1001101100101, 1001101001110, 1001101101000, 1001101110010, 1001101011001, 1001001111100, 1001100000111, 1001101010011, 1001100000100, 1001101000101, 1001101101000, 1001100000011, 1001101000101, 1001100000100, 1001101101000, 1001101000011, 1001101111111, 1001100000100, 1001101101000, 1001101100000, 1001100000100, 1001100000011, 1000101111100, 1001100000100, 1001111000110, 1001101000011, 1001101101000, 1001100001111, 1001100000111, 1001100000000, 1001100001110, 1001100000111, 1001100000000, 1001111000110, 1001100000001, 1001101001010'

flagNums = flagStr.split(', ')
flagBin = map(int, flagNums)
flahg = []

# changes the flag from unicode chars to integers
def Ord(flag):
    x0r([ord(i) for i in flag])
    
def unOrd(flagNums):
    d3c(flagNums)

def x0r(listt):
    ff = []
    for i in listt:
        if isprime(i) == True:
            #ff.append(prime(i) ^ 0x1337)
            #ff.append(prime(i))
            ff.append(int(100))
        else:
            #ff.append(i ^ 0x1337)
            #ff.append(i)
            ff.append(int(333))
    b1n(ff)
    b1n2(ff)
    print('>TESTING...')
    d3c(ff)

def x1r(listr):
    ff = []
    #print type(listr[1])
    #print listr[1] + listr[2]
    for i in listr:
        try:
            if codes.index(i):
                #print ' FOUND!'
                flahg.append(primes.index(i))
            else:
                print ' NOT FOUND! '
        except:
            #print ' Not in the codes list. '
            flahg.append(i^0x1337)

    print flahg

    #for letter in flahg:
        #print chr(letter)

        #for code in codes:
         #   print ' code == ', code
          #  if i == code:
           #     print ' FOUND! ', i
            #else:
             #   s = (code^0x1337)
              #  print s
               # if s < 256:
               #     print chr(s)
               # else:
               #     print ' OVER 256! ', s
               #     print ' index ', codes.index(s)
               # print('---------')

            #print(i)
            #print(prime(i))
            #print(prime(i) ^ 0x1337)

            #print('+++')
            #a = i
            #x = prime(i)
            #y = 0x1337
            #z = (1/0x1337)
            #print "> x = prime(i): ", x
            #print "> y = 0x1337: ", y
            #print "> z = 1/0x1337: ", z
            #print "> x^y from original problem: ", x^y
            #print "> x^z should reverse it back to prime(i)", x^z
            #print "---"
            #print "> a = i: ", a
            #print "> a^y: ", a^y
            #print "> a^z: ", a^z
            #print "+++"
            #print(i)

def b1n(listt):
    ff = []
    for i in listt:
        ff.append(int(bin(i)[2:]))
    print(ff)

def b1n2(listt):
    ff = []
    for i in listt:
        ff.append(int(i))
    print(ff)
    
def uni(listr):
    ff = []
    for i in listr:
        s = str(i).decode("utf-8")
        ff.append(s)
    print(ff)

###########################################
def d3c(flagNums):
    ff = []
    for i in flagNums:
        y = int(i, 2)
        #y = i
        ff.append(y)
    dd3c(ff)

def dd3c(flagValues):
    ff = []
    z = (0x1337)
    y = (1/4919)
    for i in flagValues:
        #print ' i = ', i
        #print type(i)
        #print ' i^y = ', i^y
        x = int(i)
        ff.append(i^y)
    print '***'
    print(ff)
    print '***'
    x1r(ff)

if __name__ == "__main__":
    #Ord(flag)
    unOrd(flagNums)

'''
 OUTPUT :
[1001100000110, 1001100000100, 1001100000100, 1001100000000, 1001101100010, 1001101100111, 1001101001100, 1001101001111, 1001100000111, 1001101000101, 1001101101000, 1001100000011, 1001101011001, 1001101110011, 1001101101000, 1001101110101, 1001101011110, 1001101011001, 1001100000011, 1001011001010, 1001101100101, 1001101001110, 1001101101000, 1001101110010, 1001101011001, 1001001111100, 1001100000111, 1001101010011, 1001100000100, 1001101000101, 1001101101000, 1001100000011, 1001101000101, 1001100000100, 1001101101000, 1001101000011, 1001101111111, 1001100000100, 1001101101000, 1001101100000, 1001100000100, 1001100000011, 1000101111100, 1001100000100, 1001111000110, 1001101000011, 1001101101000, 1001100001111, 1001100000111, 1001100000000, 1001100001110, 1001100000111, 1001100000000, 1001111000110, 1001100000001, 1001101001010]
'''

