from functools import reduce


def exploreLambda():
    point = [(1, 3), (3, 5), (-8, 9)]

    pointSorted = sorted(point)
    print(pointSorted)

    pointSorted = sorted(point, key=lambda x: x[1])
    print(pointSorted)

    funcLambda = lambda x: x[0] + x[1]
    pointSorted = sorted(point, key=funcLambda)
    print(pointSorted)

    numbers = [1, 3, 5, 6, 8, 9, 10]
    square = map(lambda x: x * x, numbers)
    print(square)
    print(list(square))

    even = filter(lambda x: x % 2 == 0, numbers)
    print(list(even))

    product = reduce(lambda x, y: x * y, numbers)
    print(product)


# [(-8, 9), (1, 3), (3, 5)]
# [(1, 3), (3, 5), (-8, 9)]
# [(-8, 9), (1, 3), (3, 5)]
# <map object at 0x103660ee0>
# [1, 9, 25, 36, 64, 81, 100]
# [6, 8, 10]
# 64800

if __name__ == "__main__":
    exploreLambda()
