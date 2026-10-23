str=input("Enter a string:").lower()
rev=str[::-1]
if str==rev:
    print("String is palindrome")
else:
    print("String is not palindrome")