def merge_sort(lst):

    if len(lst) <= 1:
        return lst

    else:
        middle = int(len(lst) / 2)
        left = lst[:middle]
        right = lst[middle:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):

    global inversions
    lst = list()
    i, j = 0, 0
    len_left = len(left)

    while i < len_left and j < len(right):

        if left[i] <= right[j]:
            lst.append(left[i])
            i += 1

        else:
            lst.append(right[j])
            j += 1
            inversions += len_left - i

    lst += left[i:] + right[j:]

    return lst


def main():

    n = int(input())
    A = [int(i) for i in input().split()]

    merge_sort(A)
    print(inversions)


if __name__ == "__main__":
    inversions = 0
    main()
