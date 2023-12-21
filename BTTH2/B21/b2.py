if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    i = 1
    while i <= len(alphabet):
        if i % 10 == 0 and i != 0:
            print(alphabet[i - 1])
        else:
            print(alphabet[i - 1], end=' ')
        i += 1