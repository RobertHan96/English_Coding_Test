test = "...!@BaT  # *..y.abcdefghijklm"
test2 = '"z-+.^."'


def solution(new_id):
    answer = ''
    possible_char = ['-', '_', '.']
    if len(new_id) == 0:
        return 'a' * 3
    # 알파벳 소문자/숫자/지정한 특수문자인 경우에만 추천ID에 문자로 추가, 그 외에는 제거
    for i in list(new_id.lower()):
        if i.isalpha() or i.isnumeric():
            answer += i
        else:
            if i in possible_char:
                answer += i

    last_char = answer[-1]
    temp = ''
    for i in range(len(answer) - 1):
        if answer[i] == answer[i+1] and answer[i] == '.':
            pass
        else:
            temp += answer[i]

    # 마지막 인덱스가 . 이 아니라면 다시 추가
    answer = temp + last_char

    if len(answer) == 1 and answer.count('.'):
        return 'a' * 3
    if answer[0] == '.':
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]

    if len(answer) == 0:
        answer = 'a' * 3
    if len(answer) > 15:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]

    if len(answer) == 1:
        answer = answer[0] * 3
    if len(answer) < 3:
        answer += answer[-1]

    return answer


print(solution('..'))
