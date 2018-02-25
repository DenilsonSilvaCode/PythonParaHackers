#!/usr/bin/python3

# -*- coding: utf-8 -*-

#gerador de Hexadecimal 

import os
import sys

try:
	string=sys.argv[1]
	cmd = "echo -n "+string+" | xxd -ps | sed 's/[[:xdigit:]]\{2\}/\\\\x&/g'"
	os.system(cmd)
except IndexError:
	print("\nInforme a string!\n")
	
