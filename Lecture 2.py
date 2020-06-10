#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jenilee

Lecture 2: 
    - String Slicing
    - Functions on strings: len(length), split, join
    - Lists
    - List len, list slicing
"""

###string slicing


''' talk about index counting here '''

someString = 'Hello World !' #12 indices but length of 13

""" if I want to slice the whole string """

anotherString = someString[:] #if blank, uses default
''' we're gonna use a square bracket and separate with a colon
    if it's empty, it means we will slice from beginning to end
'''

''' another way to write it is this '''
another_String = someString[0:13] 

''' notice that length is 13, not 12 '''

# string[start = 0 : end = len(string) : step = 1] --these are default
''' start is inclusive and end is exclusive '''


worldString = someString[6:] #start at index six until the end 

print(anotherString)
print(another_String)
print(worldString)

helloString = someString[:5] #start at beginning until index 4

print(helloString)

thingString = someString [3:9] #starts at index 3 and end at 8

print(thingString)
''' whatever lo Wor means '''

''' now let's talk about the step
    default as mentioned above is step of 1
'''

'''let's make a variable '''

name = "RGievriaalntof"

''' well this doesn't make sense '''

firstName = name[1:12:2] #start at 1, end at 11 and skips every other letter
middleName = name[-2:] #start at 2nd to last til end with step of 1
lastName = name[:10:2] #want to grab every other letter from 0 to 9


print(firstName, middleName, lastName)
''' ha look at that, it sliced correctly '''

''' there's a lot of ways to do string slicing
    and it's really up to you on how you want to do it
'''

'''let's talk about functions of strings'''

###string length
'''grabs length of the string'''

print( len(name) )

'''what about the other variable'''
print( len(someString) )


''' now I know I have Hello and World 
    but what if I want to combine both of these
'''

'''let's make another variable'''

'''type sepString = someString.split and show them the
    window prompt for whitespace
'''

sepString = someString.split()

print(sepString)

'''one thing you might notice is that it didn't print a string
    here, it printed a list and that's what we're gonna talk about
    in a bit
    as you can notice, it separated the strings based on the space
    into three different strings
'''


'''but then wait, what if I want to join the strings'''

'''another function we can use is join
    so now that our string is separated, 
    we can use the join method, 
'''

reunitedString = " ".join(sepString)
''' so what join will do is that it takes the string
    which is the space and this will be inserted
    in between each item inside of sepString
    so the join will take this space string
    and insert it in every item, which in this case
    is hello world and !
    and we're gonna make it one string
'''

print(reunitedString)



### Lists ###

'''
    lists are probably the datatype that you're gonna use most
    when you program in python and that's bec they are amazing
'''

'''
    one analogy that we can use to describe lists
    is a general linked list, which means that
    you can add at the beginning, the end and the middle
    or take of items on a list at the beg, end and middle
'''

''' list in python can contain elements of different data types 
    and not only that, it can also contain itself
'''

#two ways to create empty list and ill call it very cleverly
empty_list = list() #method 1 use the list keyboard
'''again i'll very cleverly call it'''
another_empty_list = [] #method 2

'''what if I want to put contents with different datatypes'''
random_things = [ 5, "volts", 8.72, [ "Another", "list" ] ] #quite clever

print(random_things)


### list length

'''len will work the same as with strings
    but it doesn't know that the last list
    have 2 elements
    so while we see 5 items, it will only see 4
    and so you're missing one item, which is something to consider
''' 

print( len(random_things) ) #doesn't know another list has 2 elements


### list slicing

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
odds = numbers[::2] #beginning to end and skip every other one
evens = numbers[1::2] #index one, which is value 2 and skip as well

print(odds)
print(evens)


'''what if I wanna be more ambitious'''
rev_odds = numbers[-2::-2] #2nd to last, inclusive, til end, step backwards

'''ill get a bit more lazy'''
rev_evens = evens[::-1] #go through entire list with a reverse step of 1

print(rev_odds)
print(rev_evens)

'''what happens when I want to add data at the end
    let's say i wanna add 10 at the end of evens
    so ill call a method called append
'''
evens.append(10)

'''then for odds, let's say i want to even out the odds haha'''
odds.append(11)

print(odds)
print(evens)


