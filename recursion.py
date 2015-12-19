#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 14 Recursion"""

def fibonacci(n):
    """
    Fibonacci Function
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
    """
    Euclid's Algorithm for Greatest Common Divisor
    """
    while b:
        (a, b) = (b, (a % b))
    return a

def compare_string(s1, s2):
    if (s1 and s2) == '':
        return 0
    elif len(s1) < len(s2):
        return len(s1) - 1
    elif len(s1) > len(s2):
        return len(s1) + 1
