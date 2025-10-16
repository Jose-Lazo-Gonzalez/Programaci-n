n1=int(input("dame un numerin"))
n2=int(input("dame otro numerin"))

while n1<11 or n2<11:
    print("error autista")
    n1=int(input("dame un numerin"))
    n2=int(input("dame otro numerin"))

if n1<n2:
    for i in range (0,n2+1,11):
        if i>n1:
            print(i)
elif n1>n2:
    for i in range (0,n1+1,11):
        if i>n2:
            print(i)