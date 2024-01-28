# # [1] =======
# a = [1,2,3]
# max = a[0]
# if a[1]>max: max = a[1]
# if a[2]>max: max = a[2]
# print(max)

# # [1'] =======
# a = [1,2,3,4]
# max = a[0]
# if a[1]>max: max = a[1]
# if a[2]>max: max = a[2]
# if a[3]>max: max = a[3]
# print(max)

# # [1''] =======
# def max_of(a):
#     max = a[0]
#     for i in range(1, len(a)):
#         if a[i] > max:
#             max = a[i]
#     return max
#
# a = [22, 57, 11, 91, 32]
# print(max_of(a))

# # [2] =======
# # 시퀀스 원소의 최댓값 출력하기
# from typing import Any, Sequence
#
# def max_of(a: Sequence) -> Any:
#     max = a[0]
#     for i in range(1, len(a)):
#         if a[i] > max:
#             max = a[i]
#     return max
#
# if __name__ == '__main__':
#     print('배열의 최댓값을 구합니다.')
#     num = int(input('원소 수를 입력하세요. : '))
#     x = [None]*num
#
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]값을 입력하세요. : '))
#
#     print(f'최댓값은 {max_of(x)}입니다.')

# # [3] =======
# # 배열 원소의 최댓값을 구해서 출력하기 (원솟값을 난수로 생성)
#
# import random
# from max import max_of
#
# print('난수의 최댓값을 구합니다.')
# num = int(input('난수의 개수를 입력하세요. : '))
# lo = int(input('난수의 최솟값을 입력하세요 : '))
# hi = int(input('난수의 최댓값을 입력하세요 : '))
# x = [None] * num
#
# for i in range(num):
#     x[i] = random.randint(lo, hi)
#
# print(f'{x}')
# print(f'이 가운데 최댓값은 {max_of(x)} 입니다.')

# # [4] =======
# # 각 배열 원소의 최댓값을 구해서 출력하기 (튜플, 문자열, 문자열 리스트)
#
# from max import max_of
#
# t = (4, 7, 5.6, 2, 3.14, 1) # 튜플
# s = 'string' # 문자열
# a = ['APPLE', 'STRAWBERRY', 'BANANA'] # 문자열 리스트
#
# print(f'{t}의 최댓값은 {max_of(t)}입니다.')
# print(f'{s}의 최댓값은 {max_of(s)}입니다.')
# print(f'{a}의 최댓값은 {max_of(a)}입니다.')

# # [5] =======
# # 리스트의 모든 원소를 스캔하기 (원소 수를 미리 파악)
#
# x = ['John', 'George', 'Paul', 'Ringo']
#
# for i in range(len(x)):
#     print(f'x[{i}] = {x[i]}')

# # [6] =======
# # 리스트의 모든 원소를 enumerate() 함수로 스캔하기
#
# x = ['John', 'George', 'Paul', 'Ringo']
#
# for i, name in enumerate(x):
#     print(f'x[{i}]={x[i]}')

# # [7] =======
# # 리스트의 모든 원소를 enumerate() 함수로 스캔하기 (1부터 카운트)
#
# x = ['John', 'George', 'Paul', 'Ringo']
#
# for i, name in enumerate(x,1):
#     print(f'{i}번째 = {name}')

# # [8] =======
# # 리스트의 모든 원소를 스캔하기 (인덱스 값을 사용하지 않음)
#
# x = ['John', 'George', 'Paul', 'Ringo']
#
# for i in x:
#     print(i)
#
# for i in x[::-1]: # 리스트 역순
#     print(i)

# # [5'] =======
# # 튜플의 모든 원소를 스캔하기 (원소 수를 미리 파악)
#
# x = ('John', 'George', 'Paul', 'Ringo')
#
# for i in range(len(x)):
#     print(f'x[{i}] = {x[i]}')

# # [6'] =======
# # 튜플의 모든 원소를 enumerate() 함수로 스캔하기
#
# x = ('John', 'George', 'Paul', 'Ringo')
#
# for i, name in enumerate(x):
#     print(f'x[{i}]={x[i]}')

# # [7'] =======
# # 튜플의 모든 원소를 enumerate() 함수로 스캔하기 (1부터 카운트)
#
# x = ('John', 'George', 'Paul', 'Ringo')
#
# for i, name in enumerate(x,1):
#     print(f'{i}번째 = {name}')

# # [8'] =======
# # 튜플의 모든 원소를 스캔하기 (인덱스 값을 사용하지 않음)
#
# x = ('John', 'George', 'Paul', 'Ringo')
#
# for i in x:
#     print(i)
#
# for i in reversed(x): # 튜플 역순
#     print(i)


# # [9] =======
# # 뮤터블 시퀀스 원소를 역순으로 정렬
#
# from typing import Any, MutableSequence
#
# def reverse_array(a: MutableSequence) -> None:
#     """뮤터블 시퀀스 a의 원소를 역순으로 정렬"""
#     n = len(a)
#     for i in range(n//2):
#         a[i], a[n-i-1] = a[n-i-1], a[i]
#
# if __name__ == '__main__':
#     print('배열 원소를 역순으로 정렬합니다.')
#     nx = int(input('원소 수를 입력하세요 : '))
#     x = [None]*nx
#
#     for i in range(nx):
#         x[i] = int(input(f'x[{i}]값을 입력하세요 : '))
#
#     reverse_array(x)
#
#     print('배열 원소를 역순으로 정렬했습니다.')
#     for i in range(nx):
#         print(f'x[{i}]={x[i]}')


# # [10] =======
# # 10진수 정수값을 입력받아 2~36진수로 변환하여 출력하기
#
# def card_conv(x: int, r: int) -> str:
#     """정수값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""
#     d = ''
#     dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     # n = len(str(x))
#
#     # print(f'{r:2} | {x:{n}d}')
#     while x > 0:
#         # print('   +' + (n+2)*'-')
#         # if x//r:
#         #     print(f'{r:2} | {x//r:{n}d} ... {x%r}')
#         # else:
#         #     print(f'   {x//r:{n}d} ... {x%r}')
#         d += dchar[x % r]
#         x //= r
#
#     return d[::-1]
#
# if __name__== '__main__':
#     print('10진수를 n진수로 변환합니다.')
#
#     while True:
#         while True:
#             no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요 : '))
#             if no > 0:
#                 break
#
#         while True: # 2 ~ 36
#             cd = int(input('어떤 진수로 변환할까요? : '))
#             if 2 <= cd <= 36:
#                 break
#
#         print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')
#
#         retry = input('한 번 더 변환할까요? (Y/N) : ')
#
#         if retry in {'N','n'}:
#             break

# # [11] =======
# # 1부터 n까지 정수의 합 구하기
# def sum_1ton(n):
#     """1부터 n까지 정수의 합"""
#     s = 0
#     while n > 0:
#         s += n
#         n -= 1
#     return s
#
# x = int(input('x의 값을 입력하세요 : '))
# print(f'1부터 {x}까지 정수의 합은 {sum_1ton(x)}입니다.')

# # [12] =======
# # 리스트에서 임의의 원솟값을 업데이트하기
#
# def change(lst, idx, val):
#     """lst[idx]의 값을 val로 업데이트"""
#     lst[idx] = val
#
# x = [11, 22, 33, 44, 55]
# print('x = ', x)
#
# index = int(input('업데이트할 인덱스를 선택하세요 : '))
# value = int(input('새로운 값을 입력하세요 : '))
#
# change(x, index, value)
# print(f'x = {x}')

# # [13] =======
# # 1,000 이하의 소수를 나열하기
#
# counter = 0
#
# for n in range(2, 1001):
#     for i in range(2, n):
#         counter += 1
#         if n % i == 0:
#             break
#     else: # 나누어 떨어지는 정수가 존재하지 않으면
#         print(n)
#
# print(f'나눗셈을 실행한 횟수 : {counter}')

# # [13'] =======
# # 1000 이하의 소수를 나열하기 (알고리즘 1)
#
# counter = 0
# ptr = 0
# prime = [None]*500
#
# prime[ptr] = 2
# ptr += 1
#
# for n in range(3, 1001, 2):
#     for i in range(1, ptr):
#         counter += 1
#         if n % prime[i] == 0:
#             break
#     else:
#         prime[ptr] = n
#         ptr += 1
#
# for i in range(ptr):
#     print(prime[i])
#
# print(f'나눗셈을 실행한 횟수 : {counter}')

# # [13''] =======
# # 1000 이하의 소수를 나열하기 (알고리즘 개선2)
#
# counter = 0
# prime = [2, 3]
# # ptr = 0
# # prime = [None]*500
# #
# # prime[ptr] = 2
# # ptr += 1
# #
# # prime[ptr] = 3
# # ptr += 1
#
# for n in range(5, 1001, 2):
#     i = 1
#
#     while prime[i] * prime[i] <= n:
#         counter += 2
#         if n % prime[i] ==0:
#             break
#         i += 1
#
#     else:
#         prime += [n]
#         # prime[ptr] = n
#         # ptr += 1
#         counter += 1
#
# for i in prime:
#     print(i)
# # for i in range(ptr):
# #     print(prime[i])
#
# print(f'곱셈과 나눗셈을 실행한 횟수 : {counter}')


# # [14] =======
# # 자료형을 정하지 않은 리스트 원소 확인하기
#
# x = [15, 64, 7, 3.14, [32, 55], 'ABC']
# for i in range(len(x)):
#     print(f'x[{i}] = {x[i]}')


