if __name__ == "__main__":
    year = int(input("nhap so nam"))
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(year, "la nam nhuan")
    else:
        print(year, "ko phai la nam nhuan")