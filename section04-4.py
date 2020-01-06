# Section04-3
# 딕셔너리, 집합

# 딕셔너리(dict) : 순서 X, 중복 X, 수정 O, 삭제 O

# key, value (형식으로 되어 있음)
# 선언
a = {'name' : 'Kim', 'phone': '010-7777-7777', 'birth': 2000101}
b = {0: 'Hello', 1: 'Hello Coding'}
c = {'arr' : [1, 2, 3, 4, 5]}

print(type(a))
print(a['name'])
print(a.get('name'))
print(a.get('address')) # get으로 활용해야함
print(c['arr'][1:3])

# 딕셔너리 추가
a['adress'] = 'Seoul'
print(a)

a['rank'] = [1, 2, 3]
a['rank2'] = (1, 2, 3, )
print(a)

# keys, values, items
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))

print(2 in b) # key 로 찾음
print('name2' not in a) # key 로 찾음


# 집합(Sets) (순서X, 중복X)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(l)


s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2)) # 교집합
print(s1 & s2) # 교집합

print(s1 | s2) # 합집합
print(s1.union(s2)) # 합집합

print(s1 - s2) # 차집합
print(s1.difference(s2)) # 차집합

# 추가
s3 = set([7, 8, 10, 15])
s3.add(18)
s3.add(15)
print(s3)

s3.remove(15)
print(s3)

print(type(s3))