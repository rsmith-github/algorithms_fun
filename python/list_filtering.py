import unittest

def filter_list(l):
    'return a new list with the strings filtered out'
    return [element for element in l if type(element) == int]
