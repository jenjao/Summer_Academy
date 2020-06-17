#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:26:05 2020

@author: jenileejao
"""

''' so now we have another file called mod.py
    where were importing mymodule
    and when were importing, we dont include the .py extension
    so here, lets import mymodule
'''


import mymodule #this will import mymodule.py

print (mymodule.thing) 

mymodule.someThing()

''' so here we're accessing thing and someThing through the mymodule name
    this is the standard way to execute an imported module
    the mymodule namespace hold the mymodule variables thing and someThing
'''