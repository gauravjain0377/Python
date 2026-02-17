text = input("Enter a string: ")

length = len(text)

if length % 2 == 0:
    middle = text[length // 2 - 1 : length // 2 + 1]
else:
    middle = text[length // 2]

print("Middle character(s):", middle)