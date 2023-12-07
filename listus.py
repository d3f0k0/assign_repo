#Author: Tran Nguyen Hanh
#https://github.com/d3f0k0/assign_repo

limit = 10**6
n = int(input("nhap n"))
i = 1
if n < limit:
    while i <= n:
        if n % i == 0:
            print(i, end=" ")
        i = i + 1
