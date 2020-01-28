# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# ex1
# 상속 기본
# 슈퍼클래스 (부모), 및 서브 클래스 (자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성 (종류, 회사, 맛, 면종류, 이름) : 부모

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tuple
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        print(super().show())
        return 'Car Info'

# 일반 사용
model1 = BmwCar('52','51','50')
print(model1.color) # 부모
print(model1.type)  # 부모
print(model1.car_name) # 자식
print(model1.show()) # 부모
print(model1.show_model()) # 자식

# Method Overriding
model2 = BenzCar('51','52','53')
print(model2.show())

# Parent Method Call
model3 = BenzCar('40','41','42')
print(model3.show())