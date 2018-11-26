'''
Python Tutorial 00 - Basic Syntax
Berlin Cosmopolitan School

Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace:

    https://en.wikipedia.org/wiki/Python_(programming_language)
'''


#0.1 Comments
#In computer programming, a comment is an annotation in the code itself. They are generally ignored by compilers and interpreters, So the computer is not able to see them. They are added with the purpose of making the source code easier for humans:

#This is an In-Line Comments

'''
This is a
Multi-Line
Comments
'''


#0.2 Variables
#In computer programming, a variable is a storage location in RAM (identified by a memory address) paired with an associated symbolic name (an identifier), which contains some known or unknown quantity of information referred to as a value. This separation of name and content allows the name to be used independently of the exact information it represents. Here few examples using differents data types (explained in the followings tutorials):

variable = 1
radius = 10.7
name = 'Mickey'
surname = 'Mouse'
collectionA = [100, 12, 13, 14]
collectionB = {'product': 'Coca Cola', 'price': 1.50}


#0.3 Sequence
#the ordered sequencing of successive commands is considered one of the basic control structures, which is used as a building block for programs. Every instruction composing the code will be executed from


#0.4 Indentation
#In computer programming, an indentation style is a convention governing the indentation of blocks of code to convey program structure. Here an example using complex control structures explained in the following toturials:

#Main Sequence/Context
collection = [100, 200, 300, 100, 101, 40, 50]
print("incoming collection", collection)

for item in collection:
    #2nd Level Sequence/Context
    if item > 100 == 0:
        #3rd Level Sequence/Context
        result = "good"
    else:
        #3rd Level Sequence/context
        result = "bad"

    #Back on 2nd Level Sequence
    print(result)

#Back on Main Sequence
print("-- end")
