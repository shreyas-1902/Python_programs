num=int(input("Enter a number:"))
ori=num
count=0
add=0
while num>0:
    count+=1
    num=num//10
num=ori
while num>0:
    dig=num%10
    add+=dig**count
    num=num//10

if add==ori:
    print("The number is armstrong")
else:
    print("The number is not armstrong")