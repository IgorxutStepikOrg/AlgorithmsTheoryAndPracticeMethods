def main():

    lst = list()
    money = 0
    n, W = map(int, input().split())

    for i in range(n):
        c, w = map(int, input().split())
        lst.append([c / w, w])

    lst.sort(reverse=True)

    for i in lst:

        if i[1] <= W:
            W = W - i[1]
            money += i[0] * i[1]

            if W == 0:
                break

        else:
            money += i[0] * W
            break

    print("%0.3f" % money)


if __name__ == "__main__":
    main()
