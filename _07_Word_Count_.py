# P01. REQ : Find length of given string   ie., "Hello World"  # 11
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
   'Hello World'                     str1 = 'Hello World'
2. Traverse through each char     2. Use for loop to iterate through each char
3. Incrementing count value       3. counter = 0. Increment in each iteration
                                      Operators / Decision Making / Loops
'''

# 1.Builtin functions

print("-----1. Built Functions--------")

msg = input("Enter any string : ")

print(f'The number of words in the given string is {len(msg.split())}')

# 2. Algorithm ***

print("--------2. Algorithm----------")

msg = input("Enter any string : ")

count = 0

for ele in msg:
    if ele == ' ':
        count += 1

print(f'The number of words in the given string = {count + 1}')

# 3 Using Functions  ==>   40

print("--------3 Using Functions----------")

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
