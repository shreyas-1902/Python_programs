str=input("Enter a string:")
count=0
for char in str:
    if char in "aeiouAEIOU":
        count+=1
print(f"There are vowels {count} in the string")