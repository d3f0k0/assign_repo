#Author: Tran Nguyen Hanh
#https://github.com/d3f0k0/assign_repo

n = int(input("nhap n"))
i = 0
oddSum = 0
evenSum = 0
while i < n:
    if i % 2 == 0:
        evenSum = evenSum + i
    elif i % 2 != 0:
        oddSum = oddSum + i
    i = i+1
print("tong so chan va le tuong ung:")
print(evenSum)
print(oddSum)