# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

# test.assert_equals(square_digits(9119), 811181)
# test.assert_equals(square_digits(0), 0)

def square_digits(num):
  number_list = []
  num_list = []
  num = str(num)
  for one_num in num:
    one_num = int(one_num)
    sqrt = one_num ** 2
    number_list.append(str(sqrt))
  for number in number_list:
    num_list.append(number)
  result = "".join(num_list)
  result = int(result)

  return result

print(square_digits(9119))