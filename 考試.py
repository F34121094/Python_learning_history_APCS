n = int(input())
arr = [0 for i in range(n)]
for i in range(len(arr)):
    arr[i] = int(input())
ans = arr.sort()
for i in range(len(arr)):
    print(ans[i],end = " ")