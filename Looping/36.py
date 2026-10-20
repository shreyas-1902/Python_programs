tot=0
num=int(input("Enter a number:"))

while num!=0:
    tot+=num
    num=int(input("Enter the next number:"))
print(f"Sum= {tot}")