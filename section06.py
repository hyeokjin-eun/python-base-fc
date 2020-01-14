# Section05-1
# 함수식 및 람다

# 함수 정의 방법
# def 함수명 (parameter)
#   code

# 함수 호출
# 함수면(parameter)

# 함수 선언 위치 중요

# ex
def hello(world):
    print("Hello", world)

hello("Python!")
hello(7777)

# ex2 return

def hello_return(world):
    val = "Hello" + str(world)
    return val

str = hello_return("Python Return!")
print(str)

# ex3 다중 retrun

def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(1)
print(type(val1), val1, val2, val3)


# ex3 다중 retrun Data Type

def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul(1)
print(type(lt), lt)
