# asking the user for a number to generate its multiplication table
number = int(input("Enter a number to see its multiplication table: "))

# looping through a list from 1 to 10 to print the mltu table of the given nuber
for x in range(1, 11):
    print(f"{number} * {x} = {number * x}")
