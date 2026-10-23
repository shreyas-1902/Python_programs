str=input("Enter a string:")
words=str.split()
short=words[0]
for i in words:
    if len(i)<len(short):
        short=i
print(short)