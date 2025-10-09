import random

a=random.randint(0,10)
b=random.randint(0,10)
c=a+b
print(a)
print(b)
d=int(input("introduce el resultado"))
while d!=c:
    print("error")
    d=int(input("introduce el resultado"))
print("muy bien")