from math import sqrt

a=int(input())
b=int(input())
c=int(input())

D=b**2-4*a*c
if D<0:
    print("Нет корней")
elif D==0:
    print(-b/(2*a))
else:
    print(-b+sqrt(D)/(2*a))
    print(-b-sqrt(D)/(2*a))