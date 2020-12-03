import re

def get_valid_passwords():
	password_definitions = read_input()
	valid_passwords_count = sum(map(lambda password_definition : is_valid(password_definition), password_definitions))
	print(valid_passwords_count)

def is_valid(password_definition):
	count = password_definition['password'].count(password_definition['char'])
	return count >= int(password_definition['min']) and count <= int(password_definition['max'])

def read_input():
	password_regex = re.compile(r'^(?P<min>\d+)-(?P<max>\d+)\s*(?P<char>[A-Za-z]):\s*(?P<password>\w+)')
	with open('input.txt') as f:
		return [get_password_values(line, password_regex) for line in f]

def get_password_values(text: str, regex):
	match = regex.search(text)
	return {
		'min': match.group('min'),
		'max': match.group('max'),
		'char': match.group('char'),
		'password': match.group('password')
	}

if __name__ == '__main__':
	get_valid_passwords()
