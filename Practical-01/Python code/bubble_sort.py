arr = []
print("Enter the number of elements in the array:")
n = int(input())
print("Enter the elements of the array:")
for _ in range(n):
    arr.append(int(input()))

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print(f"Swapped {arr[j]} and {arr[j+1]}: {arr}")
print("Sorted array is:")
for i in range(n):
    print(arr[i], end=" ")