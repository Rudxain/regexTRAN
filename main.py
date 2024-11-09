#!/usr/bin/env python3
from typing import Final
from sys import argv
import re

# this should accept pre-compiled `re.Pattern`s,
# but IDK how to do that properly
def retran_exec(src: str, replace: str | bytes, dat: str | bytes):
	'''
	this is intended to be imported
	'''
	prg: Final = re.compile(src, re.X)
	while dat != (dat := prg.sub(replace, dat)):
		yield dat


def main(*args: str):
	if len(args) == 0:
		print('usage: retran <program file> [input file]')
		
	with open(args[0], 'r') as f:
		src = f.read()
	dat = ''
	if len(args) > 1:
		with open(args[1], 'r') as f:
			dat = f.read()

	# order is very important!
	# `src` can contain \x2f, but `replace` can't
	(src, replace) = src.split('//', 1)

	for gen in retran_exec(src, replace, dat):
		print(gen)

if __name__ == '__main__':
	main(*argv[1:])
