str=input("Enter your string:")
count=0
for char in str:
    if char not in "aeiouAEIOU":
        count+=1

print(count)