str=input("Enter a string:")
nstr=""
for char in range(len(str)-1, -1, -1):
    nstr=nstr+str[char]
if str==nstr:
    print("The string is palindrome")
else:
    print("String is not palindrome")