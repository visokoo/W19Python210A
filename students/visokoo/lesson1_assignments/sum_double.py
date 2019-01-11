'''
----------------------------------------------------
Assignment: Python Push Ups - Warmup Part 1 - sum_double.py
Author: visokoo | Created: 1/9/2019
ChangeLog: 1/9/2019, Created file 


Given two int values, return their sum. Unless the two values 
are the same, then return double their sum.


sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
----------------------------------------------------

'''

def sum_double(a, b):
  if a == b:
    return ((a + b) * 2)
  else:
    return a + b
