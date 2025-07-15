#program uses nested loop to draw a square pattern
rows = int(input('Enter the size of the pattern: '))
i = 1
while i <= rows:
    for j in range(1, (rows+1)):
        print("*", end=' ')
    print()
    i += 1
