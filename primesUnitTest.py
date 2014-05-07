#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import primes

class primesTest(unittest.TestCase):
	def setUp(self):
		self.primesTill10 = [2, 3, 5, 7]
		self.primesTill20 = [2, 3, 5, 7, 11, 13, 17, 19]
		self.primesTill100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

	def testConstructor(self):
		noArgument = primes.Primes
		self.failUnlessEqual(noArgument().getPrimes(), self.primesTill100)
		self.assertEqual(noArgument().LargestPrime, 97)
		
		argument0 = primes.Primes(0)
		self.failUnlessEqual(argument0.getPrimes(), [])
		self.assertEqual(argument0.LargestPrime, None)

		argument1 = primes.Primes(1)
		self.failUnlessEqual(argument1.getPrimes(), [])
		self.assertEqual(argument1.LargestPrime, None)

		argument2 = primes.Primes(2)
		self.failUnlessEqual(argument2.getPrimes(), [2])
		self.assertEqual(argument2.LargestPrime, 2)

		argument10 = primes.Primes(10)
		self.failUnlessEqual(argument10.getPrimes(), self.primesTill10)
		
	def testConstructorExceptions(self):
		self.failUnlessRaises(ValueError, primes.Primes, -10)
		self.failUnlessRaises(ValueError, primes.Primes, 12.5)
		self.failUnlessRaises(ValueError, primes.Primes, 'a')
		self.failUnlessRaises(ValueError, primes.Primes, [2, 3])

	def testErathostenesFilter(self):
		a = primes.Primes()
		self.failUnlessRaises(ValueError, a.erathostenesFilter, -1)
		self.failUnlessRaises(ValueError, a.erathostenesFilter, 'a')
		self.failUnlessRaises(ValueError, a.erathostenesFilter, 2.3)

	def testPrintPrimes(self):
		argument20 = primes.Primes(20)
		self.failUnlessEqual(argument20.printPrimes(0, 1), None)

	def testGetPrimes(self):
		argument10 = primes.Primes(10)
		self.failUnlessEqual(argument10.getPrimes(), [2, 3, 5, 7])

	def testPrimeFactorDecomposition(self):
		argument0 = primes.Primes(0)
		self.failUnlessEqual(argument0.primeFactorDecomposition(0), [0])
		self.failUnlessEqual(argument0.primeFactorDecomposition(1), [1])
		self.failUnlessEqual(argument0.primeFactorDecomposition(2), [2])
		self.failUnlessEqual(argument0.primeFactorDecomposition(11), [11])
		self.failUnlessEqual(argument0.primeFactorDecomposition(84), [2, 2, 3, 7])
		self.failUnlessEqual(argument0.primeFactorDecomposition(500), [2, 2, 5, 5, 5])
		self.failUnlessRaises(ValueError, argument0.primeFactorDecomposition, 'a')
		
	def testExportImportPrimes(self):
		argument = primes.Primes(10)
		argument.exportPrimes("test.bin")
		argument.erathostenesFilter(100)
		argument.importPrimes("test.bin")
		self.failUnlessEqual(argument.getPrimes(), [2, 3, 5, 7])
		argument.erathostenesFilter(50000)
		numberOfPrimes = len(argument.getPrimes())
		savePrimes = argument.getPrimes()
		argument.exportPrimes("test.bin")
		argument.importPrimes("test.bin")
		self.failUnlessEqual(argument.getPrimes(), savePrimes)
		self.failUnlessRaises(TypeError, argument.exportPrimes, 123)
		self.failUnlessRaises(IOError, argument.importPrimes, "fileDoesNotExist.bin")
		newPrimes = primes.Primes(filename = "test.bin")
		self.failUnlessEqual(len(newPrimes.getPrimes()), numberOfPrimes)
		self.assert_(True)
		self.failUnless(True)

	def testExportImportDecomposedNumbers(self):
		argument = primes.Primes(100)
		argument.primeFactorDecomposition(50)
		argument.primeFactorDecomposition(97)
		argument.exportDecomposedNumbers("decomposedNumbers.bin")
		argument.resetAll(10)
		self.assertEqual(argument.DecomposedNumbers, {})
		argument.importDecomposedNumbers("decomposedNumbers.bin")
		self.assertEqual(argument.DecomposedNumbers, {50: [2, 5, 5], 97: [97]})
		self.assertEqual(argument.Primes, self.primesTill10) 

	def testHiddenGetter(self):
		primesInstance = primes.Primes(501)
		primesInstance.primeFactorDecomposition(345)
		primesInstance.primeFactorDecomposition(500)
		primeNumbers = primesInstance.getPrimes()
		largestPrime = primesInstance.getLargestPrime()
		numberOfPrimes = primesInstance.getNumberOfPrimes()
		decomposedNumbers = primesInstance.getDecomposedNumbers()
		self.assertEqual(primeNumbers, primesInstance.Primes)
		self.assertEqual(numberOfPrimes, primesInstance.NumberOfPrimes)
		self.assertEqual(largestPrime, primesInstance.LargestPrime)
		self.assertEqual(decomposedNumbers, primesInstance.DecomposedNumbers)

	def testResetAll(self):
		primesInstance = primes.Primes()
		primesInstance.primeFactorDecomposition(50)
		primesInstance.primeFactorDecomposition(97)
		self.assertEqual(primesInstance.DecomposedNumbers, {50: [2, 5, 5], 97: [97]})
		primesInstance.resetAll(20)
		self.assertEqual(primesInstance.Primes, self.primesTill20)
		self.assertEqual(primesInstance.LargestPrime, 19)
		self.assertEqual(primesInstance.NumberOfPrimes, 8)
		self.assertEqual(primesInstance.DecomposedNumbers, {})

if __name__ == "__main__":
	unittest.main()
