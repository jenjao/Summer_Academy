# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:35:36 2020

@author: user
"""


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

''' 
    so here im calling all three possible versions of this 
    constructor.
    
    p1
    one where theres no parameters, so both of these have 
    no parameters and its stored here
    
    p2
    here where only one of them is provided
    meaning that y will use the default parameter
    
    p3
    and here where none of the arguments will use the default parameter
'''