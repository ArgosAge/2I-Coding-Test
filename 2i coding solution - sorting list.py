# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:03:29 2023

@author: omg70_000
"""


def list_sort_no_duplicate(num_list):

    """
    function takes in a list of numbers and returns a new sorted list in 
    descending order with no duplicates, additionally checks input type 
    """

    # checks if input is a type of list
    if isinstance(num_list, (list,tuple,set,dict)) != True:
        return("Input is not a list type")
    
    # initialise counter 
    count = 0
    
    # check if each element is a float or an integer
    for num in num_list:
        if isinstance(num, (float,int)) != True:
            return("Element %d in list is not a float or an integer"%count)

        count += 1

    # use set to remove duplicates and sorted func to sort and return as list
    return sorted(set(num_list),reverse=True) 
            