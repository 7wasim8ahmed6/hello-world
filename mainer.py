# Hacker rank tasks

from collections import deque

if __name__ == '__main__':
    d = deque()
    N = int(input())
    for i in range(N):
        lInput = input().split()
        if (len(lInput) == 1):
            eval('d.' + lInput[0] + '()')
        else:
            eval('d.' + lInput[0] + '(' + lInput[1] + ')')

    print(d)