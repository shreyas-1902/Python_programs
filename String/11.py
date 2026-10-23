str=input("Enter a string or sentence:").lower()
ch=input("Enter a character or word to find:").lower()
count=0
for i in range(len(str)):
    if str[i]==ch:
        count+=1
print(count)