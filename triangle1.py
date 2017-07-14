def triangle1(max):
    L = [1]
    m = 0
    while m < max:
        yield L
        L = [L[x] + L[x + 1] for x in range(len(L) - 1)]
        L.insert(0,1)
        L.append(1)
        m = m + 1


a = triangle1(11)
for i in a:
    print(i)
