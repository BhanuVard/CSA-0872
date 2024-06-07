1 = [1,1,1,2,2,3,4,4]
u = []
for  i in 1:
    if i not in u and 1.count(i) == 1:
        u.append(i)
print(list(u))
