while True:
    print("===== NUMBER SYSTEM CONVERTER =====\n\n1. Decimal to Binary\n2. Decimal to Octal\n3. Decimal to Hexadecimal\n4. Binary to Decimal\n5. Octal to Decimal\n6. Hexadecimal to Decimal")
    print("7. Exit")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        decimal = int(input("Enter a decimal number: "))
        binary = bin(decimal).replace("0b", "")
        print(f"Binary representation of {decimal} is {binary}")
    elif choice == 2:
        decimal = int(input("Enter a decimal number: "))
        octal = oct(decimal).replace("0o", "")
        print(f"Octal representation of {decimal} is {octal}")
    elif choice == 3:
        decimal = int(input("Enter a decimal number: "))
        hexadecimal = hex(decimal).replace("0x", "")
        print(f"Hexadecimal representation of {decimal} is {hexadecimal}")
    elif choice == 4:
        binary = input("Enter a binary number: ")
        try:
            decimal = int(binary, 2)
            print(f"Decimal representation of {binary} is {decimal}")
        except ValueError:
            print("Invalid binary number. Please enter a valid binary number.")
    elif choice == 5:
        octal = input("Enter an octal number: ")
        try:
            decimal = int(octal, 8)
            print(f"Decimal representation of {octal} is {decimal}")
        except ValueError:
            print("Invalid octal number. Please enter a valid octal number.")
    elif choice == 6:
        hexadecimal = input("Enter a hexadecimal number: ")
        try:
            decimal = int(hexadecimal, 16)
            print(f"Decimal representation of {hexadecimal} is {decimal}")
        except ValueError:
            print("Invalid hexadecimal number. Please enter a valid hexadecimal number.")
    elif choice == 7:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a number from 1 to 7.")
