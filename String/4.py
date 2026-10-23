str=input("Enter your name:")
count=0
for char in str:
    if char in "aeiouAEIOU":
        count+=1

print(count)