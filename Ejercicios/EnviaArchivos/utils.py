# coding=utf-8
import random

def binary(n):
    if(n == 0):
        return "0"
    b = ""
    while n != 0:
        b += str(n % 2)
        n /= 2
    return b[::-1]

def isPrime(n):
    i = n - 1
    while i > 1:
        if n % i == 0:
            return False
        i -= 1
    return True

def randZero(n):
    return random.randint(0, n)

def clean(url):
    clean = open(url, "w")
    clean.close()

def abs(x):
    if x < 0:
        return -x
    return x
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 