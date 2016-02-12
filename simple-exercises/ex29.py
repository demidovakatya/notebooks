# Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

def filter_long_words(words, n):
    '''
    words: a list of words,
    n: an integer.
    returns: the list of words that are longer than n
    '''
    return filter(lambda x: len(x) > n, words)

