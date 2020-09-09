test = [[1, 2, 3, 4],  # 0, 1, 2, 3
        [4, 5, 6, 7],  # 1, 2, 3, 4
        [9, 8, 9, 9],  # 2, 3, 4, 5
        [4, 5, 6, 7]   # 3, 4, 5, 6
        ]


def diagonalDifference(arr):
    # Write your code here
    left_diagonal = 0
    right_diagonal = 0
    first_index = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i + j == len(arr[i]) - 1:
                right_diagonal += arr[i][j]
            if i == first_index and j == first_index:
                left_diagonal += arr[i][j]
                first_index += 1
    return abs(left_diagonal-right_diagonal)


print(diagonalDifference(test))
