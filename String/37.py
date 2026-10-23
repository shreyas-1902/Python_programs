str=input("Enter a string:")
words=str.split()
longest=""
for i in words:
    if len(i)>len(longest):
        longest=i
print(longest)