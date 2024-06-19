from collections import defaultdict


def exploreDefaultDict():
    d = defaultdict(list)
    d['a'] = 1

    print(d)
    print(d['a'])
    print(d['x'])
    print(d['v'])
    print(d['c'])

    d['x'] = 4
    print(d['x'])

    d = defaultdict(list)
    d['a'] = [1]

    print(d)
    print(d['a'])
    print(d['x'])
    print(d['v'])
    print(d['c'])

    d['x'] = [4]
    print(d['x'])


exploreDefaultDict()

# defaultdict(<class 'list'>, {'a': 1})
# 1
# []
# []
# []
# 4
# defaultdict(<class 'list'>, {'a': [1]})
# [1]
# []
# []
# []
# [4]