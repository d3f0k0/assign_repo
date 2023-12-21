if __name__ == "__main__":
    x= int(input("nhap so x"))
    digit1 = x // 100
    digit2 = x // 10 % 10
    digit3 = x // 1 % 10
    s = digit1 + digit2 + digit3
    print(s)