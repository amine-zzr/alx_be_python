# asking the user for the size of the desired pattern
lenght = int(input("Enter the size of the pattern: "))
row = lenght

while row:
    for col in range(lenght):
         print("*", end="")
    print()
    row -= 1
