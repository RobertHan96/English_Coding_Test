# When she flips page , she sees pages  and .
# Each page except the last page will always be printed on both sides.
# The last page may only be printed on the front, given the length of the book.
# If the book is  pages long, and she wants to turn to page , what is the minimum number of pages she will turn?
# She can start at the beginning or the end of the book.

# 고려해야할 사항
'''
 1) 책의 맨 첫장은 1p 하나만 존재한다.
 2) 따라서 총 페이지수가 홀수라면 책의 마지막 장은 2장, 아니라면 마지막 장은 1장이다.
 3) 첫장에서 시작하는 것과, 마지막에서 시작하는 것중 목표 페이지까지 가는 거리가 짧은 곳을 선택한다.
 4) 이웃하는 페이지의 번호를 유의하면서 2p씩 넘기면서 목표 페이지에 도달했는지 체크한다. 
'''


def pageCount(n, p):
    from_beginning = p-1
    from_end = n-p
    answer = 0
    page = 1
    neighborhood_page = 0

    if n - p < 2 and n != 1 and n-p != 1:  # 찾으려는 페이지가 책의 시작, 또는 마지막 장일때 바로 리턴
        return answer
    if from_beginning < from_end:  # 앞에서부터 찾는게 빠른 경우
        while page < p:
            if page >= p or neighborhood_page == p:
                return answer
            else:
                answer += 1
                page += 2
                neighborhood_page = page - 1
    else:  # 뒤에서부터 찾는게 빠른 경우
        page = n
        if n % 2 == 1:  # 뒤에서부터 찾는 경우 이웃하는 페이지가 다를수 있으므로 홀/짝 여부 검사
            neighborhood_page = n-1
        while page > p:
            if page <= p or neighborhood_page == p:
                return answer
            else:
                answer += 1
                page -= 2
                neighborhood_page = page - 1

    return answer

# 매우 쉽게해결한 케이스, 2로 나눈 몫을 활용하면 한줄로 해결 가능..


def solution(n, p):
    print(min(p//2, n//2-p//2))


solution(5, 4)
