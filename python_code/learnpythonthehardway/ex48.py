# Takes a string of raw input from a user and returns a sentence that's 
# composed of a list of tuples with the (TOKEN, WORD) pairings. If a word
# isn't part of the lexicon then it should still return the WORD but set 
# the TOKEN to an error token. These error tokens will tell users they messed up.



# get a phrase from user
stuff = raw_input("> ")
# break it up into words
words = stuff.split()


