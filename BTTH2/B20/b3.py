if __name__ == "__main__":
    n  = int(input("nhap n"))
    f = 1
    s , t = 0
    for i in range(1, n):
        f = f*i
        s = s + (1/i)
        t = t + i**3
    print(f,s,t)