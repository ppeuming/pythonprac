# # [1] =======
# # while (for) 문으로 작성한 선형 검색 알고리즘
# from typing import Any, Sequence
#
# def seq_search(a: Sequence, key: Any) -> int:
#     """시퀀스 a에서 key와 같은 원소를 선형검색 (while문)"""
#     i = 0
#
#     while True:
#         if i == len(a):
#             return -1
#         if a[i] == key:
#             return i
#         i += 1
#
#     # """시퀀스 a에서 key와 같은 원소를 선형검색 (for문)"""
#     # for i in range(len(a)):
#     #     if a[i] == key:
#     #         return i
#     # return -1
#
# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요 : '))
#     x = [None] * num
#
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))  # int
#
#     ky = int(input('검색할 값을 입력하세요 : '))  # int
#
#     idx = seq_search(x, ky)
#
#     if idx == -1:
#         print('검색값을 갖는 원소가 존재하지 않습니다.')
#     else:
#         print(f'검색값은 x[{idx}]에 있습니다.')


# # [2] =======
# # seq_search() 함수를 사용하여 실수 검색하기
# from seqsearch import seq_search
#
# print('실수를 검색합니다.')
# print('주의: "End"를 입력하면 종료합니다.')
#
# number = 0
# x = []
#
# while True:
#     s = input(f'x[{number}] : ')
#     if s == 'End':
#         break
#     x.append(float(s))    # float
#     number += 1
#
# ky = float(input('검색할 값을 입력하세요 : '))  # float
#
# idx = seq_search(x, ky)
# if idx == -1:
#     print('검색값을 갖는 원소가 존재하지 않습니다.')
# else:
#     print(f'검색값은 x[{idx}]에 있습니다.')


# # [3] =======
# # seq_search() 함수를 사용하여 특정 인덱스 검색하기
# from seqsearch import seq_search
#
# t = (4, 7, 5.6, 2, 3.14, 1)
# s = 'string'
# a = ['DTS', 'AAC', 'FLAC']
#
# print(f'{t}에서 5.6의 인덱스는 {seq_search(t, 5.6)}입니다.')
# print(f'{s}에서 "n"의 인덱스는 {seq_search(s, "n")}입니다.')
# print(f'{a}에서 "DTS"의 인덱스는 {seq_search(a, "DTS")}입니다.')


# # [4] =======
# # 앞의 선형 검색 알고리즘을 보초법으로 수정
# from typing import Any, Sequence
# import copy
#
# def seq_search(seq: Sequence, key: Any) -> int:
#     """시퀀스 seq에서 key와 일치하는 원소를 선형검색 (보초법)"""
#     a = copy.deepcopy(seq)
#     a.append(key)
#
#     i = 0
#     while True:
#         if a[i] == key:
#             break
#         i += 1
#
#     return -1 if i == len(seq) else i
#
# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요 : '))
#     x = [None] * num
#
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]'))
#
#     ky = int(input('검색할 값을 입력하세요 : '))
#
#     idx = seq_search(x, ky)
#
#     if idx == -1:
#         print('검색값을 갖는 원소가 존재하지 않습니다.')
#     else:
#         print(f'검색값은 x[{idx}]에 있습니다.')


from typing import Sequence, Any
import copy

def seq_search(seq: Sequence, key: Any) -> int:

    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1

    return -1 if i == len(seq) else i

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    ky = int(input('검색할 값을 입력하세요 : '))

    idx = seq_search(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')

# [5] =======

