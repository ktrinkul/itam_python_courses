if __name__ == '__main__':
    str = input()
    mas = list(str)
    print(mas)
    if len(mas) >= 5:
        x = slice(2, 4)
        print(mas[x])
    else:
        print(mas[::-1])
