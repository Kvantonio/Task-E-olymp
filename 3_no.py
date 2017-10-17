n = int(input())
a = 4
if n<=0:
    print(int(0))
    
elif n==1:
    print (n* 12)
    
elif n % 5 == 0:
    print (36 * (n/5))
    
else:
    print((n * 12)-((n-1)*a))
