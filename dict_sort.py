dict1 = {'a':10, 'b':4, 'c':8}
dict2 = {}
for i in sorted(dict1, key = dict1.get):
    dict2[i] = dict1[i]
print(dict2)
