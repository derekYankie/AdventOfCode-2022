# Assignment: Unit test file for day01.py
# https://docs.pytest.org/en/6.2.x/parametrize.html
# Date: 12/01/2022
# Author: derekYankie

import pytest
import os

from day01 import findMostCalories

@pytest.mark.parametrize("num1, num2, total", [(4,10,14), (5,10,15)])
def testAdd(num1, num2, total):
    assert num1+num2 == total

def findMostCalories(testAdd):
    print("Great Job!")

def main():
    """ Main program """
    findMostCalories(testAdd)

if __name__ == "__main__":
    main()
