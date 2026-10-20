num=int(input("Enter a number:"))
tot=0
while num>0:
    digit=num%10
    tot+=digit
    num=num//10
print(f"The sum of digits is {tot}")