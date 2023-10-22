# exceptions - statements or code can still cause an error even when the syntax is correct.

x = 5
if x < 0:
  raise Exception(f"\nx should be positive")
else:
  print(f"\n{x} is a positive number as expected")
  
x = 5
assert (x >= 0), f"x should be positive"
  
# catch exceptions when they occur

try:
  x = 5 / 0
except:
  print(f"\nAn error has occured")
  
# include the type of an exception 
try:
  x = 5 / 0
except Exception as Error:
  print(f"\n{Error}")
  
# catching multiple exceptions when the type of error is known
# the first error is always raised even if there are other oerrors that follow.

try:
  x = 5 / 0
  y = x + '5'
except ZeroDivisionError as ZeroError:
  print(f"\n{ZeroError}")
except TypeError as TyError:
  print(f"\n{TyError}")
  
# can also add an 'else' clause when no exception has beeb raised

try:
  x = 5 / 1
  y = x + 5
except ZeroDivisionError as ZeroError:
  print(f"\n{ZeroError}")
except TypeError as TyError:
  print(f"\n{TyError}")
else:
  print(f"\nThe code is working as expected")
  
# can also add a 'finally' clause which runs regardless of whether an exceptions has been or not

try:
  x = 5 / 1
  y = x + 'a'
except ZeroDivisionError as ZeroError:
  print(f"\n{ZeroError}")
except TypeError as TyError:
  print(f"\n{TyError}")
else:
  print(f"\nThe code is working as expected")
finally:
  print(f'\nCleaning up...')
  
# user defined exceptions - they take Exception as base input

class ValueTooHighError(Exception):
  pass

# exceptions can also be defined to take in arguments:

class ValueTooSmallError(Exception):
  def __init__(self, message, value):
    self.message = message
    self.value = value

def testValue(x):
  if x > 100:
    raise ValueTooHighError(f"Value is too high")
  if x < 5:
    raise ValueTooSmallError(f'\nValues is too small', x)
  
# testValue(200)
# testValue(2)

# alternatively use try except block:

try:
  testValue(2)
except ValueTooHighError as ValueError:
  print(ValueError)
except ValueTooSmallError as ValueError:
  print(ValueError.message, ValueError.value)