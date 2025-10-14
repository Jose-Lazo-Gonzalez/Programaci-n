a=int(input("dame un numero:"))
b=1
c=0
while b!=0:
    b=a%10
    print(b)
    a=a//10
    c+=b
print ("resultado:",c)
  
    
print ("fin")