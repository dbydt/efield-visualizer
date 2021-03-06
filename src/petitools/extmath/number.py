# Description:
# number.py contains number theory related
# functions
# 
# Author:
# Calvin Yeung (dbydt)

from math import *
from sys import setrecursionlimit

# set recursion limit of gcd function
setrecursionlimit(100000)

# checks if number is prime
def is_prime(n):
	if n <= 1:
		return False
	if n == 2:
		return True
	for x in [2] + range(3, int(sqrt(n) + 1), 2):
		if n % x == 0:
			return False
	return True

# check if two numbers have any common factors	
def is_relatively_prime(m, n):
	return gcd(m, n) == 1

# returns the next prime after the given number
def next_prime(n):
	while True:
		n += 1
		if is_prime(n):
			return n

# returns a list of all primes less than n		
def prime_list(n):
	p = []
	for x in range(n):
		if is_prime(x):
			p.append(x)
	return p

# generates primes using sieve method
def primes_list_sieve(n):
	p = []
	list = []
	
	# generate list of "True"
	j = 0
	while j < n:
		list.append(True)
		j += 1
	
	# cancel multiples of primes; ascending
	for i in range(2, int(sqrt(n))):
		if list[i]:
			for j in range(i**2, n, i):
				list[j] = False
	
	# generate list of numbers from boolean list
	i = 0
	while i < len(list):
		if list[i]:
			p.append(i)
		i += 1
	
	# return list (without 0 and 1)
	return p[2:]


# returns the prime factorization of a number
def prime_factors(n):
	p = []
	num = 2
	count = 0
	added = False
	
	while n != 1 or not added:
		if n % num == 0:
			n /= num
			count += 1
			added = False
		else:
			if count > 0:
				p.append((num, count))
				count = 0
				added = True
				
			num = next_prime(num)
	
	return p

# returns the greatest common denominator of two numbers
def gcd(m, n):
	if n == 0:
		return m
	return gcd(n, m % n)

# fraction object that supports basic operations
class RationalNumber:
	def __init__(self, n, d=1):
		self.n = n
		self.d = d
	
	# float value of fraction
	def floatValue(self):
		return float(self.n) / self.d
	
	# inverse of fraction	
	def inverse(self):
		return Fraction(self.d, self.n)
	
	# negated fraction	
	def negate(self):
		return Fraction(-self.n, self.d)
	
	# addition between two fractions
	def __add__(self, other):
		n = self.n * other.d + self.d * other.n
		d = self.d * other.d
		g = gcd(n, d)
		return Fraction(n / g, d / g)
	
	# subtraction between two fractions
	def __sub__(self, other):
		return self + other.negate()
	
	# multiplication between two fractions
	def __mul__(self, other):
		n = self.n * other.n
		d = self.d * other.d
		g = gcd(n, d)
		return Fraction(n / g, d / g)
	
	# division between two fractions	
	def __div__(self, other):
		return self * other.inverse()
	
	# string representation of fraction
	def __str__(self):
		if self.d == 0:
			return str(self.n)
		else:
			return str(self.n) + "/" + str(self.d)


# vector class that supports basic operations
class Vector:
	
	# initialization
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	# get components in tuple
	def get_components(self):
		return (self.x, self.y)
	
	# normalized to unit vector in direction of vector
	def get_normalized(self):
		mag = self.get_magnitude()
		return Vector(self.x / mag, self.y / mag)
	
	# magnitude only
	def get_magnitude(self):
		return sqrt(self.x ** 2 + self.y ** 2)
	
	# angle formed by vector	
	def get_direction(self):
		return atan2(self.x, self.y)
	
	# add function
	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)
	
	# subtract function
	def __sub__(self, other):
		return self + other.negate()
	
	# string representation
	def __str__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ")"
	
	# negate function
	def negate(self):
		return Vector(-self.x, -self.y)