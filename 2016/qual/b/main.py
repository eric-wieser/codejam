import sys
import string

flip_trans = str.maketrans('+-', '-+')

def flip(stack, up_to=None):
	_, up_to, _ = slice(None, up_to, None).indices(len(stack))
	return stack[:up_to].translate(flip_trans)[::-1] + stack[up_to:]

def solve(stack):
	target = len(stack) * '+'
	n = 0
	print(stack, file=debug)
	while stack != target:
		if stack[0] == '-':
			up_to = stack.rindex('-') + 1
			stack = flip(stack, up_to)
		else:
			up_to = stack.rindex('+-')+1
			stack = flip(stack, up_to)
		print(stack, file=debug)
		n = n + 1
	return n

debug = sys.stdout
sys.stdin = open('large.in')
sys.stdout = open('large.out', 'w')

T = int(input())

for i in range(T):
    stack = input().strip()
    res = solve(stack)
    print("Case #{}: {}".format(i+1, res))
