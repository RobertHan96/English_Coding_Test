test = [1, 3, 5, 7, 9]


def miniMaxSum(arr):
    arr = list(arr)
    arr.sort()
    mini_sum = sum(arr[:-1])
    max_sum = sum(arr[1:])
    print(mini_sum, max_sum)


print(miniMaxSum(test))
