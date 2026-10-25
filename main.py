#Câu 3.7
#a
while True:
    n=int(input("n="))
    if n<0:
        break
    giaithua=1
    i=1
    while i<=n:
        giaithua*=i
        i+=1
    print(f"n!={giaithua}")
#b
while True:
    n=int(input("n="))
    if n<0:
        break
    giaithua=1
    for i in range(1,n+1):
        giaithua*=i
    print(f"n!={giaithua}")
#Câu 3.8
m=input("")
n=int(input(""))
if 1<=n<=20:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(m, end=" ") 
        print()
#Câu 3.9
#a
n=int(input())
if 2<=n<=50:
    i=2
    while i<=n:
        print(i,end=" ")
        i+=2
#b
n=int(input())
if 2<=n<=50:
    for i in range(2,n+1,2):
        print(i, end=" ")
#Câu 3.10
#a
n=int(input("n="))
if n>=1:
    for i in range(1,n+1):
        print(i)
    print()
#b
n=int(input("n="))
if n>=1:
    m=0
    for i in range(1,n+1):
        print(i,end=" ")
        m+=1
        if m%5==0:
            print()
#c
n=int(input("n="))
if n>=1:
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j, end=" ")
        print()
#Câu 3.11
duong=0
am=0
while True:
    n=int(input())
    if n==0:
        break
    elif n>0:
        duong+=1
    else:
        am+=1
print(f"{duong} positive numbers")
print(f"{am} negative numbers")
#Câu 3.12
n=int(input())
if 0<=n<=10000:
    keycode="ABCDEFGHKL"
    ketqua=""
    for i in str(n):
        ketqua+=keycode[int(i)]
    print(ketqua)
