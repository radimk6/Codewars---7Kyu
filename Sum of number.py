# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# Examples (a, b) --> output (explanation)
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

# test.assert_equals(get_sum(0,1),1)
# test.assert_equals(get_sum(0,-1),-1)

def get_sum(a,b):
  if b < a:
    number = b
    for numbers in range(b+1, a+1):
      number += numbers
  else:
    number = a
    for numbers in range(a+1, b+1):
      number += numbers
  return number

print(get_sum(0, -1))