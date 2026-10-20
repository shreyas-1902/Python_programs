while True:
    print("\nMENU")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Exit")

    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            a=int(input("Enter first number:"))
            b=int(input("Enter second number:"))
            print("Sum=", a+b)

        case 2:
            a=int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Difference=", a-b)

        case 3:
            a=int(input("Enter first number:"))
            b=int(input("Enter second number:"))
            print("Product=", a*b)

        case 4:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice!")