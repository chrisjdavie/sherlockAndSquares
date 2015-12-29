'''
Solution of https://www.hackerrank.com/challenges/sherlock-and-squares.

Square integers between two numbers. Ought to be straight forwards.
'''
import math

T = input()

for _ in range(T):
    A, B = map(int,raw_input().split())
    a = int( math.ceil( math.sqrt(A) ) ) 
    b = int( math.floor( math.sqrt(B) ) ) + 1
    print b - a