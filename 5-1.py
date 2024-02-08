# # [1] =====================
# # 양의 정수 n의 팩토리얼 구하기
#
# def factorial(n: int) -> int:
#     """양의 정수 n의 팩토리얼값을 재귀적으로 구함"""
#     if n > 0:
#         return n * factorial(n-1)
#     else:
#         return 1
#
# if __name__ == '__main__':
#     n = int(input('출력할 팩토리얼값을 입력하세요 : '))
#     print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')

# # [2] =====================
# # 양의 정수 n의 팩토리얼 구하기 (n이 음수이면 ValueError 예외 처리 발생)
# def factorial(n: int) -> int:
#     if n > 0:
#         return n * factorial(n-1)
#     elif n == 0:
#         return 1
#     else:
#         raise ValueError
#
# if __name__ == '__main__':
#     n = int(input('출력할 팩토리얼값을 입력하세요.'))
#     try:
#         print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')
#     except ValueError:
#         print(f'{n}의 팩토리얼은 구할 수 없습니다.')


# # [3] =====================
# # 유클리드 호제법으로 최대 공약수 구하기
#
# def gcd(x: int, y: int) -> int:
#     """정수값 x와 y의 최대 공약수를 반환"""
#     if y == 0:
#         return x
#     else:
#         return gcd(y, x % y)
#
# if __name__ == '__main__':
#     print('두 정숫값의 최대 공약수를 구합니다.')
#     x = int(input('첫 번째 정숫값을 입력하세요 : '))
#     y = int(input('두 번째 정숫값을 입력하세요 : '))
#
#     print(f'두 정숫값의 최대 공약수는 {gcd(x, y)}입니다.')
