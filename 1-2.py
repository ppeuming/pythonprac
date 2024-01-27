# # ========
# # 1부터 n까지 정수의 합 구하기 1 (while문)
#
# print('1부터 n까지 정수의 합을 구합니다.')
# n = int(input('n값을 입력하세요: '))
#
# sum = 0
# i =1
#
# while i<=n:
#     sum += i
#     i += 1
#
# print(f'i값은 {i}입니다.')
# print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

# # ========
# # 1부터 n까지 정수의 합 구하기 1 (for문)
# print('1부터 n까지 정수의 합을 구합니다.')
# n = int(input('n값을 입력하세요 : '))
#
# sum = 0
# for i in range(1, n+1):
#     sum += i
#
# print(f'1부터 n까지 정수의 합은 {sum}입니다.')

# # ========
# # a부터 b까지 정수의 합 구하기 (for문)
#
# print('a부터 b까지 정수의 합을 구합니다.')
# a = int(input('정수 a를 입력하세요. : '))
# b = int(input('정수 b를 입력하세요. : '))
#
# if a>b:
#     a, b = b, a
#
# sum = 0
# for i in range(a,b+1):
#     sum += i
#
# print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')

# # ========
# # a부터 b까지 정수의 합 구하기 1
#
# print('a부터 b까지 정수의 합을 구합니다.')
# a = int(input('정수 a를 입력하세요 : '))
# b = int(input('정수 b를 입력하세요 : '))
#
# if a>b:
#     a, b = b, a
#
# # sum = 0
# # for i in range(a, b+1):
# #     if i<b:
# #         print(f'{i} + ', end='')
# #     else:
# #         print(f'{i} = ', end='')
# #     sum += i
# #
# # print(sum)
#
# sum = 0
# for i in range(a, b):
#     print(f'{i} + ', end='')
#     sum += i
#
# print(f'{b} = ', end='')
# sum += b
#
# print(sum)

# # ========
# # +와 -를 번갈아 출력하기 1
#
# print('+와 -를 번갈아 출력합니다.')
# n = int(input('몇 개를 출력할까요? : '))
#
# # for i in range(n):
# #     if i%2:
# #         print('-', end='')
# #     else:
# #         print('+', end='')
# # print()
#
# for i in range(1,n+1):
#     if i%2:
#         print('+', end='')
#     else:
#         print('-', end='')

# # ========
# # +와 -를 번갈아 출력하기 2
#
# print('+와 -를 번갈아 출력합니다.')
# n = int(input('몇 개를 출력할까요? : '))
#
# for _ in range(n//2): # for _ in range(1,n//2+1)
#     print('+-', end='')
#
# if n%2:
#     print('+', end='')
#
# print()

# # ========
# # *를 n개를 출력하되 w개마다 줄바꿈하기 1
#
# print('*를 출력합니다.')
# n = int(input('몇 개를 출력할까요? : '))
# w = int(input('몇 개마다 줄바꿈할까요? : '))
#
# # for i in range(n):
# #     print('*', end='')
# #     if i % w == w-1:
# #         print()
# # if n % w:
# #     print()
#
# for _ in range(n//w):
#     print('*'*w)
#
# rest = n%w
# if rest:
#     print('*'*rest)

# # ========
# # 1부터 n까지 정수의 합 구하기 (n값은 양수만 입력받음)
#
# print('1부터 n까지 정수의 합을 구합니다.')
#
# while True:
#     n = int(input('n값을 입력하세요. : '))
#     if n>0:
#         break
#
# sum = 0
# i=1
#
# for i in range(1,n+1):
#     sum += i
#     i += 1
#
# print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

# # ========
# # 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기
#
# area = int(input('직사각형의 넓이를 입력하세요. : '))
#
# for i in range(1, area+1):
#     if i*i>area: break
#     if area%i: continue
#     print(f'{i} x {area//i}')

# # ========
# # 10~99 사이의 난수 n개 생성하기 (13이 나오면 중단)
#
# import random
#
# n = int(input('난수의 개수를 입력하세요 : '))
#
# for _ in range(n):
#     r = random.randint(10, 99)
#     print(r, end=' ')
#     if r == 13:
#         print('\n프로그램을 중단합니다.')
#         break
# else:
#     print('\n난수 생성을 종료합니다.')

# # ========
# # 1~12까지 8은 건너뛰고 출력하기 1
#
# for i in range(1,13):
#     if i == 8: continue
#     print(i, end=' ')
#
# print()

# # ========
# # 1~12까지 8은 건너뛰고 출력하기 2
#
# for i in list(range(1,8))+list(range(9,13)):
#     print(i, end=' ')
# print()

# # ========
# # 2자리 양수(10~99) 입력받기
#
# print('2자리 양수를 입력하세요.')
#
# while True:
#     no = int(input('값을 입력하세요 : '))
#     if no>=10 and no<=99: # not(no<10 or no>99)
#         break
# print(f'입력받은 양수는 {no}입니다.')

# # ========
# # 구구단 곱셈표 출력하기
#
# print('-'*27)
# for i in range(1,10):
#     for j in range(1,10):
#         print(f'{i*j:3}', end='')
#     print()
# print('-'*27)

# # ========
# # 왼쪽 아래가 직각인 이등변 삼각형으로 * 출력하기
#
# print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
# n = int(input('짧은 변의 길이를 입력하세요. : '))
#
# for i in range(n):
#     for j in range(i+1):
#         print('*', end='')
#     print()

# # ========
# # 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기
#
# print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
# n = int(input('짧은 변의 길이를 입력하세요. : '))
#
# for i in range(n):
#     for _ in range(n-i-1):
#         print(' ',end='')
#     for _ in range(i+1):
#         print('*', end='')
#     print()

# # ========
# # 함수 내부, 외부에서 정의한 변수와 객체의 식별번호 출력하기
#
# n = 1       # 전역 변수 (함수 내부, 외부에서 사용)
# def put_id():
#     x = 1   # 지역 변수 (함수 내부에서만 사용)
#     print(f'id(x) = {id(x)}')
#
# print(f'id(1) = {id(1)}')
# print(f'id(n) = {id(n)}')
# put_id()

# ========
# 1부터 100까지 반복하여 출력하기
for i in range(1,101):
    print(f'i = {i:3} id(i) = {id(i)}')

