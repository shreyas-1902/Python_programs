num=int(input("Enter a number:"))
count=0
a=0
b=1

while count<num:
    print(a)
    res=a+b
    a=b
    b=res
    count+=1