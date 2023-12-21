if __name__ == "__main__":
    n = int(input("n: "))
    if (n // 7) % 2 == 0:
        print("trai: ", 7 - n % 7, "phai: ", n % 7)
    else:
        print("trai: ", n % 7, "phai: ", 7 - n % 7)