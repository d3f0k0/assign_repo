#Author: Tran Nguyen Hanh
#https://github.com/d3f0k0/assign_repo

limit = 10**6
m,n,t = map(int, input("nhap m n t").split())
paidNum = 0
i = 0
if ((m > limit or m < 1 or n < 0 or t > limit) == False):
    while i <= n:
        if i % m != 0:
            paidNum = paidNum + 1
        i = i + 1
    cost = t * paidNum
    print(cost)