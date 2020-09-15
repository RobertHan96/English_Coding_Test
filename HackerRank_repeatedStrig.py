test = 'abaabaabaa'
n = 10


def repeatedString(s, n):
    if n == 1 and s == 'a':
        return 1
    else:
        return s.count('a') * (n // len(s)) + s[:n % len(s)].count("a")
        # 7 / 1 + 0 => 7
        # s가 반복되는 구간내에서 'a'를 카운트하고 나눈 뒤에, 나머지 구간에서 'a'를 카운트한 값을 더함
        # 결과적으로 전체 패턴에서 a의 개수를 셀수 있음
