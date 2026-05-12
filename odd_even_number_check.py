
# odd and even number check
i = 0
while i != 1:
    a = int(input("Enter the value of A to compute the odd and even number:"))
    if a % 2 == 0:
        print(f"{a} is even number.")
    else:
        print(f"{a} is odd number.")
    i = int(input("Exit? Yes=1, NO=0: "))
    if i == 1:
        print("Program Exited..")
        break

    elif i == 0:
        print("Congratulation, Again computing any value")
    else:
        print("Invalid input! Program exited.")
        break
