# John works at a clothing store.
# He has a large pile of socks that he must pair by color for sale.
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

test = [10, 20, 20, 10, 10, 30, 50, 10, 20]


def sockMerchant(n, ar):
    checked = [0] * 101
    answer = 0
    for num in ar:
        checked[num] += 1
    print(checked)
    for num in checked:
        mok = num // 2
        if mok != 0:
            answer += mok
    return answer


print(sockMerchant(9, test))
