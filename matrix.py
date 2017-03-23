from utils import *
import random
import time
import argparse
import os

# set of posible arguments
parser = argparse.ArgumentParser(description='Generates a Matrix style screen.')
parser.add_argument('-ch', '--characters', help='The set of characters that may be included in Matrix.')
parser.add_argument('-s', '--speed', help='The speed of the lines: (slower) 1, 2 or 3 (faster).')
parser.add_argument('-b', '--binary', action='store_true',   help='The set of characters that may be included in Matrix.')
args = parser.parse_args()


def main():

	# if a set of arguments is given it's used.
	if(args.characters):
		characters = args.characters
	else:
		characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0134567889'

	# if the argument binary is given, the characters shown are 0 or 1.
	if args.binary:
		characters = '01'

	sleep_time = 0.05

	if args.speed:

		if args.speed == '1':
			sleep_time = 0.05
		elif args.speed == '2':
			sleep_time = 0.03
		elif args.speed == '3':
			sleep_time = 0
		else:
			sleep_time = 0.05




	while True:

		# the number of characters depends on the terminal width
		rows, columns = os.popen('stty size', 'r').read().split()

		# init a empty line
		line = ''

		for _ in range(int(columns)):

			# we get a random character
			random_index = random.randint(0,len(characters) - 1)
			character = characters[random_index]

			# 4 about 10 characters will be dark colored.
			probabilidad = True if random.randint(0,9) >= 3 else False
			if(probabilidad):
			    character = text_success(character)
			else:
			    character = text_msg(character)

			line += " {} ".format(character)

		print line
		time.sleep(sleep_time)




if __name__ == '__main__':   main()
