num=int(input("Enter a number:"))
add=0
a=0

while num>0:
    a=num%10
    if a%2==0:
        add+=a
    num=num//10
print(f"Addition of the even numbers is: {add}")