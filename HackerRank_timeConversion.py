# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# 07:05:45PM => 19:05:45

test = '12:59:54PM'


def timeConversion(s):
    day_night = s[-2:]
    s = s[:-2]
    times = str(s).split(':')
    hour = int(times[0])
    if day_night == 'PM' and hour != 12:
        hour += 12
    if hour < 10:
        hour = "0{}".format(hour)
    if hour == 12 and day_night == 'AM':
        hour = '00'
    if hour == 12 and day_night == 'PM':
        hour = '12'

    return "{}:{}:{}".format(hour, times[1], times[2])


print(timeConversion(test))
