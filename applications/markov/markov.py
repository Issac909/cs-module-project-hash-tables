import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    f.close()
    
words = words.split(' ')

# TODO: analyze which words can follow other words
# Your code here
pairs = []
for x in range(len(words) - 1):
    pairs.append((words[x], words[x + 1]))
    
dictionary = {}
for x in pairs:
    if x[0] in dictionary.keys():
        dictionary[x[0]].append(x[1])
    
    else:
        dictionary[x[0]] = [x[1]]


# TODO: construct 5 random sentences
# Your code here

for x in range(5):
    start = [random.choice(words)]
    print('\n')
    for n in range(30):
        start.append(random.choice(dictionary[start[-1]]))
    
    print(' '.join(start), end = ' ')
    print('\n')

