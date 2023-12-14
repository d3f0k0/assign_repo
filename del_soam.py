#Author: Tran Nguyen Hanh
#https://github.com/d3f0k0/assign_repo

if __name__ == "__main__":
    numArr = list(map(int, input("nhap cac so").split()))
    positiveList = []
    for i in range(len(numArr)):
        if (numArr[i] < 0) == False:
            positiveList.append(numArr[i])
    for j in range(len(positiveList)):
        print(positiveList[j], end=' ')