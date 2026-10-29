lst=[10,20,30,40,50,60,70,40,20,10]
# lst=list(set(lst))
# print(lst)

new_lst=[]
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)