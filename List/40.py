lst = [10, 20, 30]
lst.append(40)
print("append():", lst)

lst.extend([50, 60])
print("extend():", lst)

lst.insert(1, 15)
print("insert():", lst)

lst.remove(30)
print("remove():", lst)

lst.pop(2)
print("pop():", lst)

print("index():", lst.index(40))

lst.append(20)
print("count():", lst.count(20))

lst.sort()
print("sort():", lst)

lst.reverse()
print("reverse():", lst)

new_lst = lst.copy()
print("copy():", new_lst)

lst.clear()
print("clear():", lst)