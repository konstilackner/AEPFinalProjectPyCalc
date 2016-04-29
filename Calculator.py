# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 13:17:46 2016

@author: Konstantin
"""

# Understands how to do mathematical operations on numbers
class Calculator:
    
    def __init__(self, amount):
        self.amount = amount
        
    def add(self, i):
        return self.amount + i
    
    def multiply(self, i):
        return self.amount * i
        
    def divide(self, i):
        return self.amount / i
        
    def square(self):
        return self.amount ** 2