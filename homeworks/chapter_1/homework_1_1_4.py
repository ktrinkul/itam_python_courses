if __name__ == '__main__':
    b = list(map(int, input().split(" ")))
    cotr = 0
    cb8 = 0
    cch = 0
    for i in b:
        if i<0:
            cotr += 1
        if i > 8:
            cb8 += 1
        if abs(i) % 2 == 0:
            cch += 1
print(cotr, cb8, cch)