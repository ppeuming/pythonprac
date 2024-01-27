# # 세 정수를 입력받아 최대값 구하기
#
# print('세 정수의 최대값을 구합니다')
# a = int(input('정수 a의 값을 입력하세요 : ')) // 문자열을 입력받아 정수형으로 변환
# b = int(input('정수 b의 값을 입력하세요 : '))
# c = int(input('정수 c의 값을 입력하세요 : '))
#
# max = a
# if (b>max): max = b
# if (c>max): max = c
#
# print(f'최댓값은 {max}입니다.')

# # ========
# # 이름을 입력받아 인사하기
#
# # print('이름을 입력하세요 : ', end='')
# # name = input() // 입력받는 값은 문자열
#
# name = input('이름을 입력하세요 : ') // 한번에 처리
#
# print(f'안녕하세요? {name}님.')

# # ========
# # 세 정수의 최댓값 구하기
#
# def max3(a,b,c):
#   max = a
#   if b > max: max = b
#   if c > max: max = c
#   return max
#
# print(f'max3(3,2,1)={max3(3,2,1)}')

# # ========
# # 세 정수를 입력받아 중앙값 구하기 1
# def med3(a,b,c):
#   if a>=b:
#     if b>=c: 
#       return b
#     elif a<=c: # a>=b, b<c
#       return a
#     else: 
#       return c
#   elif a>c: # a<b
#     return a
#   elif b>c: # a<b, a<=c
#     return c
#   else:
#     return b
#
# print('세 정수의 중앙값을 구합니다.')
# a = int(input('정수 a의 값을 구하세요. : '))
# b = int(input('정수 b의 값을 구하세요. : '))
# c = int(input('정수 c의 값을 구하세요. : '))
#
# print(f'중앙값은 {med3(a,b,c)}입니다.')

# # ========
# # 세 정수를 입력받아 중앙값 구하기 2
# def med3(a,b,c):
#   if (b>=a and a>=c) or (c>=a and a>=b):
#     return a
#   elif (a>b and b>c) or (c>b and b>a):
#     return b
#   return c
#
# print('세 정수의 중앙값을 구합니다.')
# a = int(input('정수 a의 값을 구하세요. : '))
# b = int(input('정수 b의 값을 구하세요. : '))
# c = int(input('정수 c의 값을 구하세요. : '))
#
# print(f'중앙값은 {med3(a,b,c)}입니다.')

# # ========
# # 입력받은 정수의 부호(양수, 음수, 0) 출력하기
#
# n = int(input('정수를 입력하세요: '))
#
# if n>0:
#   print('이 수는 양수입니다.')
# elif n<0:
#   print('이 수는 음수입니다.')
# else:
#   print('이 수는 0입니다.')

# # ========
# # 3개로 분기하는 조건문
#
# n = int(input('정수를 입력하세요 : '))
#
# if n == 1:
#   print('A')
# elif n ==2:
#   print('B')
# else:
#   print('C')

# # ========
# # 4개로 분기하는 조건문
#
# n = int(input('정수를 입력하세요 : '))
#
# if n == 1:
#   print('A')
# elif n == 2:
#   print('B')
# elif n == 3:
#   print('C')
# # else:
# #   pass

