#Author: Tran Nguyen Hanh
#https://github.com/d3f0k0/assign_repo

if __name__ == "__main__":
    strList = list(map(str, input("Nhap cau").split()))
    strInv = []
    for i in range(0, len(strList)):
        strInv.append(strList[(len(strList) - 1) - i])
    print(strInv)