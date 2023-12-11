from collections import deque


def build_next_level(arr):
    next_arr = []
    for i in range(0, len(arr), 2):
        next_arr.append(hash(arr[i] + arr[i + 1]))
    return next_arr


def build_merkle_tree(data_source):
    leaves = [val for val in data_source]
    levelByLevel = [leaves]
    while len(levelByLevel[-1]) > 1:
        if len(levelByLevel[-1]) % 2 == 1:
            levelByLevel[-1].append(levelByLevel[-1][-1])
        levelByLevel.append(build_next_level(levelByLevel[-1]))
    return levelByLevel


tree1 = build_merkle_tree([1, 2, 3, 2, 5, 6, 7, 8])
tree2 = build_merkle_tree([1, 2, 3, 4, 5, 6, 8, 8])


def find_disperancy(tree1, tree2):
    tree1.reverse()
    tree2.reverse()
    q = deque()
    q.append((0, 0))
    while q:
        l = len(q)
        for _ in range(l):
            level, index = q.popleft()
            if tree1[level][index] != tree2[level][index]:
                q.append((level + 1, index * 2))
                q.append((level + 1, index * 2 + 1))
        # if we are at the last level, then we are done
        if level + 1 == len(tree1) - 1:
            break

    ans = []
    for level, index in q:
        if tree1[level][index] != tree2[level][index]:
            ans.append((level, index))

    return ans


diffs = find_disperancy(tree1, tree2)

for level, index in diffs:
    print(f"Level: {level}, Index: {index}")
    print(f"Tree 1: {tree1[level][index]}")
    print(f"Tree 2: {tree2[level][index]}")
    print()
