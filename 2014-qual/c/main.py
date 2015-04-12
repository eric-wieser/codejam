import sys
import math

sys.stdin = open('small.in')
sys.stdout = open('small.out', 'w')

def is_palindromic(x):
	return str(x) == str(x)[::-1]

def is_fair(x):
	s = int(math.sqrt(x))
	return s*s == x and is_palindromic(x) and is_palindromic(s)

def solve(a, b):
	return sum(is_fair(x) for x in range(a, b + 1))


n = int(raw_input())

for i in range(n):
	a, b = [int(x) for x in raw_input().split()]
	print "Case #{}: {}".format(i+1, solve(a, b))
