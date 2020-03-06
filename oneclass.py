import math
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
dta=b*b-4*a*c
if dta>=0 and a!=0:
    x1=(-b+math.sqrt(dta))/2/a
    x2=(-b-math.sqrt(dta))/2/a
    print("x1=%d" % x1)
    print("x2=%d" % x2)
elif dta==0:
    x1=x2=-c/b
    print("x=%d" % x1)
else:
    print("无解")