if __name__ == "__main__":
    a, t= map(float, input("nhap so tien a , thang t").split())
    i = 0
    while i <= t:
        intrest = a*(0.2/100)
        after = a + intrest
        i += 1
    print(after)
