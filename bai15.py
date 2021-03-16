a=input('nhap a:')
b=input('nhap b:')
c=input('nhap c:')
d=b*b-4*a*c
if  d>0:
    x1=(-b-sqrt(d))/(2*a)
    x2=(-b+sqrt(d))/(2*a)
    print('chuong tring có hai nghiem phan biet x1,x2',x1,x2)
elif d==0:
    x1=x2=(-b/(2*a))
    print('phuong trinh co nghiem kep x1=x2 ',x1)
else:
    print('phuong trinh vo nghiem')
