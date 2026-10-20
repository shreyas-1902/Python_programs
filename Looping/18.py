num=2
while num<=50:
    i=2
    count=0

    while i<num:
        if num%i==0:
            count+=1
        i+=1

    if count==0:
        print(num)

    num+=1
