str=input("Enter a string:")
upper_count=0
lower_count=0

for i in str:
    if i.isupper():
        upper_count+=1
    elif i.islower():
        lower_count+=1
print(f"Upper Characters = {upper_count}")
print(f"Lower Characters = {lower_count}")