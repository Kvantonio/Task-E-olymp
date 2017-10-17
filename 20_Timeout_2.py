n = str(input())
i = 0
while n != 0:
    n = str(n)
    i = i + 1
    number = list(n) 
    a = len(number)
    n = int(n)
    if a == 1:
        n = int(number[0])-int(number[0])

    elif a == 2:
        n = n-(int(number[0])+int(number[1]))
    
    elif a == 3:
        n = n-(int(number[0])+int(number[1])+int(number[2]))
    
    elif a == 4:
        n = n-(int(number[0])+int(number[1])+int(number[2])+int(number[3]))
    
    elif a == 5:
        n = n-(int(number[0])+int(number[1])+int(number[2])+int(number[3])+int(number[4]))
    
    elif a == 6:
        n = n-(int(number[0])+int(number[1])+int(number[2])+int(number[3])+int(number[4])+int(number[5]))
    
    elif a == 7:
        n = n-(int(number[0])+int(number[1])+int(number[2])+int(number[3])+int(number[4])+int(number[5])+int(number[6]))
    
    elif a == 8:
        n = n-(int(number[0])+int(number[1])+int(number[2])+int(number[3])+int(number[4])+int(number[5])+int(number[6])+int(number[7]))
    
    elif a == 9:
        n = n-(int(number[0])+int(number[1])+int(number[2])+int(number[3])+int(number[4])+int(number[5])+int(number[6])+int(number[7])+int(number[8]))
print (i)
