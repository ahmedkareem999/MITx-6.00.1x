'''
Week-2:Exercise-Odd
Write a Python function, odd, that takes in one number and returns True when the number is odd and False otherwise.

You should use the % (mod) operator, not if.

This function takes in one number and returns a boolean.
'''
#code
def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    while x % 2 != 0:
        return True
        break
    
    return False
