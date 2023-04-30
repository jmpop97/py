import collections
a = [1, 1, 2, 2, 3, 4, 7, 7]
b = collections.Counter(a).most_common(2)
if (b[0][1] == b[1][1]):
    result = -1
else:
    result = b[0][0]
