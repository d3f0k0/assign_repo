#Author: Tran Nguyen Hanh
#https://github.com/d3f0k0/assign_repo

if __name__ == "__main__":
    N = int(input("nhap n"))
    A = list(map(int, input("nhap cac day so a").split()))
    oddEven = []
    if len(A) == N:
        for i in range(N):
            if A[i] % 2 == 0:
                oddEven.append(0)
            elif A[i] % 2 != 0:
                oddEven.append(1)
    for j in range(len(oddEven)):
        print(oddEven[j], end=' ')