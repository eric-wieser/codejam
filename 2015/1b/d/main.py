from __future__ import division
import sys
import math

which = 'sample'

sys.stdin = open('{}.in'.format(which))
sys.stdout = open('{}.out'.format(which), 'w')


def solve(counts):
	pass


t = int(raw_input())

for i in range(t):
	d = int(raw_input())
	counts = [int(c) for c in raw_input().split()]