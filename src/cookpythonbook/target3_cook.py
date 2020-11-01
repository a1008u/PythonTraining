# 複素数を含まないmath関数
from math import *

# 複素数対応math関数
import cmath

def variables():
  a = [1, 2, 3]
  b = a
  c = b
  b[1] = 5
  print(a, b, c)

def variables2():
  a = 1
  b = a
  c = b
  b = 5
  print(a, b, c)

def escape():
  x1 = "\tThis string starts with a \"tab\"."
  x2 = "This string contains a single backslash(\\)."
  x = """Starting and ending a string with triple " characters
permits embedded newlines, and the use of " and ' without
backslashes"""
  print(x1, x2, x)


def numeric_func():
  print(tanh(2.3543))
  # print(tanh('4243'))

def complex_numbers():
  print((3+2j).real)

def cmath_func():
  print(cmath.sqrt(-1))

def userinput():
  name: str = input("Name? ")
  print(name)
  age: int = int(input("Age? "))   
  print(age)


if __name__ == '__main__':
  variables()
  variables2()
  escape()
  numeric_func()
  complex_numbers()
  cmath_func()
  userinput()