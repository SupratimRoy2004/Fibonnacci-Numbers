n=int(input("Enter the number of elements of the fibonnacci sereis:"))
a=0
b=1
print(a, end=" ")
print(b,end=" ")
for i in range(2,n,1):
    c=a+b
    a=b
    b=c
    print(c, end=" ")
