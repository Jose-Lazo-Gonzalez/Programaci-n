lista=[]
b=1
for i in range (15):
    num=int(input("dame un numero"))
    if i==14:
        lista.insert(0,num)
    else:
        lista.insert(b,num)
    b+=1
    
        
print(lista)
