# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 11:21:34 2019

@author: Yosef
"""
'''

Question #6

Write a function called name_facts that will take a firstname (string) as an input parameter, 
and print out various facts about the name, including:
1) its length, 
2) whether it starts with the letter A, and 
3) whether it contains a Z or X. To gain full credit for this exercise,
 you must use string formatting to print out the result.

'''




def name_facts(name):
    
    name=name.lower()
    length= int(len(str(name))) 
    print(length)
    print(name)
    
    if name[0] == 'a':
        var= "does start with the letter A."
    else:
        var= "does not start with the letter A"
    if name == 'z' or ' x':
        var2= "and does contain a Z or X"

name_facts(input("Type your name please. "))

print("Your name is %s letters long, does not start with %s, and %s " % (length, var, var2))
