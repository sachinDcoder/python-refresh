from collections import deque

def exploreDeque():
    queue = deque([])
    queue.append(1)
    queue.append(2)
    queue.append(3)

    print(queue)

    queue.appendleft(9)
    queue.appendleft(8)
    queue.appendleft(7)
    print(queue)

    queue.pop()
    print(queue)

    queue.popleft()
    print(queue)

    queue.extend([4, 56, 788])
    print(queue)

    queue.extendleft([-99, -67, -87])
    print(queue)

    queue.rotate(1)  # rotate one place to right
    print(queue)

    queue.rotate(-2)  # rotate two place to left
    print(queue)

exploreDeque()

#
# deque([1, 2, 3])
# deque([7, 8, 9, 1, 2, 3])
# deque([7, 8, 9, 1, 2])
# deque([8, 9, 1, 2])
# deque([8, 9, 1, 2, 4, 56, 788])
# deque([-87, -67, -99, 8, 9, 1, 2, 4, 56, 788])
# deque([788, -87, -67, -99, 8, 9, 1, 2, 4, 56])
# deque([-67, -99, 8, 9, 1, 2, 4, 56, 788, -87])

