size = int(input("Enter the size of the pattern: "))
row = size
while row > 0:
    for i in range(size):
        print("*", end=" ")
    print()
    row -= 1
    