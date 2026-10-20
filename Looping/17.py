num=int(input("Enter a number:"))
b=0

while num>0:
    a=num%10
    if a>b:
        b=a
    num=num//10
print(f"The biggest digit in number is {b}")