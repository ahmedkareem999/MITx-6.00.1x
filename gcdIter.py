'''
Week-2:Exercise-gcd Iter
The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.
'''
#code
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a == b:
        return a
    elif a > b :
        i = b
        while i <= a and i >= 2:
            if a % i == 0 and b % i == 0:
                return i
                break
            else:
                i -= 1
        return 1
    else:
        i = a
        while i <= b and i >= 2:
            if b % i == 0 and a % i == 0:
                return i
            else:
                i -= 1
        return 1
