def func(len, list):
    P = [0] * len
    M = [0] * (len + 1)
    L = 0
    list = list[:: -1]

    for i in range(len):
        lo = 1
        hi = L

        while lo <= hi:
            mid = (lo + hi) // 2

            if list[M[mid]] < list[i]:
                lo = mid + 1

            elif list[M[mid]] == list[i]:
                lo += 1

            else:
                hi = mid - 1

        newL = lo
        P[i] = M[newL - 1]

        if newL > L:
            M[newL] = i
            L = newL

        elif list[i] < list[M[newL]]:
            M[newL] = i

    # восстановление решения
    result = [0] * L
    k = M[L]
    for i in range(L - 1, -1, -1):
        result[i] = len - k
        k = P[k]

    return result


def main():
    n = int(input())
    A = [int(i) for i in input().split()]

    result = func(n, A)

    print("{0}\n{1}".format(len(result), " ".join(map(str, result[::-1]))))


if __name__ == "__main__":
    main()
