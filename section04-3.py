# Section04-3
# 리스트, 튜플

# 리스트 (순서, 중복, 수정, 삭제) 가능
# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana']
e = [10, 100, ['Pen', 'Banana']]

# 인덱싱 (인덱싱의 범위를 지정하는 것은 슬라이싱)
print(d[3])
print(d[-1])
print(d[0] + d[1])
print(e[2][1])
print(e[-1][-1])

# 슬라이싱
print(d[0:3])
print(e[2][1:2])

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'Hi')

# 리스트 수정 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)

c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)

del c[-1]
print(c)

# 리스트 함수

y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2, 7)
print(y)
y.remove(2)
print(y)
y.pop
print(y)
ex = [88, 77]
y.extend(ex)
print(y)