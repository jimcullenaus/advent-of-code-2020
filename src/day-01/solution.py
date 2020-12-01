import itertools
import math

def get_product(num_pairs: int, target: int) -> int:
	with open('input.txt') as f:
		numbers = [int(line.strip()) for line in f]

	pairs = itertools.combinations(numbers, num_pairs)
	valid_pairs = [pair for pair in pairs if sum(pair) == target]

	if len(valid_pairs) > 0:
		valid_pair = valid_pairs[0]
		return math.prod(valid_pair)
	else:
		raise Exception

if __name__ == '__main__':
	print(get_product(2, 2020))
	print(get_product(3, 2020))
