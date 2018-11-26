'''
Python Tutorial 01 - Basic Operators
Berlin Cosmopolitan School

Programming languages typically support a set of operators: constructs which behave generally like functions, but which differ syntactically or semantically from usual functions. Common simple examples include:
- arithmetic operators (+, -, /, *, %)
- comparison operators (<, >, <=, >=, ==, !=, equal, not equal)
- logical operators (and, or, not, xor, nand)
- value assigment to variables (=)
Languages usually define a set of built-in operators, and in some cases allow user-defined operators:

    https://en.wikipedia.org/wiki/Operator_(computer_programming)
'''


#1.1 Arithmetic Operators
#The basic arithmetic operations are addition, subtraction, multiplication and division. Those operations are implemented in any computer processor, wich contains a dedicated section called ALU (arithmetic and logic unit). Youcan say that the computer brain is able by default to solve those operations and interlace them together:

print("Arithmetic Expression 1:", 1 + 1 )
print("Arithmetic Expression 2:", 1 * 10 )
print("Arithmetic Expression 3:", 100 + 34/45 + (10/8)*4 )
print("Arithmetic Expression 4:", 30 - 34%45 + (8/3)*4 )


#1.2 Comparison Operators
#Comparison operators are used in logical statements to determine equality or difference between variables or values. The most common are eual to (==), not equal to (!=), less than (<), less than or equal to (<=), greater than (>), greater then or equal to (>=). As result they give a boolean number, so a value that can be True or False:
print("Comparison Expression 1:", 1 > 4)
print("Comparison Expression 2:", 2 < 100 )
print("Comparison Expression 3:", 2 == 3 )
print("Comparison Expression 4:", 2 == 2 )
print("Comparison Expression 5:", 2 != 1 )
print("Comparison Expression 6:", 2 != 2 )


#1.2 Logic Operators
#In logic, a logical operator is a symbol or word used to connect two or more sentences (of either a formal or a natural language) in a grammatically valid way, such that the value of the compound sentence produced depends only on that of the original sentences and on the meaning of the connective. In formal languages, like math or programming, those operators are applied to Boolean expression (mathematical expression using True and False as value, and providing a result in the same domain). We will approach only AND, OR and NOT:

#AND provides True only if both the incoming values are True
print("Truth Table AND:", True and True)
print("Truth Table AND:", True and False)
print("Truth Table AND:", False and True)
print("Truth Table AND:", False and False)

#OR provides False only if both the incoming values are False
print("Truth Table OR:", True or True)
print("Truth Table OR:", True or False)
print("Truth Table OR:", False or True)
print("Truth Table OR:", False or False)

#NOT provides the opposite state of the incoming value
print("Truth Table NOT:", not True)
print("Truth Table NOT:", not False)

#Input values in logic expressions may be comparison expresion results
a = 100
print("Inside the set (100, 200):", (a > 100) and (a < 200))
print("Inside the set [100, 200]:", (a >= 100) and (a =< 200))
print("Outside the set (100, 200):", not((a > 100) and (a < 200)) )
print("Outside the set [100, 200]:", not((a >= 100) and (a =< 200)) )
print("One of those values:", (a == 100) or (a == 200))
print("None of those values:", (a != 100) or (a != 200))


#1.1 Assignment
#n computer programming, an assignment statement sets and/or re-sets the value stored in the storage location(s) denoted by a variable name; in other words, it copies a value into the variable, from a user defined value, another variable or an expression result (that may also uses other variables):

#a variable can be set with a user-defined value
a = 1
print("a value:", a) #NOTE: a must be defined in order to be used
b = 2
print("b value:", b) #NOTE: b must be defined in order to be used

#a variable can be set with the result coming from an expression
result = (a+b)/b
print(result)

#a vaiable can use itself, getting the current state to evaluate the new one
result = result > 100
print(result)
