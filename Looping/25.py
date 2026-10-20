str=input("Enter a string:")
count=0
for char in str:
    if char.isalpha() and char not in "aeiouAEIOU":
        count+=1
print(f"There are consonants {count} in the string")