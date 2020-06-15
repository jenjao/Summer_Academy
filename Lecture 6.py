#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jenilee

Lecture 6:
    - Function
    - Classes
"""


''' A function is a set of statements that take inputs, 
    do some specific computation and produces output.
    Python provides built-in functions like print(), etc. 
    but we can also create your own functions. 
    These functions are called user-defined functions.
'''

''' A return statement is used to end the execution of the function call 
    and “returns” the result (value of the expression following 
    the return keyword) to the caller.
    If the return statement is without any expression, 
    then the special value None is returned.
'''


''' quadratic formula and making it a function
'''

''' we'll have three inputs, which are singular values
    and there's a possibility that it could return one value
    or it could return a list
'''

''' because i'm going to be calculating the quadratic formula
    i'm going to have to use a sqrt function
    but I don't really want to write my own sqrt function
    so what i can do is I can import the math.py library
    which already have a sqrt function
'''

from math import sqrt

''' to create a function, we can use def, or define keyword and give it 
    a name, i'll call this quad
'''

''' it'll have three inputs, a, b, and c  which should look familar
    for thos who have studied the algorithm.
'''


def quad(a, b, c):
    ''' so to begin, we have to calculate the discriminant
        of the quadratic formula to make sure it's not negative
        because we only want to calculate the roots 
        if their not imaginary
    '''
    
    dis = (b ** 2) - (4 * a * c)
    
    ''' 2 possibilities of discriminant
        greater than zero, real roots
        less than zero, imaginary roots and we don't want this
    '''
    
    ''' so because we have a condition, we are going to use
        a conditional statement.
    '''
    
    if dis < 0:
        print("Roots cannot be imaginary!")
        ''' because we're just letting the user know 
            that the roots cant be imaginary,
            we don't want to do anything
            so we just wnat to get out of here
        '''
        return None
        ''' so here i'm just returning a single value, which is none
        '''
    else:
        x1 = (-b + sqrt(dis)) / (2 * a)
        x2 = (-b - sqrt(dis)) / (2 * a)
        
        ''' what I want you to take note is the use of my parenthesis
            i want to be very very in control of 
            what kind of mathematical operations I want to do first
        
            so when doing mathematical operations in python,
            it will try to obey PEMDAS
            but when you have multiplication and division,
            it will do the operations from left to right
            so I use parenthesis for the mathematical operations
            that I want done first
            
        '''
        
        result = [ x1, x2 ] 
        ''' when this calculates, I want to create a list of the
            roots and store them into result
        '''
        
        return result
    

''' so now let's test it
    here im gonna create three variables
'''

x = 13
y = 20
z = 5

''' now im going to call my function and store it in
    a variable called roots
'''

roots = quad(x, y, z)

''' i want to check if it returns a list or none
'''

if roots: # if roots is not none
    print(roots)
   
    
''' but now let's try it when the function returns none
'''
       
z = 50

roots = quad(x, y, z)

if roots: 
    print(roots)

''' so since the discriminant is a negative number, it prints
    roots cant be imaginary
'''


### classes
''' constructor and destructor
'''

''' A class is a code template for creating objects. 
    Objects have member variables and have behaviour associated with them.
'''

class Point():
    ''' when making a class, somehting that you need to keep in mind
        is what happens when its created
        
        this is the role thats taken by the constructor
        the constructor is called at the beginning of life for the 
        class when its created
    '''
    
    def __init__(self): 
        ### 1 (self, x, y)
        ### 2 (self, x=0, y=0)
        ''' the constructor of all classes is done with 
            this keyword. so anytime you see this line,
            you know its a constructor for the class
            we can talk about self later
        '''
        
        print("Point is created")

        ''' so whats gonna happen when we reach 
            the end of life for this class
            well we have to call the destructor
        '''
        
        ### 1
        #self.x = 0 #do this later
        #self.y = 0
        
        ### 2
        #self.x = x
        #self.y = y
        
    def __del__(self): # delete
        print("Point is going to be destroyed")

    ''' init is where youre gonna have your functions
        and if you want to initialize your variables
        and delete is for cleaning up everything
        
        so if theres a connection over the network
        you want to disconnect or if theres some other
        communication that youre doing,
        heres where you want to stop it
    '''
    
p = Point() 

''' here i want to call the constructor 
    of point and assign it to p
    
    so lets call it
    
    and it says point is created
    well that doesnt seem too right
    
    so ill run it again, but this time,
    the constructor is created as well as the destructor
    
    and if we run it over and over, its going
    to create the constructor and destructor over and over
'''

''' so what does self mean? so in python self means
    the class thats calling these functions, so itself
'''

''' so here point itself is gonna call init and del
    self = current instance
    
    in terms of adding attributes, meaning variables that 
    belong to a class, how does one go about it
    
    well, lets say point is a 2D point
    
    so here we need x and y coordinates but I just cant do this
    
'''

### TYPE THIS AFTER DEF _INIT_ PRINT
### def __init__(self):
###        print("Point is created")
###        self.x = 0
###        self.y = 0
''' AFTER PRINT
    x = 0
    y = 0
    i cant just do this because here,
    these are locally created variables
    so what ill have to do to make them attributes
    is to prefix them with the SELF variable
    
    SO: 
    self.x = 0
    self.y = 0
    
    the current instance that calls this constructor
    in itself is gonna have its own internal variables here
''' 
        
''' so now if i'm gonna do something like:
'''

print(p.x, p.y)

''' so when point calls init, it puts itself as a variable
    and it sets its own attributes to zero
'''

''' so here, theres a problem with the constructor
    when I call the constructor, its always setting
    the values to zero
    
    maybe i want to set it to a different value
    and we should treat this as a function
'''

### TYPE THIS INSIDE __INIT__ AFTER SELF
###def __init__(self, x, y):
###        print("Point is created")
###        self.x = x
###        self.y = y
        
''' def __init__(self, x, y):
    then change 
    self.x = x
    self.y = y

    but this is no longer a default unparametarized constructor
    this is a default parametrized constructor
    
    
'''

''' python allows us a methodology of merging the two
    and that is the use of default arguments,
    
    here I can say that x = 0 and y = 0 (inside __init__ after self)
    I can provide default arguments to this
    
    so I can create point 
    ###the print(p.x, p.y) above
    and this is gonna be 0, 0
'''

###
### def __init__(self, x=0, y=0):
###        print("Point is created")
###        self.x = x
###        self.y = y

### last

'''then I wanna do p2 and p3 etc 
'''
'''    
p2 = Point(1)
print(p2.x, p2.y)

p3 = Point(3, 9)
print(p3.x, p3.y)
'''

''' p1
    so here im calling all three possible versions of this 
    constructor.
    one where theres no parameters, so both of these have 
    no parameters and its stored here
    
    p2
    here where only one of them is provided
    meaning that y will use the default parameter
    
    p3
    and here where none of the arguments will use the default parameter
'''


    
        
        
        
        
        
    
        
        
    
        
        
    









