import math
from typing import List

def get_grid() -> List[List[bool]]:
	with open('input.txt') as f:
		return [parse_line(line) for line in f]


def parse_line(line: str) -> List[bool]:
	# [:-1] to skip the newline char
	return [char is '#' for char in line][:-1]

def get_tree_count(right: int, down: int):
	grid = get_grid()
	column = 0
	tree_count = 0
	for row in grid[::down]:
		if row[column]:
			tree_count += 1
		column = (column + right) % len(row)
	return tree_count

if __name__ == '__main__':
	vals = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
	answer = math.prod([get_tree_count(*val) for val in vals])
	print(answer)
