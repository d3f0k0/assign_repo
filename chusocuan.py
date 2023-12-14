#Author: Tran Nguyen Hanh
#https://github.com/d3f0k0/assign_repo

if __name__ == "__main__":
    numIn = int(input("nhap so n"))
    numDigitArray = []
    numDigitArrayInv = []
    for i in range(0, 10):
        if (numIn - 10**i < 0) == False:
            digit = numIn // 10**i % 10
            numDigitArrayInv.append(digit)
    for j in range(0, len(numDigitArrayInv)):
        numDigitArray.append(numDigitArrayInv[(len(numDigitArrayInv) - 1) - j])
    print(numDigitArray)