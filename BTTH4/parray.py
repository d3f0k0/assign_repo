#Author: Tran Nguyen Hanh
#https://github.com/d3f0k0/assign_repo

if __name__ == "__main__":
    limit = 100000
    N = int(input("nhap n"))
    sumAB = []
    A = list(map(int, input("nhap cac so day a").split()))
    B = list(map(int, input("nhap cac so day b").split()))
    if (len(A) == len(B) == N):
        for i in range(N):
            sumAB.append(A[i] + B[i])
    for j in range(len(sumAB)):
        print(sumAB[j], end=' ')
