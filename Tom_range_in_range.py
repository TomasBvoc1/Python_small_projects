r = 1
while r <= 5:
    c = 1
    while c <= 9:
        print("x", end='')
        c += 1
    r += 1
    print("", end="\n")
print("\n------------------------\n")
columns = 4
rows = 4
for row in range (0, rows):
    for column in range(0, columns):
        print("*", end="")
    print()
print("\n------------------------\n")
rows_=8
row_value = 1
for row_value in range(1,rows_+1):
    for star in range(0, row_value):
        print("o", end="")
    print()
for row_value in range(rows_-1, 0,-1):
    for star in range(0, row_value):
        print("o", end="")
    print()
print("\n------------------------\n")
rows = 7
for row_number in range (1, rows+1):
    for number in range (1, row_number+1):
        print(number, end=" ")
    print()
for row_number in range (rows-1,0,-1):
    for number in range (1, row_number+1):
        print(number, end=" ")
    print()