num=int(input("Enter a number:"))
onum=num
rev=0

while num>0:
    n1=num%10
    rev=rev*10+n1
    num=num//10
if onum==rev:
    print("The number is palindrome number")
else:
    print("The number is not palindrome")