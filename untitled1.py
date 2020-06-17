#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 09:39:19 2020

@author: jenileejao
"""

'''
finally lets discuss modules in reference ot classes
sometimes these are confused
either because of the notation were using
or sometimes because the module contains just one class
and sometimes seem synonymous

remember module is a file that contains a python code
and a class is just python code

in this somewhat confusing example,
the designers of the decimal class 
decided to name the module decimal
and the class that's inside the module as decimal

so that's why were able to say from decimal import Decimal

in this example, case really matters

so the lower case d is the module and the uppercase D 
is the class thats inside the module 

as weve talked aobut yesterday, a name of the class
starts with a capital letter

thats a standard python convention

as weve talked about, we can import certain variables of a module
using thing form 
from decimal import decimal

were sayin from the decimal module import the decimal class

and now were using the decimal class the way its intended to be used

'''

from decimal import Decimal

print Decimal('3.5') + Decimal('3.5')