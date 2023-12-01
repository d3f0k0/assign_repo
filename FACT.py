#Author: Tran Nguyen Hanh
#github.com/

n , x = map(int, input("nhap n x").split())
if n<23:
    s0 = 1
    i0 = 1
    while i0<= n:
        s0 = s0*i0
        i0= i0+1

s1 = 0
i1 = 1
while i1<= n:
    s1 = s1+(1/i1)
    i1= i1+1
    
s2 = 1
i2 = 1
while i2<= n:
    p = 1
    j = 1
    while j<= i2:
        p = p*j
        j= j+1
    s2 = s2 + (1/p)
    i2 = i2+1

s3 = 1
i3 = 1
while i3<= n:
    p = 1
    j = 1
    while j<= i3:
        p = p*j
        j= j+1
    s3 = s3 + ((x^i3)/p)
    i3 = i3+1

s4 = 1
i4 = 1
while i4<= n:
    p = 1
    j = 1
    while j<= i4:
        p = p*j
        j= j+1
    s4 = s4 + ((((-1)*x)^i4)/p)
    i4 = i4+1
    

#rounding number
rs1 = round(s1,2)
rs2 = round(s2,2)
rs3 = round(s3,2)
rs4 = round(s4,2)
    
print(s0)
print(rs1)
print(rs2)
print(rs3)
print(rs4)
