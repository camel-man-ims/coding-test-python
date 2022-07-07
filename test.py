import sys

sys.stdin=open("input.txt", "rt")
board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

