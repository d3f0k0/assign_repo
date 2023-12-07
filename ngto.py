#Author: Tran Nguyen Hanh
#https://github.com/d3f0k0/assign_repo

limit = 10**12
n = int(input("nhap n"))
i = 0
if (n >= 1 and n <= limit):
    while i <= n:
        i = i+1
        if (i != 1 and i != n and n % i == 0):
            print("NO")
            break
    else: print("YES")