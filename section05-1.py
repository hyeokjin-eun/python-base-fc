# Section05-1
# 파이썬 흐름제어(제어문)
# 조건문 실습

print(type(True))
print(type(False))

# ex1
if True:
    print("Yes")

# ex2
if False:
    print("No")
else:
    print("else")

# 관계 연산자
# >, >=, <, <=, ==, !=
a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print()

# 참 거짓 종료 (True, False)
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0

city = ""
if city:
    print("True")
else:
    print("False")

# 논리 연산자
# and or not
a = 100
b = 60
c = 15

print('and : ', a > b and b > c)
print('or : ', a > b or c > b)
print('not : ', not a > b)
print(not False)
print(not True)