# # [1] =====================
# # 체인법으로 해시 함수 구현하기
# from __future__ import annotations
# from typing import Any, Type
# import hashlib
#
# class Node:
#     """해시를 구성하는 노드"""
#     def __init__(self, key: Any, value: Any, next: Node) -> None:
#         """초기화"""
#         self.key = key
#         self.value = value
#         self.next = next
#
# class ChainedHash:
#     """체인법으로 해시 클래스 구현"""
#     def __init__(self, capacity: int) -> None:
#         """초기화"""
#         self.capacity = capacity                # 해시 테이블 크기 지정
#         self.table = [None] * self.capacity     # 해시 테이블(리스트) 선언
#
#     def hash_value(self, key: Any) -> int:
#         """해시값을 구함"""
#         if isinstance(key, int):
#             return key % self.capacity
#         return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
#
#     def search(self, key: Any) -> Any:
#         """키가 key인 원소를 검색하여 값을 반환"""
#         hash = self.hash_value(key)
#         p = self.table[hash]    # table[hash]가 가리키는 연결 리스트 찾아가기
#
#         while p is not None:
#             if p.key == key:
#                 return p.value
#             p = p.next
#
#         return None
#
#     def add(self, key: Any, value: Any) -> bool:
#         """키가 key이고 값이 value인 원소를 추가"""
#         hash = self.hash_value(key)
#         p = self.table[hash]
#
#         while p is not None:        # 연결 리스트
#             if p.key == key:
#                 return False
#             p = p.next
#
#         temp = Node(key, value, self.table[hash])   # 새로 초기화된 노드 객체
#         self.table[hash] = temp     # 노드를 추가
#         return True                 # 추가 성공
#
#     def remove(self, key: Any) -> bool:
#         """키가 key인 원소 삭제"""
#         hash = self.hash_value(key)
#         p = self.table[hash]
#         pp = None               # 바로 앞의 노드를 주목
#
#         while p is not None:
#             if p.key == key:
#                 if pp is None:
#                     self.table[hash] = p.next
#                 else:
#                     pp.next = p.next
#                 return True     # key 삭제 성공
#             pp = p
#             p = p.next
#         return False
#
#     def dump(self) -> None:
#         """해시 테이블을 덤프"""
#         for i in range(self, capacity):
#             p = self.table[i]
#             print(i, end='')
#             while p is not None:
#                 print(f'  → {p.key} ({p.value})', end='')
#                 p = p.next
#             print()

# # [2] =============================
# # 체인법을 구현하는 해시 클래스 ChainedHash
#
# from enum import Enum
# from chained_hash import ChainedHash
#
# Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료']) # 메뉴 선언
#
# def select_menu() -> Menu:
#     """메뉴 선택"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep='   ', end='')
#         n = int(input(': '))
#         if 1 <= n <= len(Menu):
#             return Menu(n)
#
# hash = ChainedHash(13)
#
# while True:
#     menu = select_menu()
#
#     if menu == Menu.추가:
#         key = int(input('추가할 키를 입력하세요 : '))
#         val = input('추가할 값을 입력하세요 : ')
#         if not hash.add(key, val):
#             print('추가를 실패했습니다!')
#
#     elif menu == Menu.삭제:
#         key = int(input('삭제할 키를 입력하세요 : '))
#         if not hash.remove(key):
#             print('삭제를 실패했습니다!')
#
#     elif menu == Menu.검색:
#         key = int(input('검색할 키를 입력하세요 : '))
#         t = hash.search(key)
#         if t is not None:
#             print(f'검색한 키를 갖는 값은 {t}입니다')
#         else:
#             print('검색할 데이터가 없습니다')
#
#     elif menu == Menu.덤프:
#         hash.dump()
#
#     else:
#         break


# # [3] =========================
# # 오픈 주소법으로 해시함수 구현하기
#
# from __future__ import annotations
# from typing import Any, Type
# from enum import Enum
# import hashlib
#
# # 버킷의 속성
# class Status(Enum):
#     OCCUPIIED = 0 # 데이터를 저장
#     EMPTY = 1 # 비어있음
#     DELETED = 2 # 삭제완료
#
# class Bucket:
#     """해시를 구성하는 버킷"""
#
#     def __init__(self, key: Any = None,
#                         value: Any = None,
#                         stat: Status = Status.EMPTY) -> None:
#         """초기화"""
#         self.key = key
#         self.value = value
#         self.stat = stat
#
#     def set(self, key: Any, value: Any, stat: Status) -> None:
#         """모든 필드에 값을 설정"""
#         self.key = key
#         self.value = value
#         self.stat = stat
#
#     def set_status(self, stat: Status) -> None:
#         """속성을 설정"""
#         self.stat = stat
#
# class OpenHash:
#     """오픈 주소법으로 구현하는 해시 클래스"""
#
#     def __init__(self, capacity: int) -> None:
#         self.capacity = capacity
#         self.table = [Bucket()] * self.capacity
#
#     def hash_value(self, key: Any) -> int:
#         """해시값을 구함"""
#         if isinstance(key, int):
#             return key % self.capacity
#         return(int(hashlib.md5(str(key).encode()).hexdigest, 16)
#                % self.capacity)
#
#     def rehash_value(self, key: Any) -> int:
#         """재해시값을 구함"""
#         return (self.hash_value(key) + 1) % self.capacity
#
#     def search_node(self, key: Any) -> Any:
#         """키가 key인 버킷을 검색"""
#         hash = self.hash_value(key)
#         p = self.table[hash]
#
#         for i in range(self.capacity):
#             if p.stat == Status.EMPTY:
#                 break
#             elif p.stat == Status.OCCUPIIED and p.key == key:
#                 return p
#             hash = self.rehash_value(hash)
#             p = self.table[hash]
#         return None
#
#     def search(self, key:Any) -> Any:
#         """키가 key인 원소를 검색하여 값을 반환"""
#         p = self.search_node(key)
#         if p is not None:
#             return p.value
#         else:
#             return None
#
#     def add(self, key: Any, value: Any) -> bool:
#         """키가 key이고 값이 value인 원소를 추가"""
#         if self.search(key) is not None:
#             return False
#
#         hash = self.hash_value(key)
#         p = self.table[hash]
#
#         for i in range(self.capacity):
#             if p.stat == Status.EMPTY or p.stat == Status.DELETED:
#                 self.table[hash] = Bucket(key, value, Status.OCCUPIED)
#                 return True
#             hash = self.rehash_value(key)
#             p = self.table[hash]
#         return False
#
#     def remove(self, key: Any) -> bool:
#         """키가 key인 원소를 삭제"""
#         p = self.search_node(key)
#         if p is None:
#             return False
#         p.set_status(Status.DELETED)
#         return True
#
#     def dump(self) -> None:
#         """해시 테이블을 덤프"""
#         for i in range(self.capacity):
#             print(f'{i:2} ', end='')
#             if self.table[i].stat == Status.OCCUPIED:
#                 print(f'{self.table[i].key} ({self.table[i].value})')
#             elif self.table[i].stat == Status.EMPTY:
#                 print('-- 미등록 --')
#             elif self.table[i].stat == Status.DELETED:
#                 print('-- 삭제 완료 --')

# [4] =========================
# 오픈 주소법을 구현하는 해시 클래스 Openhash 사용

from enum import Enum
from open_hash import OpenHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = OpenHash(13)

while True:
    menu = select_menu()

    if menu == Menu.추가:
        key = int(input('추가할 키를 입력하세요 : '))
        val = input('추가할 값을 입력하세요 : ')
        if not hash.add(key, val):
            print('추가를 실패했습니다!')

    elif menu == Menu.삭제:
        key = int(input('삭제할 키를 입력하세요 : '))
        if not hash.remove(key):
            print('삭제를 실패했습니다.')

    elif menu == Menu.검색:
        key = int(input('검색할 키를 입력하세요 : '))
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else:
            print('검색할 데이터가 없습니다.')

    elif menu == Menu.덤프:
        hash.dump()

    else:
        break


