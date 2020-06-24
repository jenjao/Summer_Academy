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
        if theyre not imaginary
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





    
        
        
        
        
        
    
        
        
    
        
        
    









