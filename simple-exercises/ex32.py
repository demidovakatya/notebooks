# Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the line to the screen if it is a palindrome.

file_name = input("Please enter the file name: ")

def palindrome(phrase):
    punctuation = "'.?,! "

    clean_phrase = ""
    for letter in phrase:
        if letter not in punctuation:
            clean_phrase += letter.lower()

    return clean_phrase == clean_phrase[::-1]

file = open(file_name, 'r')
for line in file:
    if palindrome(line.rstrip()):
        print(line.rstrip())
file.close()
