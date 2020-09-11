# Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography.
# During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, or a downhill,  step.
# Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude.


test = ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']
test2 = ['D', 'D', 'U', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'D']

# 고도가 0이면서 up_hill일때가 산 1개를 넘은 것이므로 그때만 카운트 증가
def countingValleys(n, s):
    level = valleys = 0
    for step in s:
        level += 1 if step == "U" else -1
        valleys += level == 0 and step == "U"
    return valleys


print(countingValleys(len(test2), test2))
