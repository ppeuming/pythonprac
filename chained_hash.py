# 체인법으로 해시 함수 구현하기
from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """해시를 구성하는 노드"""
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    """체인법으로 해시 클래스 구현"""
    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity                # 해시 테이블 크기 지정
        self.table = [None] * self.capacity     # 해시 테이블(리스트) 선언

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)
        p = self.table[hash]    # table[hash]가 가리키는 연결 리스트 찾아가기

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:        # 연결 리스트
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])   # 새로 초기화된 노드 객체
        self.table[hash] = temp     # 노드를 추가
        return True                 # 추가 성공

    def remove(self, key: Any) -> bool:
        """키가 key인 원소 삭제"""
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None               # 바로 앞의 노드를 주목

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True     # key 삭제 성공
            pp = p
            p = p.next
        return False

    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  → {p.key} ({p.value})', end='')
                p = p.next
            print()

