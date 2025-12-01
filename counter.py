# from collections import Counter
import collections

words = "apple mango mango apple orange".split()
# print(Counter(words))
print(collections.Counter(words))
print(collections.Counter(words).most_common(2))

