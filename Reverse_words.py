# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"


#reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god'
#reverse_words('apple'), 'elppa'
#reverse_words('a b c d'), 'a b c d')
#reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')

def reverse_words(text):
    one_word = text.split(" ")
    words_list = []
    for x in one_word:
      words_list.append(x[::-1])

    return " ".join(words_list)

print(reverse_words('The quick brown fox jumps over the lazy dog.'))