import numpy as np

a = ['', "", [], {}, 0, (), set(), range(0), np.array([0,0])]
true_list = ["null", " ", ' ', "asdf"]
i = 0

for test in a:
    if test:
        print("true")
        print(i)
        print(test)

    else:
        print("false")
        print(i)
    i += 1
