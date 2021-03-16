a=float(input('nhap so a: '))
b=float(input('nhap so b: '))
c=float(input('nhap so c: '))
if a==0:
    if b==0:
        print('phuong trinh vo nghiem')
    else:
        print('phuong trinh co mot nghiem:x=',-c/b)
d=b*b-4*a*c
if d>0:
    x1=((-b-sqrt(d))/(2*a))
    x2=((-b+sqrt(d))/(2*a))
    print('phuong trinh có hai nghiem x1=',x1,'x2=',x2)
elif d==0:
    x1=x2=-b/(2*a)
    print('phuong trinh co nghiem kep x1=x2=',x1)
else:
    print('phuong trinh vo nghiem')
