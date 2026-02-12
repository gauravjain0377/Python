n = int(input("Enter number of elements: "))
L = []

for i in range(n):
    value = input("Enter element: ")
    L.append(value)

mid = n // 2

print("Middle element is:")
print(L[mid])



