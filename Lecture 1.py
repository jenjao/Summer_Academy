# -*- coding: utf-8 -*-
"""
@author: Jenilee

Lecture 1: Introduction
    - comments
    - valid variable names
    - print function
    - numerical datatypes
    - letter-based datatypes
    - operations between datatypes
    
"""

''' Talk about datatypes first 
    - Classification that specifies which type of value 
      a variable has and what type of mathematic, relational 
      or logical operations can be applied to it 
      without causing an error.   
    
    Int 
    -	Short for “integer.”
    -	Numeric variable holding whole numbers
    -	E.g. 5, 20, 1999, 345789 and etc.

    Float 
    -	Short for “floating point.”
    -	Numeric variable holding floating decimal points.
    -	E.g. 3.4, 2.894, 5674.0001857 and etc.

    Double
    -	Similar to float but has double the amount of numbers after 
        the decimal point.
    
    String
    -	Used to represent a text rather than numbers.
    -	Comprised of a set of characters.
    -	Can also represent numbers if specified correctly.

'''

### HOW TO COMMENT ###
''' Comment:
    - text around your code but is never ran
      and generally ignored by the computer
    - used for documentation 
'''

# This is a single line comment

'''
This is a 
multi-line 
comment
'''

"""
This is also 

a multi-line 

comment
"""

### VALID VARIABLE NAMES ###
''' Variable:
    - Are names that are used to store values 
      to be referenced throughout your code
'''

''' Assignment:
    - Putting a value into a variable
    - x = 14, I'm assigning the number 14 to the variable x
'''

'''
contain: lower case, upper case, underscore, and numbers
start with: lower case, upper case, and underscore
'''

_under = 5 
Total87 = _under ** 2
lower_case = 'lower'


'''
- can't start with a number
- can't be a keyword
    - print
    - False
    - None 
    - True
    - and
    - class
    - finally
    - is
    - return
    - continue
    - for
'''

### print function ###
print('Hello World!')
'''
    talk about '' and "", they can be used interchangebly
    if they're in '' or "", then they print exactly
'''

'''
    but what if I want to print a value
'''

x = 14
y = 3.14

print(x)
print(y)
# print value for x and y in different rows
'''
notice that it printed the value of x and y, and not the letter itself
'''


print(x, y)
# print value for x and y in the same line

'''
    well wait, I want it to be separated by a comma
'''

print(x, y, sep=', ')
# print value for x and y with a separator



'''
now that we know how to print the values of the variable, 
we're now gonna talk about the operations between the datatypes
'''

### how numbers interact with each other ###

'''
we can also assign an operation to a variable
'''

z = x + y

print(z)


print(7/2) 
#floating point division


print(7//2) 
#works like an int datatype


#exponentiation operator
a = 3 ** 2
b = 3.1 ** 2
print(a)
print(b)
print('%.2f' %b) #print exact decimal place


'''
our examples have been assigning numbers to the variables 
and performing operations on integers and floats 
but what if I want to use a letter-based datatype

so now we'll talk about how to do all these to strings
'''
#letter-based datatype (strings)

'''
we can also assign strings to a variable
'''
s = 'Hello ' #single quotes and double quotes are interchangeable
t = "world!"

'''
we can also perform operations on strings
'''
u = s+t
print(u)
print(s+t)



