import random
a= random.randint(1,10)
b=int(input("adivina el numero:"))
while a!=b:
    print("error")
    a= random.randint(1,10)
    b=int(input("adivina el numero:"))
print ("ole ole los caracoles")