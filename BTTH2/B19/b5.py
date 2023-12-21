if __name__ == "__main__":
    electric = int(input("nhap so dien"))
    if electric >= 0 and electric <= 50:
        price = electric * 1.578
    elif electric >= 51 and electric <= 100:
        price = electric * 1.734
    elif electric >= 101:
        price = electric * 2.014
    print("gia dien:" , price)