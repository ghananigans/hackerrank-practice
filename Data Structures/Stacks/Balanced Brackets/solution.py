#!/bin/python3

import sys

def check_brackets(brackets):
    data = list()
    
    for b in brackets:
        if b == '{':
            data.append(b)
        elif b == '[':
            data.append(b)
        elif b == '(':
            data.append(b)
        elif b == ')':
            if len(data) == 0 or data[-1] != '(':
                return False
            
            data.pop()
        elif b == ']':
            if len(data) == 0 or data[-1] != '[':
                return False
            
            data.pop()
        elif b == '}':
            if len(data) == 0 or data[-1] != '{':
                return False
            
            data.pop()
        else:
            assert(false)
    
    return len(data) == 0


t = int(input().strip())
for a0 in range(t):
    s = input().strip()
    
    print_result = "YES" if check_brackets(s) else "NO"
    print(print_result)

