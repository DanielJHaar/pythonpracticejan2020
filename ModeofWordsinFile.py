#Parses a user inputted text file, and returns the most common word in the file along with the number of times it appears.

name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print("The most common word:", bigword, "appears" , bigcount, "times.")
