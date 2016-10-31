def main():

    n = int(input())
    lst = list()
    sum_tmp = n
    i = 1

    while sum_tmp > 0:

        if i < sum_tmp and (sum_tmp - i) < (i + 1):
            i = sum_tmp

        lst.append(i)
        sum_tmp -= i
        i += 1

    print("{0}\n{1}".format(len(lst), " ".join(map(str, lst))))


if __name__ == "__main__":
    main()
