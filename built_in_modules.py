import math, random, platform

def sqroot(num):
    return math.sqrt(num)

def random_num():
    return random.randint(1, 1000)

def p_version_os():
    return platform.version(), platform.system(), platform.python_version_tuple()

print(round(sqroot(121)))
print(random_num())
print(*p_version_os())