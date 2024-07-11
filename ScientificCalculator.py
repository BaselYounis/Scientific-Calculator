import math
import time

import numpy as np
from sympy import bernoulli
pi=3.1415926535897932384626433
def calculateFuncTime(func,input):
    start=time.time()
    func(input)
    end=time.time()
    elapsed=end-start
    return elapsed
def abs(x):
    if x >= 0:
        return x
    else:
        return -1*x
def factorial(n):
    if n==0:
        return 1
    if n==1:
        return 1
    product=1
    for i in range(1,n+1):
        product*=i
    return product
def power(x,n):
    product=1
    for i in  range(abs(n)):
        product*=x
    if n>=0:
        return product
    else:
        return 1/product

def ln(x,numberOfSeriesTerms=10):
    if x>1.5:
        return ln(x/1.5)+ln(1.5)
    if x<0.5:
        return ln(x*2)-ln(2)
    sum=0
    for i in range(1,numberOfSeriesTerms+1):
        if i%2==0:
            sum+=-1*power(x-1,i)/i
        else:
            sum += 1 * power(x - 1, i) / i
    return sum

def exp(x,numberOfSeriesTerms=10):
    if abs(x)>0.5:
        return power(exp(x/10),10)
    sum=0
    for i in range(numberOfSeriesTerms):
        sum+=power(x,i)/factorial(i)
    return sum
print(ln(100000000000000))
def sin(x,numberOfSeriesTerms=10):
    if x<0:
        return -1*sin(abs(x))
    if x>pi:
        return -1*sin(abs(x-pi))
    def sinHelper(x,numberOfSeriesTerms):
        sum=0
        for i in range(numberOfSeriesTerms):
            if i%2==0:
                sum+=1*power(x,2*i+1)/factorial(2*i+1)
            else:
                sum += -1 * power(x, 2 * i + 1) / factorial(2 * i + 1)
        return sum
    if abs(x)>=pi/2 and abs(x)<=pi:
        return sinHelper(pi-x,numberOfSeriesTerms)
    return sinHelper(x,numberOfSeriesTerms)
def cos(x,numberOfSeriesTerms=10):
    return sin(pi/2-x,numberOfSeriesTerms)

def tan(x,numberOfSeriesTerms=10):
    return sin(x,numberOfSeriesTerms)/cos(x,numberOfSeriesTerms)

def sec(x,numberOfSeriesTerms=10):
    return 1/cos(x,numberOfSeriesTerms)
def cosec(x,numberOfSeriesTerms=10):
    return 1/sin(x,numberOfSeriesTerms)
def cotan(x,numberOfSeriesTerms=10):
    return 1/tan(x,numberOfSeriesTerms)


