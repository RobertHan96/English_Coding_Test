# You are in charge of the cake for a child's birthday.
# You have decided the cake will have one candle for each year of their total age.
# They will only be able to blow out the tallest of the candles.
# Count how many candles are tallest.


def birthdayCakeCandles(candles):
    candles = list(candles)
    _max = max(candles)
    return candles.count(_max)


test = [3, 2, 1, 3]
birthdayCakeCandles(test)
