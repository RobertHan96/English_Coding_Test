from itertools import combinations
from difflib import SequenceMatcher

od = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4, ]


def solution(orders, course):
    answer = []
    table = {}
    for i in course:
        table[i] = []

    for i in range(len(orders)):
        temp = []
        if i + 1 in table.keys():
            for j in range(len(orders[i])):
                temp.append(orders[i][j])
            table[i+1] = temp

    return table

    # a = "XYZ"
    # aa = "XWY"
    # result = SequenceMatcher(None, a, aa).find_longest_match(0, len(a), 0, len(aa))


print(solution(od, course))
