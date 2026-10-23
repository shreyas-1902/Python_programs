str=input("Enter a string:")
res=""
for i in str:
    if i.isalnum() or i==" ":
        res+=i

print(res)