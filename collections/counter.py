from collections import Counter


def exploreCounter():
    string = "aaaaaaaaaabbbbcccccc"
    counter = Counter(string)
    print(counter)
    print(counter.keys())
    print(counter.values())
    print(counter.most_common(2))
    print(counter.most_common(2)[0])
    print(counter.most_common(2)[0][0])
    print(list(counter.elements()))

    lst = [1, 2, 4, 5, 6]
    counterList = Counter(lst)
    print(counterList)
    print(counterList.keys())
    print(counterList.values())
    print(counterList.most_common(2))
    print(counterList.most_common(2)[0])
    print(counterList.most_common(2)[0][0])
    print(list(counterList.elements()))  # counterList.elements() gives iterator


exploreCounter()

# Counter({'a': 10, 'c': 6, 'b': 4})
# dict_keys(['a', 'b', 'c'])
# dict_values([10, 4, 6])
# [('a', 10), ('c', 6)]
# ('a', 10)
# a
# ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c']
# Counter({1: 1, 2: 1, 4: 1, 5: 1, 6: 1})
# dict_keys([1, 2, 4, 5, 6])
# dict_values([1, 1, 1, 1, 1])
# [(1, 1), (2, 1)]
# (1, 1)
# 1
# [1, 2, 4, 5, 6]