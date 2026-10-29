lst=[16,13,52,79,45,62,18,35]
lst1=[12,23,34,45,56,67]
new_lst=[]
for i in lst:
    for j in lst1:
        if i==j:
            new_lst.append(i)
print(new_lst)