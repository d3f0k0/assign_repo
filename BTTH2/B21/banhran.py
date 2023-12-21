if __name__ == "__main__":
    n, k = map(int, input("so banh can ran, kha nang ran ").split())
    a = 2 * n // k
    b = 2 * n % k
    if n <= k:
        print("thoi gian: ", 10)
    elif b != 0:
        a += 1
        print("thoi gian: ", a * 5)
    else:
        print("thoi gian:", a * 5)