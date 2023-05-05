dots = [[1, 1], [2, 2], [3, 3], [4, 4]]


a, b, c, d = dots
a1, a2, b1, b2, c1, c2, d1, d2 = *a, *b, *c, *d

[a1, a2], [b1, b2], [c1, c2], [d1, d2] = dots
print(a1)
print(b1)


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 10, 'b': 20, 'c': 30}

result_dict = {key: dict1[key] + dict2[key] for key in dict1}
print(result_dict)
a = 'apple'
a = a.capitalize()
print(a)
