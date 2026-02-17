user_list = []

n = int(input("Enter number of elements: "))

for i in range(n):
    item = input("Enter number or string: ")
    user_list.append(item)

print("User created list:", user_list)