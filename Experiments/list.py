# write a python program to find element in given list.
# [15, 17, 18, 'hello', 'welcome', 20, 25, 'PCE']

# i) Only String
# ii) Only number

# L = [15, 17, 18, 'hello', 'welcome', 20, 25, 'PCE']

n = int(input("Enter number of elements: "))
L = []

for i in range(n):
    L.append(input("Enter element: "))

choice = int(input("Press 1 for numbers, Press 2 for strings: "))

if choice == 1:
    print("Only numbers")
    for a in L:
        if a.isdigit():
            print(a)

elif choice == 2:
    print("Only strings")
    for a in L:
        if not a.isdigit():
            print(a)