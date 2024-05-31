# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

# fixed_tests_True = (
#     ( "samurai", "ai"    ),
#     ( "ninja",   "ja"    ),
#     ( "sensei",  "i"     ),
#     ( "abc",     "abc"   ),
#     ( "abcabc",  "bc"    ),
#     ( "fails",   "ails"  ),
# )

# fixed_tests_False = (
#     ( "sumo",    "omo"   ),
#     ( "samurai", "ra"    ),
#     ( "abc",     "abcd"  ),
#     ( "ails",    "fails" ),
#     ( "this",    "fails" ),
#     ( "spam",    "eggs"  )
# )

def solution(text, ending):
  # if ending in text:
  #   return True
  # else:
  #   return False
  return text.endswith(ending)

print(solution("sumo",    "omo"))