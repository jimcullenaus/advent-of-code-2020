import re

def get_valid_passwords():
	password_definitions = read_input()
	valid_passwords_count = sum(map(lambda password_definition : is_valid(password_definition), password_definitions))
	print(valid_passwords_count)

def is_valid(password_definition):
	char = password_definition['char']
	first_position = int(password_definition['first']) - 1
	second_position = int(password_definition['second']) - 1
	password = password_definition['password']
	return (password[first_position] == char) ^ (password[second_position] == char)

def read_input():
	password_regex = re.compile(r'^(?P<first>\d+)-(?P<second>\d+)\s*(?P<char>[A-Za-z]):\s*(?P<password>\w+)')
	with open('input.txt') as f:
		return [get_password_values(line, password_regex) for line in f]

def get_password_values(text: str, regex):
	match = regex.search(text)
	return {
		'first': match.group('first'),
		'second': match.group('second'),
		'char': match.group('char'),
		'password': match.group('password')
	}

if __name__ == '__main__':
	get_valid_passwords()
