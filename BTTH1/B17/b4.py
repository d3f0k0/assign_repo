if __name__ == "__main__":
    ss = int(input("nhap so giay"))
    sec = ss % 60
    minut = (ss // 60) % 60
    hour = (ss // 3600) % 24
    day = (ss // 3600) // 24
    print(day , "ngay" , hour ,"gio" , minut, "phut", sec, "giay")