# -*- coding: utf-8 -*-
"""
Auto-generated from Lec_2_student.ipynb
"""

# <a href="https://colab.research.google.com/github/ElionLAB/OOP_2026_Practice/blob/main/ch_02/src/Lec_2_student.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# 환경 설정 — Google Colab / 로컬 환경 자동 감지
import sys
IN_COLAB = 'google.colab' in sys.modules

if IN_COLAB:
    pass  # 이 노트북은 추가 패키지가 필요하지 않습니다.
else:
    print('로컬 환경: conda activate OOP 상태인지 확인하세요.')

# # Lecture 2: Python Basics & OOP 기초
# 
# **건국대학교 OOP (Python Object-Oriented Programming) — Spring 2026**
# 
# ---
# 
# ## 학습 목표
# 
# 1. Python 변수, 타입, 제어문 복습
# 2. 함수 정의와 스코프(LEGB) 이해
# 3. 핵심 데이터 구조 (list, tuple, dict, set) 활용
# 4. 클래스 기초: `__init__`, `self`, 인스턴스/클래스 속성
# 5. 상속, 다형성, 매직 메서드 입문
# 6. 모듈과 패키지 기초

# ---
# # Part 1: 슬라이드 코드 실습
# ---

# ## 실습 1: 변수 / 타입 / 제어문 복습
# 📖 **Slides 10-12**

# ### 1-1. Dynamic Typing (Slide 10)
# 
# Python은 **동적 타이핑(dynamic typing)** 언어입니다.  
# 같은 변수에 다른 타입의 값을 재할당할 수 있습니다.

# Dynamic typing demo
x = 42
print(f"x = {x}, type = {type(x)}")  # int

x = "Hello"
print(f"x = {x}, type = {type(x)}")  # str

x = [1, 2, 3]
print(f"x = {x}, type = {type(x)}")  # list

# ### 1-2. `type()`과 `isinstance()` (Slide 10)
# 
# - `type(obj)` — 객체의 정확한 타입을 반환
# - `isinstance(obj, cls)` — 상속 관계까지 고려하여 타입을 확인

# type() vs isinstance()
value = 3.14
print(type(value))                    # <class 'float'>
print(isinstance(value, float))       # True
print(isinstance(value, (int, float)))  # True — 여러 타입 확인 가능

# bool은 int의 서브클래스
print(type(True))                     # <class 'bool'>
print(isinstance(True, int))          # True — 상속 관계 반영

# ### 1-3. 제어문: if / elif / else (Slide 11)
# 
# 슬라이드의 `check_status` 함수 예제입니다.

def check_status(score: int) -> str:
    """점수에 따라 등급을 반환합니다."""
    if score >= 90:
        return "A — 우수"
    elif score >= 80:
        return "B — 양호"
    elif score >= 70:
        return "C — 보통"
    else:
        return "F — 노력 필요"


# 테스트
for s in [95, 82, 73, 55]:
    print(f"score={s:3d} → {check_status(s)}")

# ### 1-4. 반복문: for / while, break / continue (Slide 12)

# for 루프
fruits = ["사과", "바나나", "체리"]
for fruit in fruits:
    print(fruit)

print("---")

# range와 enumerate
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# while + break / continue
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue  # 짝수는 건너뜀
    if n > 7:
        break     # 7 초과면 종료
    print(n, end=" ")

print()  # 출력: 1 3 5 7

# ---
# ## 실습 2: 함수 정의 (LEGB, *args, **kwargs)
# 📖 **Slides 13, 56-58**

# ### 2-1. LEGB 스코프 규칙 (Slide 13)
# 
# Python은 이름을 찾을 때 **L → E → G → B** 순서로 탐색합니다.
# 
# - **L**ocal: 함수 내부
# - **E**nclosing: 바깥 함수 (중첩 함수에서)
# - **G**lobal: 모듈 수준
# - **B**uilt-in: `print`, `len` 등 내장 이름

# LEGB 스코프 데모
g_var = "Global"


def outer():
    e_var = "Enclosing"

    def inner():
        l_var = "Local"
        print(f"inner에서 l_var = {l_var}")     # Local
        print(f"inner에서 e_var = {e_var}")     # Enclosing
        print(f"inner에서 g_var = {g_var}")     # Global
        print(f"inner에서 len   = {len}")       # Built-in

    inner()


outer()

# ### 2-2. 기본 인자(Default Arguments) (Slide 56)

def greet(name: str, greeting: str = "안녕하세요") -> str:
    return f"{greeting}, {name}!"


print(greet("철수"))                    # 기본 인사말 사용
print(greet("영희", "반갑습니다"))       # 인사말 지정

# ### 2-3. `*args`와 `**kwargs` (Slides 57-58)

# *args — 가변 위치 인자
def add_all(*args):
    """임의 개수의 숫자를 모두 더합니다."""
    print(f"args = {args}, type = {type(args)}")
    return sum(args)


print(add_all(1, 2, 3))       # 6
print(add_all(10, 20, 30, 40))  # 100

# **kwargs — 가변 키워드 인자
def print_info(**kwargs):
    """키-값 쌍을 출력합니다."""
    print(f"kwargs = {kwargs}, type = {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


print_info(name="Alice", age=20, major="CS")

# *args와 **kwargs 함께 사용
def flexible(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")


flexible(1, 2, 3, 4, x=10, y=20)

# ### 2-4. Lambda 함수

# lambda — 이름 없는 간단한 함수
square = lambda x: x ** 2
print(square(5))  # 25

# 정렬에 활용
students = [("철수", 85), ("영희", 92), ("민수", 78)]
students_sorted = sorted(students, key=lambda s: s[1], reverse=True)
print(students_sorted)  # 점수 내림차순 정렬

# ---
# ## 실습 3: 핵심 데이터 구조
# 📖 **Slides 15-20**

# ### 3-1. List (리스트) (Slides 15-16)
# 
# - 순서가 있고, **가변(mutable)**
# - `append`, `extend`, 슬라이싱, 리스트 컴프리헨션

# List 기본 연산
numbers = [1, 2, 3]
numbers.append(4)          # 끝에 추가
print(numbers)             # [1, 2, 3, 4]

# 슬라이싱
print(numbers[1:3])        # [2, 3]
print(numbers[::-1])       # [4, 3, 2, 1] — 역순

# 리스트 컴프리헨션
squares = [x ** 2 for x in range(1, 6)]
print(squares)             # [1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)               # [0, 2, 4, 6, 8]

# ### 3-2. Tuple (튜플) (Slide 17)
# 
# - 순서가 있고, **불변(immutable)**
# - 언패킹(unpacking)에 자주 사용

# Tuple 기본
point = (3, 4)
print(point[0], point[1])  # 3 4

# 불변성 확인
try:
    point[0] = 10
except TypeError as e:
    print(f"TypeError 발생: {e}")

# 언패킹
x, y = point
print(f"x={x}, y={y}")

# 스왑에 활용
a, b = 1, 2
a, b = b, a
print(f"a={a}, b={b}")  # a=2, b=1

# ### 3-3. Dictionary (딕셔너리) (Slide 18)
# 
# - **키-값** 쌍, 키는 해시 가능(immutable)해야 함
# - `.get()`, `.items()`, `.keys()`, `.values()`

# Dictionary 생성과 접근
student = {"name": "철수", "age": 20, "major": "CS"}
print(student["name"])          # 철수

# .get() — 키가 없으면 기본값 반환 (KeyError 방지)
print(student.get("gpa", "N/A"))  # N/A

# 순회
for key, value in student.items():
    print(f"  {key}: {value}")

# 딕셔너리 컴프리헨션
sq_dict = {x: x ** 2 for x in range(1, 6)}
print(sq_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ### 3-4. Set (집합) (Slide 19)
# 
# - **중복 불허**, 순서 없음
# - 집합 연산: 교집합, 합집합, 차집합

# Set 기본
a = {1, 2, 3, 3, 2}
print(a)  # {1, 2, 3} — 중복 제거

b = {3, 4, 5}

# 집합 대수
print(f"교집합: {a & b}")       # {3}
print(f"합집합: {a | b}")       # {1, 2, 3, 4, 5}
print(f"차집합: {a - b}")       # {1, 2}
print(f"대칭차집합: {a ^ b}")   # {1, 2, 4, 5}

# 리스트에서 중복 제거
nums = [1, 1, 2, 3, 3, 3, 4]
unique = list(set(nums))
print(f"중복 제거: {sorted(unique)}")

# ### 3-5. Mutability vs Immutability 비교 (Slide 20)
# 
# | 타입 | Mutable? | 예시 |
# |------|----------|------|
# | `int`, `float`, `str`, `tuple` | Immutable | 값 변경 불가 |
# | `list`, `dict`, `set` | Mutable | 값 변경 가능 |

# Mutable vs Immutable

# Immutable — 문자열
s = "hello"
# s[0] = "H"  # TypeError!
s2 = "H" + s[1:]  # 새 문자열 생성
print(f"원본: {s}, 새 문자열: {s2}")

# Mutable — 리스트
lst = [1, 2, 3]
lst[0] = 100  # 제자리(in-place) 수정 가능
print(f"수정된 리스트: {lst}")

# 주의: mutable 객체의 별칭(aliasing)
a = [1, 2, 3]
b = a          # 같은 객체를 가리킴
b.append(4)
print(f"a = {a}")  # a도 변경됨! [1, 2, 3, 4]
print(f"a is b: {a is b}")  # True

# ---
# ## 실습 4: 클래스 기초 (Car 클래스 만들기)
# 📖 **Slides 23-24, 28, 37-39**

# ### 4-1. 가장 간단한 클래스 (Slide 37)

# 가장 간단한 클래스 — pass 사용
class Empty:
    pass


obj = Empty()
print(type(obj))  # <class '__main__.Empty'>

# ### 4-2. 동적으로 속성 추가하기 (Point 예제) (Slides 38-39)

# 동적 속성 추가 — Python은 허용하지만 권장하지는 않음
class Point:
    pass


p = Point()
p.x = 3
p.y = 4
print(f"Point({p.x}, {p.y})")
print(f"거리: {(p.x**2 + p.y**2)**0.5:.2f}")

# ### 4-3. `__init__` 생성자와 `self` (Slides 23-24)
# 
# - `__init__`: 인스턴스 생성 시 자동 호출되는 초기화 메서드
# - `self`: 인스턴스 자기 자신을 가리키는 참조

class Car:
    """자동차를 나타내는 클래스."""

    def __init__(self, make: str, model: str, speed: int = 0):
        self.make = make      # 제조사
        self.model = model    # 모델명
        self.speed = speed    # 현재 속도 (km/h)

    def accelerate(self, amount: int) -> None:
        """가속합니다."""
        self.speed += amount
        print(f"{self.make} {self.model}: 속도 → {self.speed} km/h")

    def brake(self, amount: int) -> None:
        """감속합니다."""
        self.speed = max(0, self.speed - amount)
        print(f"{self.make} {self.model}: 속도 → {self.speed} km/h")


# 인스턴스 생성
my_car = Car("Hyundai", "Sonata")
my_car.accelerate(60)
my_car.accelerate(40)
my_car.brake(30)
print(f"현재 속도: {my_car.speed} km/h")

# ### 4-4. 인스턴스 속성 vs 클래스 속성 (Slide 28)

class Dog:
    # 클래스 속성 — 모든 인스턴스가 공유
    species = "Canis familiaris"
    count = 0

    def __init__(self, name: str):
        # 인스턴스 속성 — 각 인스턴스 고유
        self.name = name
        Dog.count += 1  # 클래스 속성 수정


d1 = Dog("바둑이")
d2 = Dog("초코")

print(f"d1.species = {d1.species}")   # 클래스 속성 접근
print(f"d1.name = {d1.name}")         # 인스턴스 속성
print(f"d2.name = {d2.name}")
print(f"Dog.count = {Dog.count}")     # 2 — 클래스 속성으로 개수 추적

# ---
# ## 실습 5: 상속 & 다형성
# 📖 **Slides 25-29**

# ### 5-1. 상속 (Inheritance): Animal → Dog / Cat (Slide 25)

class Animal:
    """동물 기본 클래스."""

    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError("서브클래스에서 구현해야 합니다")


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: 멍멍!"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name}: 야옹~"


dog = Dog("바둑이")
cat = Cat("나비")
print(dog.speak())
print(cat.speak())
print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")  # True

# ### 5-2. 다형성 (Polymorphism) (Slide 26)

def make_animal_speak(animal: Animal) -> None:
    """어떤 Animal이든 speak()를 호출할 수 있습니다."""
    print(animal.speak())


# 다형성: 같은 인터페이스, 다른 동작
animals = [Dog("맥스"), Cat("루나"), Dog("찰리"), Cat("모모")]
for a in animals:
    make_animal_speak(a)

# ### 5-3. 캡슐화와 Name Mangling (Slide 27)
# 
# - `_var`: 관례상 private (접근 가능하지만 외부 사용 비권장)
# - `__var`: name mangling으로 `_ClassName__var`로 변환

class SecretAgent:
    def __init__(self, name: str, code: str):
        self.name = name
        self.__code = code  # name mangling 적용

    def reveal(self) -> str:
        return f"Agent {self.name}, code: {self.__code}"


agent = SecretAgent("Bond", "007")
print(agent.reveal())

# 직접 접근 시도
try:
    print(agent.__code)
except AttributeError as e:
    print(f"AttributeError: {e}")

# name mangling으로 접근 가능 (권장하지 않음)
print(f"mangled name: {agent._SecretAgent__code}")

# ### 5-4. 매직 메서드 입문 (`__str__`, `__add__`) (Slide 29)
# 
# 슬라이드의 **Vector** 클래스 예제입니다.

class Vector:
    """2D 벡터 클래스 — 매직 메서드 데모."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector({self.x!r}, {self.y!r})"

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __abs__(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)             # __str__ 호출
print(v1 + v2)        # __add__ 호출 → Vector(4, 6)
print(abs(v1))        # __abs__ 호출 → 5.0
print(repr(v2))       # __repr__ 호출

# ---
# ## 실습 6: 모듈 / 패키지 기초
# 📖 **Slides 60-68**

# ### 6-1. `import` 기본 (Slide 60)

import sys
import os

print(f"Python 버전: {sys.version}")
print(f"현재 디렉토리: {os.getcwd()}")
print(f"sys.path (처음 3개): {sys.path[:3]}")

# ### 6-2. `from X import Y` (Slide 60)

from math import pi, sqrt
from datetime import datetime

print(f"pi = {pi:.6f}")
print(f"sqrt(2) = {sqrt(2):.6f}")
print(f"현재 시각: {datetime.now()}")

# ### 6-3. `__name__ == "__main__"` 패턴 (Slide 60)
# 
# 모듈이 직접 실행될 때만 특정 코드를 실행하는 패턴입니다.
# 
# ```python
# # my_module.py
# def helper():
#     return "도우미 함수"
# 
# if __name__ == "__main__":
#     # 이 모듈을 직접 실행할 때만 실행됨
#     print(helper())
# ```

# 노트북에서는 __name__이 항상 "__main__"
print(f"__name__ = {__name__}")

# import한 모듈의 __name__은 모듈 이름
print(f"os.__name__ = {os.__name__}")
print(f"sys.__name__ = {sys.__name__}")

# ### 6-4. 패키지와 `__init__.py` (Slides 63-64)
# 
# 패키지는 모듈을 디렉토리로 구조화한 것입니다.
# 
# ```
# my_package/
# ├── __init__.py      # 패키지 초기화 (빈 파일도 가능)
# ├── module_a.py
# └── sub_package/
#     ├── __init__.py
#     └── module_b.py
# ```
# 
# - `__init__.py`가 있어야 Python이 디렉토리를 패키지로 인식합니다.
# - Python 3.3+ 에서는 **namespace package** (implicit)도 지원하지만, 명시적 `__init__.py`를 권장합니다.
# - `from my_package import module_a` 또는 `from my_package.sub_package import module_b` 형태로 import합니다.

# ---
# # Part 2: 응용 문제
# ---

# ## 응용 1 (하): FizzBuzz 함수 구현
# 
# **규칙**:
# - 3의 배수 → `"Fizz"`
# - 5의 배수 → `"Buzz"`
# - 15의 배수 → `"FizzBuzz"`
# - 그 외 → 숫자를 문자열로 반환

def fizzbuzz(n: int) -> str:
    """FizzBuzz 규칙에 따라 문자열을 반환합니다."""
    # TODO: 여기에 코드를 작성하세요
    pass

# 검증
assert fizzbuzz(15) == "FizzBuzz"
assert fizzbuzz(9) == "Fizz"
assert fizzbuzz(10) == "Buzz"
assert fizzbuzz(7) == "7"
assert fizzbuzz(30) == "FizzBuzz"

# 1~20까지 출력
for i in range(1, 21):
    print(f"{i:2d}: {fizzbuzz(i)}")

print("\nAll tests passed!")

# ---
# ## 응용 2 (중): BankAccount 클래스
# 
# **요구사항**:
# - `__init__(owner, balance=0)`: 계좌 소유자와 초기 잔액
# - `deposit(amount)`: 입금 (양수만 허용)
# - `withdraw(amount)`: 출금 (잔액 부족 시 `ValueError`)
# - `__str__`: 문자열 표현

class BankAccount:
    """간단한 은행 계좌 클래스."""
    # TODO: 여기에 코드를 작성하세요
    pass

# 검증
acc = BankAccount("철수", 1000)
print(acc)  # BankAccount(철수, balance=1000.00)

acc.deposit(500)
assert acc.balance == 1500
print(f"입금 후: {acc}")

acc.withdraw(200)
assert acc.balance == 1300
print(f"출금 후: {acc}")

# 잔액 부족 테스트
try:
    acc.withdraw(5000)
except ValueError as e:
    print(f"예외 발생 (정상): {e}")

# 음수 입금 테스트
try:
    acc.deposit(-100)
except ValueError as e:
    print(f"예외 발생 (정상): {e}")

print("\nAll tests passed!")

# ---
# ## 응용 3 (상): Iris Sample 클래스 뼈대 구현
# 
# **배경**: 교재(Python OOP, 4th Ed.)에서 다루는 Iris 데이터셋의 샘플을 나타내는 클래스입니다.
# 
# **요구사항**:
# - `Sample` 클래스: `sepal_length`, `sepal_width`, `petal_length`, `petal_width`, `species` 속성
# - `classify(classification)`: 분류 결과를 저장하는 상태 전이 메서드
# - `__repr__`: 디버깅용 문자열 표현

class Sample:
    """Iris 데이터셋의 샘플을 나타내는 클래스."""
    # TODO: 여기에 코드를 작성하세요
    pass

# 검증
s = Sample(5.1, 3.5, 1.4, 0.2, species="setosa")
print(repr(s))
assert s.sepal_length == 5.1
assert s.species == "setosa"
assert s.classification is None

# 분류 수행
s.classify("setosa")
assert s.classification == "setosa"
print(f"분류 결과: {s.classification}")
print(f"정답 여부: {s.species == s.classification}")

# species 없는 샘플 (테스트용)
unknown = Sample(6.3, 2.9, 5.6, 1.8)
print(repr(unknown))
assert unknown.species is None

unknown.classify("virginica")
print(f"미지 샘플 분류: {unknown.classification}")

print("\nAll tests passed!")

# ---
# ## 정리
# 
# 이번 강의에서 다룬 내용:
# 
# | 주제 | 핵심 키워드 |
# |------|-------------|
# | 변수/타입 | Dynamic typing, `type()`, `isinstance()` |
# | 제어문 | `if/elif/else`, `for`, `while`, `break/continue` |
# | 함수 | LEGB, `*args`, `**kwargs`, `lambda` |
# | 데이터 구조 | `list`, `tuple`, `dict`, `set`, mutability |
# | 클래스 기초 | `__init__`, `self`, 인스턴스/클래스 속성 |
# | 상속/다형성 | `super()`, 메서드 오버라이딩, 매직 메서드 |
# | 모듈/패키지 | `import`, `from`, `__name__`, `__init__.py` |
# 
# **다음 강의**: Chapter 3 — 클래스 설계 심화 (교재 Ch.2~3)

