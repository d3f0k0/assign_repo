#Author: Tran Nguyen Hanh
#https://github.com/d3f0k0/assign_repo

limit = 10**6
m,n = map(int, input("nhap m n").split())
#x+y = m
g = 0
if (m >= 0 and n <= limit):
    while g <= m:
        c = m - g
        if (2 * g + 4 * c == n):
            print(g, end=" ")
            print(c)
            isFound = True
            break
        g = g + 1
    if isFound == False:
        print(-1)