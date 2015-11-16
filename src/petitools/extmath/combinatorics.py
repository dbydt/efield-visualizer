# Description:
# combinatorics.py contains combinatorial functions
# 
# Author:
# Calvin Yeung (dbydt)

from sys import setrecursionlimit

# set recursion limit of factorial function
setrecursionlimit(100000)

# returns the factorial of a positive integer
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

# returns npr of n and k	
def npr(n, k):
	product = 1
	
	for x in range(n - k + 1, n + 1):
		product *= x
		
	return product

# returns ncr of n and k
def ncr(n, k):
	return npr(n, k) / factorial(k)

# returns combinations with repetition	
def ncr_repeat(n, k):
	return ncr(n + k - 1, k)

# returns composition of a string
def composition(s):
	st = sorted(s)
	comp = []
	current = st[0]
	count = 0

	for c in st + [' ']:
		if current == c:
			count += 1
		else:
			comp.append((current, count))
			current = c
			count = 1
	
	return comp

# returns if two strings are permutations of each other
def is_permutation(m, n):
	return composition(str(m)) == composition(str(n))