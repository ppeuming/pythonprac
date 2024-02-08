# # [1] =======================
# # 순수한 재귀 함수 구현하기
#
# def recur(n: int) -> int:
#     """순수한 재귀 함수 recur의 구현"""
#     if n > 0:
#         recur(n-1)
#         print(n)
#         recur(n-2)
#
# x = int(input('정숫값을 입력하세요 : '))
#
# recur(x)


# # [2] =========================
# # 순수한 재귀 함수 구현하기2
#
# def recur(n: int) -> int:
#     """순수한 재귀 함수 recur의 구현 (거꾸로 출력)"""
#     if n > 0:
#         recur(n-2)
#         print(n)
#         recur(n-1)
#
# x = int(input('정숫값을 입력하세요 : '))
#
# recur(x)

# # [3] ========================
# # 재귀 알고리즘의 비재귀적 표현 : 꼬리 재귀 제거하기
#
# def recur(n: int) -> int:
#     """꼬리 재귀를 제거한 recur() 함수"""
#     while n > 0:
#         recur(n-1)
#         print(n)
#         n = n-2 # recur(n-2)

# [4] =========================
# 스택으로 재귀 함수 구현하기 (재귀를 제거)

from stack import Stack

def recur(n: int) -> int:
    """재귀를 제거한 recur() 함수"""
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)
            n = n-1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n-2
            continue
        break

x = int(input('정수값을 입력하세요 : '))

recur(x)
