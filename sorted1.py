L = sorted([34,23,2,-7,45,4],key = abs)
print(L)
L1 = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(L1)
L2 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(L2,'key = str.lower,reverse = Ture')
