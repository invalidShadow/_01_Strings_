# P02. REQ : Find the number of characters in a given string  # 11
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

char = input('Enter the character you want to count: ')

print("Number of characters in the given string : ", msg.casefold().count(char))


# 2. Algorithm ***

print("--------2. Algorithm----------")

msg = input("Enter any string : ")

char_count = {}

for ele in msg.casefold():
    if ele not in char_count.keys():
        char_count[ele] = 1
    else:
        char_count[ele] += 1

print(f'The character count for the given string is {char_count}')

# 3 Using Functions  ==>   40

print("--------3 Using Functions----------")


def char_count(string):
    char_count_dict = {}

    for ele in string.casefold():
        if ele not in char_count_dict.keys():
            char_count_dict[ele] = 1
        else:
            char_count_dict[ele] += 1

    return char_count_dict


msg = input('Please enter a string: ')

print(f'The character count for the given string is: {char_count(msg)}')

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
