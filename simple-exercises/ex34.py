# Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted character frequency table to the screen.

def char_freq_table(file_name):
    file = open(file_name, 'r')
    text = file.read()
    file.close()
    
    freq = {}

    for c in text:
        freq[c] = freq.get(c, 0) + 1

    sorted_freq = ((k, d[k]) for k in sorted(freq, key=freq.get, reverse=True))

    print("------------")
    for k, v in sorted_freq:
        print(k, ": ", v)
    print("------------")


file_name = input("Please enter the file name: ")
char_freq_table(file_name)
