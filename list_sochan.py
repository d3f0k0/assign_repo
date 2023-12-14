#Author: Tran Nguyen Hanh
#https://github.com/d3f0k0/assign_repo

if __name__ == "__main__":
    numArr = list(map(int, input("nhap cac so").split()))
    evenList = []
    for i in range(len(numArr)):
        if numArr[i] % 2 == 0:
            evenList.append(numArr[i])
    print(evenList)