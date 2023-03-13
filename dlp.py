from prime import is_probable_prime
from math import sqrt
import random


#Exercice 1
#Q1

def pgcd(a , b):
    max_i = max ( a, b)
    min_i = 1
    while a != 0 :
        min_i = min(a , b)
        a = max_i - min_i
        b = min_i
        max_i = max (a, b)
    return min_i
        

"""
def bezout(a, b):
    r0 = max(a,b)
    r1 = min(a,b)
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
    while r1 :
        q = r0 // r1
        r,r0 = r0 - q*r1,r1
        r1 = r
        u,u0 = u0 - q*u1 , u1
        u1 = u
        v, v0 = v0 - q*v1 , v1
        v1 = v
    return r0 , u0 ,v0
"""
def bezout(a, b):
    r1 = max(a,b)
    r2 = min(a,b)
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
    while r2 :
        print(r1, " " , r2)
        q = r1 // r2
        r1 , r2 = r2 , r1 - q * r2
        r0 = r1
        

        u2 = u0 - q * u1
        v2 = v0 - q * v1

        u0 = u1
        u1 = u2

        v0 = v1
        v1 = v2
    return r0 , u0 ,v0

#Q2
def inv_mod(a, n):
    return ( pgcd(a , n) == 1)


def invertibles(N):
    primes = []
    for a in range(1 ,N):
        if inv_mod(a, N) :
            primes.append(a)
    return primes


#Q3
def phi(N):
    return len(invertibles(N))


#Exercice 2
#Q1
def exp(a, n, p):
    binary_n = bin(n)[2:]
    res = 1
    for i in range(len(binary_n)-1,-1, -1):
        res =(res *res) % p
        if binary_n[i] == '1' :
            res = (res*a) % p
    return res



def premier (n) :
    if n == 0 or n==1 :
        return False
    for i in range(2 , n//2) :
        if (i % n) == 0 :
            return False
    return True

def list_premiers (n):
    primes = []
    for i in range(n+1) :
        if premier(i):
            primes.append(i)

    return primes

#Q2
def factor(n):
    r  = n
    primes = list_premiers(n)
    cpt = 0
    print(primes)
    factors = []
    y = 0
    x = primes[cpt]
    while(r!=1):
        print(factors ," ",r)
        if r % primes[cpt] == 0 :
            y += 1
            r = r // primes[cpt]
        else :
            if y != 0 :
                factors.append((x,y))
            cpt += 1
            y = 0
            x = primes[cpt]
    if y != 0 :
        factors.append((x,y))
    return factors


#Q3
def order(a, p, factors_p_minus1):
    return


#Q4
def find_generator(p, factors_p_minus1):
    return


#Q5
def generate_safe_prime(k):
    return


#Q6
def bsgs(n, g, p):
    return


print(bezout(21, 13))