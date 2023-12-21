if __name__ == "__main__":
    n = int(input("nhap so n"))
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")