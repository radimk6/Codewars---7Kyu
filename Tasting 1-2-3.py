# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)

# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

# test.assert_equals(number([]), [])
# test.assert_equals(number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])

def number(lines):
  list = []
  x = 0
  for number in lines:
    x += 1
    list.append(x,":", number)
  return list

print(number(["a", "b", "c"]))