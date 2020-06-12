#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jenileejao

Lecture 4:
    - Loops
    - for loops
    - while loops
    - range function
    - list comprehensions
"""

breakfast = [ "pancakes", "bacon", "syrup", "coffee" ]

print(breakfast)

''' it looks messy and not really pleasing to the eyes
    so why don't i use a for loop to iterate the entire
    contents of the list
'''

for i in breakfast: ###so what does it mean? for each item in breakfast array
    ''' so this is gonna iterate from the start to end of bfast list
        in keyword will specify and do all the hard work
        to sure this for loop iterates from beginning to end of list
    '''
    print(i, end=' ')

print("")

''' how do we know what's inside the for loop
    as you notice, it's indented
    so whatever is indented after the for i in breakfast
    will be included in that for loop and same with other for loops
'''

''' so we know that line 28 is not inside the for loop
    we begin our for loop after the (:)
    so it looks much better now
'''

''' there's another way of printing this for loop too
'''

for j in range( len(breakfast) ): ###we can cover range later
    print(breakfast[j], end=' ')
print("")

for k in range( len(breakfast) ):
    print(k, end=" ") ###this is just to see the content of range but again
    ### we'll cover this in more detail later

''' what we end up with is the same as i bec
    as you can see breakfast[j] will start at zero
'''

''' and it makes sense because as you can see, 
    k starts from 0, 1, 2, 3
''' 

''' you can use for loops to see the contents of your array
    or to do something repeatedly, which we'll do later
'''


### while loops

''' if id like to print number bet 1-10 using while
'''

print('') ### don't put this yet, put this after while loop

count = 1                           
                        ### start """
while count < 11:                   
                        ### end """
    print(count, end=" ")           
                        ### body """
    count += 1 #manually add to count to reach the end condition 
    ### step """
    
    
### nested for loop

''' obejctive row of squared numbers from 1 to 10
'''

''' reset count to 1
'''
print('')
count = 1
while count < 11:
    ### set up second condition for inner while loop
    ### so that i can multiply count number
    ### with another number which is itself
    ### mult as coefficient to multiplier count and set it equal to count
    mult = count
    while mult == count: #inner while loop
        print(count * mult) 
        mult += 1 #stepping condition
    count += 1 ##inside first while loop


### range function
    
#for i in range( len(breakfast) ): ###we can cover range later
 
''' range works in a few ways
    range( stop ) === start from 0 and go up til stop condition minus 1
    range( start, stop ) === start from # until stop minus 1
    range( start, stop, step ) === same with string slicing
'''

print( range(5) )   ### if you only give stop, it's implicit that
                    ### it starts from 0 

''' but notice it did't print it in a list
    when we printed it on a for loop, we saw 0 to 4
    so why don't we make this a list
'''

a = list( range(5) )
print(a)

'''now lets use the second conditoin
'''

b = list( range(8, 17) )
print(b) 

''' so it starts at 8 and keep incrementing by 1
    up until 16, notice how it doesn't stop at 17
'''

### inclusive beginning but exclusive ending
### which means it will include the start 
### but exclude the ending we provide

''' so now let's use step
'''

c = list( range(4, 25, 2 ) ) ### skip every other one
print(c)

''' range is a class and it returns a range class
    but when we use it in for loops of cast it as a list,
    it is used as a list class'''
    
''' this brings us to our next topic
'''


### list comprehension

''' as you can see, a, b, c, they create list but it doesn't give us
    that much control on how we can create the list
    
    let's say i wanna have a list from the range of 4 to 25
    with every other number taken
    but i wanna multiply each number by 2
    well i can't do it with just the list function
    
    so there is a solution to this and it's called list comprehesion
    
    so what if we create something similar to c
    but every value multiplied by 2
'''

d = [i * 2 for i in range(4, 25, 2) ]
''' this will create a list just like c except every element
    is gonna be multiplied by 2
'''

print(d)

'''
    this is called list comprehension
    it's when you use for loop just in one line
    to create a list of values
    
    similar to range function and casting it as a list
    but for here we have a little more control
    bec were using a combi of range and for loop to create a list
    and we're able to exercise more control
    bec we're able to modify (i) for (i) in range

    if id like to, another way of doing it is
'''

# exponentiation operater

e = [ j ** 2 for j in range(10, 0, -1) ]
''' we'll get a series of squared numbers from 1 squared to 10 in reverse
'''
print(e) 





























