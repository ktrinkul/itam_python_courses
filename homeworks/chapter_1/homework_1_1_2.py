if __name__ == '__main__':
    b = list(map(int, input().split(" ")))
    max = b[0]
    min = b[0]
    for i in range(0, len(b)):
        if b[i]>max:
            max = b[i]
        if b[i]<min:
            min = b[i]
print(max, min)