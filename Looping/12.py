num=int(input("Enter a number:"))
reverse=0
while num>0:
    dig=num%10
    reverse=reverse*10+dig
    num=num//10
print(f"The reversed number is {reverse}")