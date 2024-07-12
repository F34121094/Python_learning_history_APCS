n = int(input())
a = input()
list = list(map(int,a.split()))
pass_list = []
not_pass = []
for i in list:
    if i >= 60:
        pass_list.append(i)
    else:
        not_pass.append(i)
list.sort()
print(*list)
if not_pass:
    print(max(not_pass))
else:
    print("best case")
if pass_list:
    print(min(pass_list))
else:
    print("worst case")