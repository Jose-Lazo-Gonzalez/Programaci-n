import random

a= random.randint(0,10)
b= random.randint(0,10)
print(a)
print(b)
c=a+b
d=int(input("dame un numerito:"))
while c!=d:
    print("error")
    d=int(input("dame un numerito:"))
print("FIN")
