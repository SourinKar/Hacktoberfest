def printPyramid(size):
    x = int(size/2)
    y = 1
    for i in range(size):
        printLine(x, y)
        if i < int(size/2):
            x -= 1
            y += 1
        else:
            x += 1
            y -= 1

def printLine(x, y):
    for i in range(x + 1):
        print(" ", end = "")
    for i in range(y * 2 - 1):
        print("*", end = "")
    print()
    
    
printPyramid(9)
