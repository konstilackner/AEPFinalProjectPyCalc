# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 13:27:38 2016

@author: Konstantin
"""

import unittest
from Calculator import Calculator



class TestCalculator(unittest.TestCase):

  def test_FivePlusFiveIsTen(self):
      five = Calculator(5)
      self.assertEqual(10, five.add(5))
      
  def test_ZeroPlusZeroIsZero(self):
      zero = Calculator(0)
      self.assertEqual(0, zero.add(0))
      
  def test_ZeroTimesTenIsZero(self):
      zero = Calculator(0)
      self.assertEqual(0, zero.multiply(10))
      
  def test_OneTimesFiveIsFive(self):
      one = Calculator(1)
      self.assertEqual(5, one.multiply(5))

  def test_FiveTimesFiveIsTwentyfive(self):
      five = Calculator(5)
      self.assertEqual(25, five.multiply(5))
      
  def test_ZeroDividedByTenIsZero(self):
      zero = Calculator(0)
      self.assertEqual(0, zero.divide(10))
      
  def test_SevenDividedByOneIsSeven(self):
      seven = Calculator(7)
      self.assertEqual(7, seven.divide(1))
      """
  def test_TenDividedByTenIsOne(self):
      ten = Calculator(10)
      self.assertEqual(1, ten.divide(10))
      
  def test_OneDividedByZeroIsError(self):
      one = Calculator(0)
      with self.assertRaises(ZeroDivisionError):
          one.divide(0)
          
  def test_FiveSquaredIsTwentyfive(self):
      five = Calculator(5)
      self.assertEqual(25, five.square())
      """
      
suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
unittest.TextTestRunner(verbosity=2).run(suite)