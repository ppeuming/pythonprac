# # [1] ======================================
# # 버블 정렬 알고리즘 구현하기
#
# from typing import MutableSequence
#
# def bubble_sort(a: MutableSequence) -> None:
#     """버블 정렬"""
#     n = len(a)
#     for i in range(n-1):
#         for j in range(n-1, i, -1):
#             if a[j-1] > a[j]:
#                 a[j-1], a[j] = a[j], a[j-1]
#
# if __name__ == '__main__':
#     print('버블 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요 : '))
#     x = [None] * num
#
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#
#     bubble_sort(x)
#
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')


# # [2] ======================================
# # 버블 정렬 알고리즘 구현하기 (정렬 과정을 출력)
#
# from typing import MutableSequence
#
# def bubble_sort_verbose(a: MutableSequence) -> None:
#     """버블 정렬(정렬 과정을 출력)"""
#     ccnt = 0    # 비교 횟수
#     scnt = 0    # 교환 횟수
#     n = len(a)
#     for i in range(n-1):
#         print(f'패스 {i+1}')
#         for j in range(n-1, i, -1):
#             for m in range(0, n-1):
#                 print(f'{a[m]:2}' + ('  ' if m != j-1 else
#                                      ' +' if a[j-1] > a[j] else ' -'),
#                                     end='')
#             print(f'{a[n-1]:2}')
#             ccnt += 1
#             if a[j-1] > a[j]:
#                 scnt += 1
#                 a[j-1], a[j] = a[j], a[j-1]
#         for m in range(0, n-1):
#             print(f'{a[m]:2}', end='  ')
#         print(f'{a[n-1]:2}')
#     print(f'비교를 {ccnt}번 했습니다.')
#     print(f'교환을 {scnt}번 했습니다.')
#
# if __name__=='__main__':
#     print('버블 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요 : '))
#     x = [None] * num
#
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#
#     bubble_sort_verbose(x)
#
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')


# # [3] =================================
# # 버블 정렬 알고리즘 구현하기 (알고리즘의 개선1)
#
# from typing import MutableSequence
#
# def bubble_sort_verbose(a: MutableSequence) -> None:
#     """버블 정렬(교환 횟수에 따른 중단)"""
#     ccnt = 0    # 비교 횟수
#     scnt = 0    # 교환 횟수
#     n = len(a)
#     for i in range(n-1):
#         print(f'패스 {i+1}')
#         exchng = 0  # 패스에서 교환 횟수
#         for j in range(n-1, i, -1):
#             for m in range(0, n-1):
#                 print(f'{a[m]:2}' + ('  ' if m != j-1 else
#                                      ' +' if a[j-1] > a[j] else ' -'),
#                                     end='')
#             print(f'{a[n-1]:2}')
#             ccnt += 1
#             if a[j-1] > a[j]:
#                 scnt += 1
#                 a[j-1], a[j] = a[j], a[j-1]
#                 exchng += 1
#         for m in range(0, n-1):
#             print(f'{a[m]:2}', end='  ')
#         print(f'{a[n-1]:2}')
#         if exchng == 0: # 현재 패스에서 교환이 없으면 종료
#             break
#     print(f'비교를 {ccnt}번 했습니다.')
#     print(f'교환을 {scnt}번 했습니다.')
#
# if __name__=='__main__':
#     print('버블 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요 : '))
#     x = [None] * num
#
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#
#     bubble_sort_verbose(x)
#
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')


# # [4] ======================================
# # 버블 정렬 알고리즘 구현하기 (알고리즘의 개선2)
#
# from typing import MutableSequence
#
# def bubble_sort_verbose(a: MutableSequence) -> None:
#     """버블 정렬(스캔 범위를 제한)"""
#     ccnt = 0    # 비교 횟수
#     scnt = 0    # 교환 횟수
#     n = len(a)
#     k = 0
#     i = 0
#
#     while k < n-1:
#         print(f'패스 {i + 1}')
#         i += 1
#         last = n-1
#         for j in range(n-1, k, -1):
#             for m in range(0, n-1):
#                 print(f'{a[m]:2}' + ('  ' if m != j-1 else
#                                      ' +' if a[j-1] > a[j] else ' -'),
#                     end='')
#             print(f'{a[n-1]:2}')
#             ccnt += 1
#             if a[j-1] > a[j]:
#                 scnt += 1
#                 a[j-1], a[j] = a[j], a[j-1]
#                 last = j
#         k = last
#         for m in range(0, n-1):
#             print(f'{a[m]:2}', end='  ')
#         print(f'{a[n-1]:2}')
#
#     print(f'비교를 {ccnt}번 했습니다.')
#     print(f'교환을 {scnt}번 했습니다.')
#
# if __name__=='__main__':
#     print('버블 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요 : '))
#     x = [None] * num
#
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))
#
#     bubble_sort_verbose(x)
#
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')


# [5] ==========================
# # 셰이커 정렬 알고리즘 구현하기
#
# from typing import MutableSequence
#
# def shaker_sort(a: MutableSequence) -> None:
#     """셰이커 정렬"""
#     left = 0
#     right = len(a) - 1
#     last = right
#     while left < right:
#         for j in range(right, left, -1):
#             if a[j-1] > a[j]:
#                 a[j-1], a[j] = a[j], a[j-1]
#                 last = j
#         left = last
#         for j in range(left, right):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#                 last = j
#         right = last


# # 셰이커 정렬 알구리즘 구현하기 (정렬 과정을 출력)
# from typing import MutableSequence
#
# def shaker_sort_verbose(a: MutableSequence) -> None:
#     """셰이커 정렬 (정렬 과정을 출력)"""
#     ccnt = 0 # 비교 횟수
#     scnt = 0 # 교환 횟수
#     n = len(a)
#     i = 0
#     left = 0
#     right = len(a) - 1
#     last = right
#     while left < right:
#         print(f'패스 {i+1}')
#         i += 1
#         for j in range(right, left, -1):
#             for m in range(0, n-1):
#                 print(f'{a[m]:2}' + ('  ' if m != j-1 else
#                                      ' +' if a[j-1] > a[j] else ' -'
#                                     ), end='')
#             print(f'{a[n-1]:2}')
#             ccnt += 1
#             if a[j-1] > a[j]:
#                 scnt += 1
#                 a[j-1], a[j] = a[j], a[j-1]
#                 last = j
#         left = last
#         for m in range(0, n-1):
#             print(f'{a[m]:2}', end='')
#         print(f'{a[n-1]:2}')
#
#         if (left == right):
#             break
#
#         print(f'패스 {i+1}')
#         i += 1
#         for j in range(left, right):
#             for m in range(0, n-1):
#                 print(f'{a[m]:2}' + ('  ' if m != j else
#                                      ' +' if a[j] > a[j+1] else ' -'
#                                     ), end='')
#             print(f'{a[n-1]:2}')
#             ccnt += 1
#             if a[j] > a[j+1]:
#                 scnt += 1
#                 a[j], a[j+1] = a[j+1], a[j]
#                 last = j
#         right = last
#         for m in range(0, n-1):
#             print(f'{a[m]:2}', end='  ')
#         print(f'{a[n-1]:2}')
#
#     print(f'비교를 {ccnt}번 했습니다.')
#     print(f'교환을 {scnt}번 했습니다.')
#
# if __name__ == '__main__':
#     print('셰이커 정렬을 수행합니다.')
#     num = int(input('원소 수를 입력하세요 : '))
#     x = [None] * num
#
#     for i in range(num):
#         x[i] = int(input(f'x[{i}] : '))
#
#     shaker_sort_verbose(x)
#
#     print('오름차순으로 정렬했습니다.')
#     for i in range(num):
#         print(f'x[{i}] = {x[i]}')

