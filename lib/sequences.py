#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = getfib(length)
    print(fibonacci_list)

def getfib(length):
    fibonacci =[]
    for i in range(0,length):
        if i == 0 or i == 1:
            fibonacci.append(i)
        else:
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci
