#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jenilee

Lecture 2: 
    - String Slicing
    - Functions on strings: len, split, join
    - Lists
    - List len, list slicing
"""

#string slicing

# string[start = 0 : end = len(string) : step = 1]
# start is inclusive and end is exclusive

''' talk about index counting here '''

someString = 'Hello World !' #12 indices but length of 13
anotherString = someString[:] #if blank, uses default
#anotherString = someString[0:12]
worldString = someString[6:] 

print(anotherString)
print(worldString)

helloString = someString[:5]

print(helloString)

thingString = someString [3:9]

print(thingString)

name = "RGievriaalntof"

firstName = name[1:12:2]
middleName = name[-2:]
lastName = name[:10:2]

print(firstName, middleName, lastName)


#string length

print( len(name) )
print( len(someString) )

sepString = someString.split()
print(sepString)

reunitedString = " ".join(sepString)
print(reunitedString)

""" Lists """

empty_list = list()
another_empty_list = []
random_things = [ 5, "volts", 8.72, [ "Another", "list" ] ]

print(random_things)
print( len(random_things) ) #doesn't know another list has 2 elements

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
odds = numbers[::2]
evens = numbers[1::2]

print(odds)
print(evens)

rev_odds = numbers[-2::-2]
rev_evens = evens[::-1]

print(rev_odds)
print(rev_evens)

evens.append(10)
odds.append(11)

print(odds)
print(evens)


