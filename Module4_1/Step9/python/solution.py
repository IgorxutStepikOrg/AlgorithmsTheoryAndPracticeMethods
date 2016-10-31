def main():

    points, tmp, result, lines = list(), list(), list(), dict()
    n = int(input())

    for num in range(n):
        l, r = map(int, input().split())
        points.append([l, 1, num])  # координата, тип (1 - левый, 2 - правый), номер отрезка
        points.append([r, 2, num])
        lines.update({num: 0})  # номер отрезка, покрытие (0 - не покрыт, 1 - покрыт)

    points.sort(key=lambda x: [x[0], x[1]])

    for point in points:

        if point[1] == 1:
            tmp.append(point[2])

        else:

            if lines[point[2]] == 1:
                continue

            else:
                result.append(point[0])

                for item in tmp:
                    lines[item] = 1

                tmp.clear()

    print("{0}\n{1}".format(len(result), " ".join(map(str, result))))


if __name__ == "__main__":
    main()
