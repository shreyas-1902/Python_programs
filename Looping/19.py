num=int(input("Enter a number to check:"))
i=2
count=0
while i<num:
    if num%i==0:
        count+=1
    i+=1
if count==0:
    print("Entered number is prime")
else:
    print("Entered number is not prime")