# P03. REQ : String Slicing  # 11
'''                                               12345
Usage:
--------
Operators    : +=
DM / Loops   : For Loop
Data structure: STRING INT
'''

# 0. Mathematics
# Implement the solutions in white paper
"Hello World"
'''
Maths:                            Programming Language:
==========================        ============================= 
1. Write it on paper              1. Define string 
                                     str1 = 'Hello World'
2. Traverse through each char     2. Use for loop to iterate through each char
3. Assign the value for each      3. counter = 0. Increment in each iteration
   character                         Operators / Decision Making / Loops
'''

# 1.Builtin functions

print("-----1. Built Functions--------")

msg = input("Enter any string : ")

m = int(input('Enter the starting index: '))

n = int(input('Enter the ending index: '))

if m < n < len(msg):
    print(f'The sliced part of the string between {m} and {n} positions is {msg[m:n]}')
else:
    print('Please enter valid index values!')


# 2. Algorithm ***

print("--------2. Algorithm----------")

msg = input("Enter any string : ")

m = int(input('Enter the starting index: '))

n = int(input('Enter the ending index: '))

if m < n < len(msg):
    print(f'The sliced part of the string between {m} and {n} positions is: ')
    for i in range(m, n):
        print(msg[i], end='')

else:
    print('Please enter valid index values!')

# 3 Using Functions  ==>   40

print("--------3 Using Functions----------")


def slicing(string, x, y):

    if x < y < len(string):
        print(f'The sliced part of the string between {x} and {y} positions is: ')
        for j in range(x, y):
            print(string[j], end='')

    else:
        print('Please enter valid index values!')


msg = input("Enter any string : ")

m = int(input('Enter the starting index: '))

n = int(input('Enter the ending index: '))

slicing(msg, m, n)

# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")
# 5 Exception handling  ==> 5
print("--------5 Exception handling----------")
# 6 File Handling  ==> 5
print("--------6 File Handling----------")
# 7 Database interaction MVC  ==> 2
print("--------7 Database interaction----------")
# 8 UI Interaction   ==> 2
print("--------8 UI Interaction----------")
