'''
Week-1: While Exercise -1
In this problem you'll be given a chance to practice writing some while loops.

1. Convert the following into code that uses a while loop.

print 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
'''
n = 2
while ( n >= 2 and n <=10):
    print(n)
    n += 2
print("Goodbye!")





'''
Week1: While Exercise-2
2. Convert the following into code that uses a while loop.

prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2
'''
n = 10
print ("Hello!")
while n <= 10 and n >= 2:
    print (n)
    n -= 2


    
'''
Week1:While exercise-3
3. Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:

21
which is 1 + 2 + 3 + 4 + 5 + 6.

For problems such as these, do not include input statements or define variables we will provide for you. Our automating testing will provide values so write your code in the following box assuming these variables are already defined.

'''
val1 = 0
val2 = 0
while val1 <= end:
    val1 += 1
    val2 = val2 + val1
    if val1 == end:
        print(val2)
