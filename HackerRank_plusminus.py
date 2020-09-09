def plusMinus(arr):
    negative = 0
    zero = 0
    positive = 0
    total = len(arr)

    for i in arr:
        if i <= 0:
            if i == 0:
                zero += 1
            else:
                negative += 1
        else:
            positive += 1
    print(format(positive/total, ".6f"), end='\n')
    print(format(negative/total, ".6f"), end='\n')
    print(format(zero/total, ".6f"))


test = [1, 1, 0, -1, -1]
test2 = [-4, 3, -9, 0, 4, 1]
print(plusMinus(test2))
