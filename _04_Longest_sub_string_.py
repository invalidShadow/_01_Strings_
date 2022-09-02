# P04. REQ : Longest sub-string  # 11
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

print(f'Length of the longest substring \'{max(msg.split(), key=len)}\' is {len(max(msg.split(), key=len))}')


# 2. Algorithm ***

print("--------2. Algorithm----------")

msg = input("Enter any string : ")

lst = [x for x in msg.split()]

lengths = []

count = 0

for ele in lst:
    for i in ele:
        count += 1
    lengths.append(count)
    count = 0

max_length = 0

for i in range(1, len(lengths)):
    if lengths[i] > lengths[i-1]:
        max_length = lengths[i]
    else:
        max_length = lengths[i-1]

print(f'The length of the longest substring is {max_length}')


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
