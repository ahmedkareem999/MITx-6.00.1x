'''
Pset-1 problem-1
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
'''
count = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1
print("Number of vowels:" + str(count))


'''
Pset-1 problem-2
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''
count = 0
for n in range(len(s)):
    if s[n:n+3] == "bob":
        count += 1

print("Number of times bob occurs is:" + str(count))


'''
Pset-1 problem-3
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.
'''
maxlength = 0
current = s[0]
longest = s[0]

for i in range(len(s) - 1):
	if s[i+1] >= s[i]:
		current += s[i+1]
		if len(current) > maxlength:
			maxlength = len(current)
			longest = current
	else:
		current = s[i+1]
	i += 1
print("The longest substring in alphabetical order is:" + longest)
