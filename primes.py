#!/usr/bin/python
# -*- coding: utf-8 -*-

import cPickle

class Primes(object):
	"""This class is used to compute and save prime numbers and also
	calculate prime number decompositions"""

	def __init__(self, maxNumber = 100, filename = ""):
		"""Constuctor initializes all primes until maxNumber or
		imports them from a binary file called filename"""
		self.__Filter = []
		self.__Primes = []
		self.__checkForInt(maxNumber)
		self.__MaxNumber = maxNumber
		self.__LargestPrime = None
		self.__NumberOfPrimes = None
		self.__DecomposedNumbers = {}
		if filename == "":
			self.__MaxNumber = maxNumber
			self.erathostenesFilter(self.__MaxNumber)
		else:
			self.importPrimes(filename)

	def importPrimes(self, filename):
		"""Imports prime numbers from the binary file filename"""
		with open(filename, 'rb') as f:
			self.__Primes = cPickle.load(f)
		self.__MaxNumber = len(self.__Primes)
		self.__NumberOfPrimes = self.__MaxNumber
		if self.__NumberOfPrimes > 0:
			self.__LargestPrimes = self.__Primes[self.__NumberOfPrimes-1]
		else:
			self.__LargestPrimes = None

	def exportPrimes(self, filename):
		"""Exports prime numbers to the binary file filename"""
		with open(filename, 'wb') as f:
			cPickle.dump(self.__Primes, f, cPickle.HIGHEST_PROTOCOL)

	def importDecomposedNumbers(self, filename):
		"""Imports numbers and their prime number decomposition from the
		binary file filename"""
		with open(filename, 'rb') as f:
			self.__DecomposedNumbers = cPickle.load(f)

	def exportDecomposedNumbers(self, filename):
		"""Exports numbers and their prime number decomposition from the
		binary file filename"""
		with open(filename, 'wb') as f:
			cPickle.dump(self.__DecomposedNumbers, f, cPickle.HIGHEST_PROTOCOL)

	def erathostenesFilter(self, quantity):
		"""Calculates all prime numbers up to quantity or the member variable
		self.__MaxNumber, if it is larger
    
		The Sieve of Eratosthenes is a standard way to calculate prime numbers.
		For more information confirm
		en.wikipedia.org/wiki/Sieve_of_Eratosthenes"""
		self.__checkForInt(quantity)
		if self.__MaxNumber <= quantity:
			self.__Primes = []
			self.__MaxNumber = quantity
			self.__Filter = self.__MaxNumber*[True]

			for i in xrange(2, self.__MaxNumber):
				if (self.__Filter[i] == True):
					self.__Primes.append(i)
					for j in xrange(i*i, self.__MaxNumber, i):
						self.__Filter[j] = False
			self.__Filter = []
		if self.__MaxNumber == 2:
			self.__Primes = [2]
		self.__NumberOfPrimes = len(self.__Primes)
		if self.__NumberOfPrimes > 0:
			self.__LargestPrime = self.__Primes[self.__NumberOfPrimes-1]
		else:
			self.__LargestPrime = None

	def printPrimes(self, von = 0, bis = 0):
		self.erathostenesFilter(bis)
		for i in self.__Primes:
			if von == 0 and bis == 0:
				print(i)
			else:
				if i >= von and i <= bis:
					print(i)
	def getPrimes(self):
		return self.__Primes

	def primeFactorDecomposition(self, number):
		"""Decompostion of number into prime numbers is calculated. It is
		just performed by trial and error"""
		primeFactors = []
		result = None
		self.__checkForInt(number)
		if number in self.__DecomposedNumbers:
			result = self.__DecomposedNumbers[number]
		else:
			self.erathostenesFilter(number + 1)
			if number == 0:
				self.__DecomposedNumbers[0] = [0]
				return [0]
			elif number == 1:
				self.__DecomposedNumbers[1] = [1]
				return [1]
			elif number in self.__Primes:
				self.__DecomposedNumbers[number] = [number]
				return [number]
			else:
				self.erathostenesFilter(number)
				extension = number
				i = 0
				while i < len(self.__Primes) and self.__Primes[i] < number:
					if extension > 1 and extension % self.__Primes[i] == 0:
						extension /= self.__Primes[i]
						primeFactors.append(self.__Primes[i])
						i -= 1
					i += 1
			result = primeFactors
			self.__DecomposedNumbers[number] = primeFactors
		return result

	def __checkForInt(self, inputNum):
		a = type(inputNum)
		if not (a == int or a == long) or inputNum < 0:
			raise ValueError("Insert positive integer!")

	def resetAll(self, number):
		self.__MaxNumber = 0
		self.erathostenesFilter(number)
		self.__DecomposedNumbers = {}

	def getLargestPrime(self):
		return self.__LargestPrime

	def getNumberOfPrimes(self):
		return self.__NumberOfPrimes

	def getDecomposedNumbers(self):
		return self.__DecomposedNumbers

	"Definiere versteckte(n) Getter"
	Primes = property(getPrimes)
	LargestPrime = property(getLargestPrime)
	NumberOfPrimes = property(getNumberOfPrimes)
	DecomposedNumbers = property(getDecomposedNumbers)
