from bisect import bisect_left


def pos_search(lst, value):

    left = bisect_left(lst, value)

    if left < len(lst) and lst[left] == value:
        return left + 1
    else:
        return -1


def main():

    n, *N = [int(i) for i in input().split()]
    k, *K = [int(i) for i in input().split()]

    for k in K:
        print(pos_search(N, k), end=" ")


if __name__ == "__main__":
    main()
