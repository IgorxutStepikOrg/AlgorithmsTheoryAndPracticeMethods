def distance(str1, str2):

    len_str1 = len(str1)
    len_str2 = len(str2)

    if len_str1 < len_str2:
        return distance(str2, str1)

    prev = list(range(len_str2 + 1))

    for i, chunk1 in enumerate(str1, 1):

        curr = [i]

        for j, chunk2 in enumerate(str2, 1):
            curr.append(min((curr[-1] + 1), (prev[j] + 1), (prev[j - 1] + (chunk1 != chunk2))))

        prev = curr

    return prev[len_str2]


def main():

    a, b = input(), input()

    print(distance(a, b))


if __name__ == "__main__":
    main()
