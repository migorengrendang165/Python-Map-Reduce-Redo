# import the required libraries
import sys;
from itertools import groupby;

# create a map function
def mapfunc(w):
  # let us remove all punctuation and spaces
  cleanword = ''.join([i for i in w if i.isalpha()])
  return [cleanword,1];

# create a reduce function
def reducefunc(key, values):
  counts = [x[1] for x in values];
  return [key,sum(counts)];

# download the data
!wget https://www.gutenberg.org/cache/epub/1777/pg1777.txt -O romeojuliet.txt
  
# split the document into single word
with open("romeojuliet.txt") as f:
  words=[word for line in f for word in line.split()]
  
# print words in the file
print(words);

map_result = map(mapfunc, words)
# map result containing: ['the', 1], ['any', 1], ['selected', 1], ['the', 1], ...

map_result_sorted = sorted (map_result, key = lambda x: x[0])

reduce_result = [];
for k, g in groupby(map_result_sorted, key = lambda x: x[0]):
    reduce_result.append(reducefunc(k, list(g)))
  
# print the result, how many times a word used in the file
print(reduce_result)
