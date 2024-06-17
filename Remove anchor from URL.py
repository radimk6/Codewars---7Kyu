# Complete the function/method so that it returns the url with anything after the anchor (#) removed.

# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"

# test.assert_equals(remove_url_anchor("www.codewars.com#about"), "www.codewars.com")
# test.assert_equals(remove_url_anchor("www.codewars.com/katas/?page=1#about"), "www.codewars.com/katas/?page=1")
# test.assert_equals(remove_url_anchor("www.codewars.com/katas/"), "www.codewars.com/katas/")

def remove_url_anchor(url):
  result = []
  if "#" in url:
    for y in url:
      if y == "#":
        break
      else:
        result.append(y)
    return " ".join(result)
  else:
    return url
  # return url.split('#')[0]
   
print(remove_url_anchor("www.codewars.com/katas/?page=1#about"))