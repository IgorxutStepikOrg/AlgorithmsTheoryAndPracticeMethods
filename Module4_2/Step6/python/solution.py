def main():

    k, l = map(int, input().split())
    lst = list()

    for i in range(k):
        tmp = input().split(": ")
        lst.append([tmp[1], tmp[0]])

    code = input()
    decode = ""

    lst.sort()

    while True:

        for i in lst:

            if code.startswith(i[0]):
                decode += i[1]
                code = code[len(i[0]):]

        if code == "":
            break

    print(decode)

if __name__ == "__main__":
    main()
