def exploreList():
    fruits = ["apple", "banana", "mango"]
    print(fruits)

    fruits.append("papaya")
    print(fruits)

    pop = fruits.pop()
    print(pop)
    print(fruits)

    fruits.insert(1, "watermelon")
    print(fruits)

    print(fruits.index("watermelon"))
    print(fruits.index("banana"))

    fruits.remove("mango")
    print(fruits)

    fruits.reverse()
    print(fruits)

    fruits.sort()
    print(fruits)

    newFruits = sorted(fruits)
    print(newFruits)

    fruits.clear()
    print(fruits)

    numbers = [0] * 5
    print(numbers)

    numbers = [1, 3, 5, 7, 8]
    numbers2 = [9, 10]
    print(numbers + numbers2)

    print(numbers[:3])
    print(numbers[1:3])
    print(numbers[5:3])
    print(numbers[::2])  # every 2nd index
    print(numbers[::-1])  # reverse the list

    newNumber = numbers
    print(newNumber)

    numbers[0] = 10000
    print(newNumber)

    deepCopy1 = list(numbers)
    deepCopy2 = numbers[:]
    deepCopy3 = numbers.copy()

    print(deepCopy1)
    print(deepCopy2)
    print(deepCopy3)


exploreList()