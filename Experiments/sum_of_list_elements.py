lst = []

n = int(input("Enter number of elements in list: "))

for i in range(n):
    element = int(input("Enter element: "))
    lst.append(element)

a = int(input("Enter first index: "))
b = int(input("Enter second index: "))

sum_elements = lst[a] + lst[b]

print("List:", lst)
print("Sum of elements:", sum_elements)