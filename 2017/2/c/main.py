import sys
import itertools
import numpy as np

which = "sample"

dirs = [
    np.array([0, 1]),
    np.array([1, 0]),
    np.array([0, -1]),
    np.array([-1, 0])]

def solve(room):
    shooter_mask = (room == '-') | (room == '|')
    empty_space = (room == '.')
    shooter_inds = np.argwhere(room == '-')

    covered_by = np.zeros((len(shooter_inds), 2) + room.shape, np.int8)

    for i, dir in enumerate(dirs):
        for si, start in enumerate(shooter_inds):
            curr = covered_by[si, i%2]
            i, j = start
            dx, dy = dir
            while 0 <= i < curr.shape[0] and 0 <= j < curr.shape[1]:
                cell = room[i,j]
                curr[i,j] = 1
                if cell == '\\':
                    dx, dy = dy, dx
                elif cell == '/':
                    dx, dy = -dy, -dx
                elif cell in ('-', '|'):
                    curr[...] = -1

            print(curr)

    print(room)
    print(shooter_inds, shooter_mask)


sys.stdin = open('{}.in'.format(which))
# sys.stdout = open('{}.out'.format(which), 'w')

T = int(input())

for i in range(T):
    R, C = map(int, input().split())
    room = np.array([
        list(input())
        for i in range(R)
    ])
    res = solve(room)
    print("Case #{}: {}".format(i+1, res))
