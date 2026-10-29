lst=[]
num=int(input("How many elements you want to save in list="))
while len(lst)<num:
    ele=input("Enter a element to add: ")
    lst.append(ele)

print(lst)