# # [1] ===================
# # 이진 검색 알고리즘
# from typing import Any, Sequence
#
# def bin_search(a: Sequence, key: Any) -> int:
#     """시퀀스 a에서 key와 일치하는 원소를 이진검색"""
#     pl = 0
#     pr = len(a)-1
#
#     while True:
#         pc = (pl + pr) // 2
#
#         if a[pc] == key:
#             return pc
#         elif a[pc] < key:
#             pl = pc + 1
#         else:
#             pr = pc - 1
#
#         if pr < pl:
#             break
#
#     return -1
#
# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요 : '))
#     x = [None] * num
#
#     print('배열 데이터를 오름차순으로 입력하세요')
#     x[0] = int(input('x[0]: '))
#     for i in range(1, num):
#         while True:
#             x[i] = int(input(f'x[{i}]: '))
#             if x[i-1] <= x[i]:
#                 break
#
#     ky = int(input('검색할 값을 입력하세요: '))
#     idx = bin_search(x, ky)
#
#     if idx == -1:
#         print('검색값을 갖는 원소가 존재하지 않습니다.')
#     else:
#         print(f'검색값은 x[{idx}]에 있습니다.')


# [2] ===================
# 이진 검색 알고리즘의 실행 과정을 출력
from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진검색"""
    pl = 0
    pr = len(a)-1

    print('   |', end='')
    for i in range(len(a)):
        print(f'{i : 4}', end='')
    print()
    print('---+' + (4 * len(a) + 2) * '-')

    while True:
        # pc 계산
        pc = (pl + pr) // 2

        # pc, 범위 표시
        print('   |', end='')
        if pl != pc:
            print((pl * 4 + 2) * ' ' + '<-' + ((pc - pl) * 4-1) * ' ' + '+', end='')
        else:
            print((pc * 4 + 2) * ' ' + '<+', end='')
        if pc != pr:
            print(((pr-pc) * 4 -1) * ' ' + '->')
        else:
            print('->')

        # 배열 원소 표시
        print(f'{pc:3}|', end='')
        for i in range(len(a)):
            print(f'{a[i]:4}', end='')
        print('\n   |')

        # 이진 알고리즘
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1

        if pr < pl:
            break

    return -1

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num

    print('배열 데이터를 오름차순으로 입력하세요')
    x[0] = int(input('x[0]: '))
    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i-1] <= x[i]:
                break

    ky = int(input('검색할 값을 입력하세요: '))
    idx = bin_search(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')