#Author: Tran Nguyen Hanh
#https://github.com/d3f0k0/assign_repo

if __name__ == "__main__":
    numIn = int(input("nhap so"))
    divList = []
    for i in range(1,numIn - 1):
        if numIn % i == 0:
            divList.append(i)
    print(divList)