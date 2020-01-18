# Section07-1
# 파이썬 클래스 상세 이해
# self, class, instense 변수

# 선언
class ClassCreate:
    pass

# ex1
class UserInfo:
    # 속성, 메소드
    def __init__(self, name):
        self.name = name
        print("초기화", name)
    def user_info_p(self):
        print("Name : ", self.name)


# 네임스페이스
user1 = UserInfo("Eun")
user1.user_info_p()
print(user1.name)
user2 = UserInfo("Pack")
user2.user_info_p()
print(user2.name)

print(id(user1))
print(id(user2))

print(user1.__dict__)
print(user2.__dict__)