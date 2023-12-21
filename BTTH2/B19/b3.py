if __name__ == "__main__":
    amount = int(input("nhap khoi luong cam"))
    if amount < 5:
        price = amount*12000
    else:
        price = amount*10000
    print(price)