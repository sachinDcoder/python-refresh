from collections import OrderedDict

def exploreOrderedDict():
    orderDict = OrderedDict()  # Preserve Insertion Order
    orderDict['a'] = 1
    orderDict['c'] = 1
    orderDict['b'] = 1
    orderDict['x'] = 1

    print(orderDict)


exploreOrderedDict()


# OrderedDict([('a', 1), ('c', 1), ('b', 1), ('x', 1)])