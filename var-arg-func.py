def printme(*names):
    print("type of argument: ", type(names))
    for name in names:
        print(name)
printme("john", "david", "smith", "nick")