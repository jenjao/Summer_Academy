#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jenileejao

Lecture 5:
    - if statements
    - if/else statements
    - elif statement
    - and/or logical operators
"""

value = 3

""" another case is something that is true or false """

thing = True 

''' sometimes in these python programs, you have instances where
    values might change and you don't know the exact outcome,
    how it's going to change
    so you need to check if your variables are meeting certain criteria.
'''

''' and the easiest way to do this is to use conditional statements,
    meaning an if statement
'''

''' so in this program, what we're gonna try out 
    is we're going to check if our value is equal to 3
    and if thing is true.
    so how are we gonna start that?
'''

''' so we start by checking with the if keyword
'''


if value == 9: ### after the colon, body of if statement starts
    print("Yay")
    
''' check if thing is true, 2 ways '''

if thing: ## if thing == True:
    print("True!")
    
if value == 3:
    print("Hooray")
    
if thing == True:
    print("Yas it's true")
    
''' so far, all our examples are if the statements are true
    but what if we want to do something that is not true
'''

''' so now we're going to use the else statement
    the else statement will be called under the condition that
    the if statement above it is false
'''

something = 9
another = False

if something == 4:
    print("Wohoo")
else:
    print("Boo")
    
if another == True:
    print("True True")
else:
    thing = True
    print("another is set to True")

''' explain how that works
'''

''' and again it's indented to denote that it's in the body of code
'''

''' idea is that I can write however many code I want in here
    as long as it's indented, it's part of that conditional
'''
    
this_line = True

if this_line == True:
    a = [ i for i in range(100) ]
    b = [ j * 8 for j in a ]
    print(a)
    print(b)
else:
    this_line = True
    print("this_line is set to true")   
    
''' so basically you can write anything inside these conditionals,
    as long as their indented.
    you can put loops, funciton calls,
    classes, lists and etc
'''

''' so here we printed using list comprehension
'''

''' so the idea that I want to exercise here is you can 
    do whatever you like
    the sky is the limit
'''

''' so the if statement is to evaluate the truthness of the statement
    sometimes you need to check the current state of the variable.
    if it's equal to a number
    or if a function result is equal to somehting
    or if it's valid,
    if stomething returns true, or is true as a result
    maybe you need to double check if the function executed successfully
'''

### !=
''' talk about == again and = as an assignment operator
'''

thingy = False

if thingy == True:
    print("Yay")
else:
    thingy = True
    print("thingy is set to True")

if thingy != False:
    print("Very Nice")



### elif
    
value = 15

if value == 65:
    print('Mission failed')
    
    ''' but there's another possibility that value
        could have another value and i want to 
        check that well, if it's not 65, it could be another value
        i don't want it to be an else statement because
        i need to check another specific case
        so not only should i check that value is 65
        but if it's not 65, I want to check antoher specific case
        and this type of problem can be solved by using
        the elif statement
    '''
elif value == 15:
    print("Mission successful")
    
    ''' if it's neither of these two, I want to do nothing.
    '''
    
    ''' change value to 65 and something that's not either
    '''
    
    ''' so the elif checks a secondary case if the if statement fails
        and the elif statement is specific, not general,
        while the else statement is general, 
        which brings me to the next topic
    '''
    
    ''' we've seen the if statement by itself,
        if and else together
        if and elif together
        but what about using all these together? is that valid?
        the answer is yes.
    '''
    
else:
    print("Mission status unknown")
    
    ''' go over if, elif and else for value is 5
        so since we have an else statement, we have a catch all
        if the value doesn't match the first two,
        that's why the else statement is general
    '''
    
    ''' so your next question might be, is this the maximum
        number of condition i can check?
        no, you can actually keep on using the elif statement
        indefinitely
    '''
    
    ''' insert to code:
        ### elif value == 8
            print("mission in danger")
            elif value == 5
            print("get to extraction zone")
            ###
        
        in theory, i can have as many elif as id like to 
  
    '''
    ''' first it checks the first if, then in order
        if you want to check for 5 before 8, you have to move that up
    '''

''' we've been checking for only 1 condition,
    that is not always going to be the case
    sometimes we need to check for two conditions at the same time
'''

val = 5
null = None ### nothing is happening, it's void, it's not valid

if val == 5 or null != None:
    print("I like pancakes")
    
    ''' check if value is 5 and none is not equal to none
        OR means either or both of them are true
    '''

if val == 5 and null == None:
    print("I like waffles")
    
    ''' AND is different to OR
    '''
    
    




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
