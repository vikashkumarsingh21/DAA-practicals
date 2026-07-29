list = [10,20,30,40,80,100,2000,500,425]
num = 100
low = 0
high = len(list)-1
found = False

while low<=high:
    mid = low + (high - low) // 2
    if list[mid] == num:
        found = True
        print(f"Number {num} found at index {mid}")
        break
    elif list[mid] < num:
        low = mid + 1
    else:
        high = mid -1

if not found:
    print(f"Number {num} not found")




arr = [10,20,30,40,80,100,425,500,2000]

test_cases = [
    ("Best Case", 80),
    ("Average Case", 100),
    ("Worst Case", 999)
]

for case, num in test_cases:

    low = 0
    high = len(arr) - 1
    found = False
    iterations = 0

    while low <= high:
        iterations += 1

        mid = low + (high - low) // 2

        if arr[mid] == num:
            found = True
            break
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    print(case)
    if found:
        print(f"{num} Found at index {mid}")
    else:
        print(f"{num} Not Found")

    print("Iterations =", iterations)
    print("-" * 30)