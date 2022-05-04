#!/usr/bin/python3
import random
num = random.randint(-10, 10)

if num == 0:
	print('{0} is zero'.format(num))
elif num < 0:
	print('{0} is negative'.format(num))
elif num > 0:
	print('{0} is positive'.format(num))