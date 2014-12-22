#!/usr/bin/env python
from sys import argv
from stack import Stack

def matches(i, o):
   return (i == "{" and o == "}") or (i == "(" and o == ")") or (i == "[" and o == "]")

def balanced(input_string):
    parens = Stack()
    for char in input_string:
        if char in "({[":
            parens.push(char)
        elif char in ")}]":
            if parens.isEmpty():
                return False
            else:
                if not matches(parens.pop(), char):
                    return False
    return parens.isEmpty()

print balanced(argv[1])

