#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jenileejao

Lecture 3: 
    - Lists:
        - +=
        - extend
        - insert
        - del
    - Tuples
        - len
        - slicing
"""

''' previous, talked about list
    we used append method to add data
    but what happens if we have more than 1 list
    and we want to add that list together    
'''

first_list = [1, 2, 3]
second_list = [4, 5, 6]
third_list = [7, 8, 9]

total = first_list + second_list ###but won't it add the values?

''' actually for lists, it's similar to what we did 
    for the strings, it will concatenate them
    so first_list and second_list will be concatenated
    and will be stored in total
'''

''' 
    another way is to use the += operator
    so for the third_list let's try to apply that
    currently the value for total 
    is the concatenated first and second list
    and we want to add the third_list to it    
'''

total += third_list
print(total)


''' while append and += operator adds data
    we also have another one which is the extend and insert method
'''

total.extend([ 11, 12 ])

'''but wait i want to add the value 0 at position 0'''

total.insert(0, 0) # (index, value)

'''oh wait when i extended the list i forgot 10'''

total.insert(10, 10)

print(total)

'''but I think I added too many values
    so i want to remove zero
'''

del total[0] #delete is a keyword and not a method, deletes the first index
del total[-1] #delete last element

print(total)

### tuples

'''
    collection datatype that is ordered and immutable
    which means it's constant
    same with list with the difference being tuples
    cannot be changed after its creation
'''

someTuple = ("Arya", "11", "Winterfell")

print(someTuple)

'''
    we can actually remove the parenthesis and it's still a tuple
'''

'''
    but if you want just one element inside the tuple,
    even it's inside the partenthesis, you'll still need
    a comma
'''

not_a_tuple = ("Stark")
print(type(not_a_tuple)) #string, not tuple

a_tuple = ("Jon",)
print(type(a_tuple))

''' you can also create a tuple from the built in tuple function
'''

anotherTuple = ('eggs', '2', 'scrambled')
print(anotherTuple)

'''
    if you want to access the elements,
    we can do this by referring to the index
'''

breakfast = anotherTuple[0]
print(breakfast) #change index to 1, 2, 3(larger), -1 etc

'''
    what happens when we want to change the elements inside the tuples
'''

#someTuple[1] = "18" #not possible because tuple is immutable

thingTuple = ('a', 'p', 'p', 'l', 'e')

print( len(thingTuple))

print( thingTuple.count ('p')) #try a, l, o(not inside)

print ( thingTuple.index('p')) #returns first occurence

tuple_to_list = list(thingTuple) #convert tuple to list

print(tuple_to_list)

list_to_tuple = tuple(tuple_to_list) #convert list to tuple

print(list_to_tuple) 

### tuple slicing

x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

y = x[2:5]
z = x[::-2]

print(y)
print(z)


#someTuple = ("Arya", "11", "Winterfell")

name, age, location = someTuple

print(name)
print(age)
print(location)

''' just remember, the number of elements should match 
    name, age, loc, must match arya 11 winterfell
    
    try removing location and see error
'''

i1, *i2, i3 = x

print(i1)
print(i3)
print(i2)







