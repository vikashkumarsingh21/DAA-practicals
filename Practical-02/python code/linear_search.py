arr = [10,20,30,60,55,35,76]
num = int(input("Enter the number to search: "))

found = False

for i in range(len(arr)):
    if arr[i]==num:
        found= True
        print(f"Number {num} found at index {i}")

if not found:
    print(f"Number {num} not found")