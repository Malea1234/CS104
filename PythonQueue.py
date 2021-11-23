names = []
x = 0
while x < 10:
    acceptedName = input("enter name of next person in line: ")
    names.append(acceptedName)
    x = x + 1

print("Here is the names in the order of the line: ")

while len(names):
    print (names.pop(0))

    
