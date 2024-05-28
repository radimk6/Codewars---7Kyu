# Take 2 strings s1 and s2 including only letters from a to z. 
# Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

# def basics():
#         test.assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
#         test.assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
#         test.assert_equals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")

def longest(a1, a2):
  a3 = a1 + a2
  letter_list = []
  for one_letter in a3:
    if one_letter not in letter_list:
      letter_list.append(one_letter)
  letter_list = sorted(letter_list)

  return "".join(letter_list)  

print(longest("inmanylanguages", "theresapairoffunctions"))