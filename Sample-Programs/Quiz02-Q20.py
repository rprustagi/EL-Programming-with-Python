n=7
arr = [0]* n
for i in range(n):
  arr[i] = n - i - 1
for i in range(n):
  arr[i] = arr[arr[i]]
print(arr)
