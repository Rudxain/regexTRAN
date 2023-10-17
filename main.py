#!/usr/bin/env python3
from typing import Final
from sys import argv
import re

# this is intended to be imported
def retran_exec(src: str, replace: str | bytes, dat: str | bytes):
	prg: Final = re.compile(src, re.X)
	while dat != (dat := prg.sub(replace, dat)):
		yield dat

def main(*args: str):
	with open(args[0], 'r') as f:
		src = f.read()
	dat = ''
	if len(args) > 1:
		with open(args[1], 'r') as f:
			dat = f.read()
	(src, replace) = src.split('//', 1)
	for gen in retran_exec(src, replace, dat):
		print(gen)

if __name__ == '__main__':
	main(*argv[1:])
