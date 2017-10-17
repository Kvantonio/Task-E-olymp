n = str(input())
i = 0
while n != 0:
    i = i + 1
    n = str(n)
    if len(n) == 1:
        n1 = n[0]
        n = int(n1)-int(n1)

    elif len(n) == 2:
        n1 = n[0]
        n2 = n[1]
        n = int(n)-(int(n1)+int(n2))
    
    elif len(n) == 3:
        n1 = n[0]
        n2 = n[1]
        n3 = n[2]
        n = int(n)-(int(n1)+int(n2)+int(n3))
    
    elif len(n) == 4:
        n1 = n[0]
        n2 = n[1]
        n3 = n[2]
        n4 = n[3]
        n = int(n)-(int(n1)+int(n2)+int(n3)+int(n4))
    
    elif len(n) == 5:
        n1 = n[0]
        n2 = n[1]
        n3 = n[2]
        n4 = n[3]
        n5 = n[4]
        n = int(n)-(int(n1)+int(n2)+int(n3)+int(n4)+int(n5))
    
    elif len(n) == 6:
        n1 = n[0]
        n2 = n[1]
        n3 = n[2]
        n4 = n[3]
        n5 = n[4]
        n6 = n[5]
        n = int(n)-(int(n1)+int(n2)+int(n3)+int(n4)+int(n5)+int(n6))
    
    elif len(n) == 7:
        n1 = n[0]
        n2 = n[1]
        n3 = n[2]
        n4 = n[3]
        n5 = n[4]
        n6 = n[5]
        n7 = n[6]
        n = int(n)-(int(n1)+int(n2)+int(n3)+int(n4)+int(n5)+int(n6)+int(n7))
    
    elif len(n) == 8:
        n1 = n[0]
        n2 = n[1]
        n3 = n[2]
        n4 = n[3]
        n5 = n[4]
        n6 = n[5]
        n7 = n[6]
        n8 = n[7]
        n = int(n)-(int(n1)+int(n2)+int(n3)+int(n4)+int(n5)+int(n6)+int(n7)+int(n8))
    
    elif len(n) == 9:
        n1 = n[0]
        n2 = n[1]
        n3 = n[2]
        n4 = n[3]
        n5 = n[4]
        n6 = n[5]
        n7 = n[6]
        n8 = n[7]
        n9 = n[8]
        n = int(n)-(int(n1)+int(n2)+int(n3)+int(n4)+int(n5)+int(n6)+int(n7)+int(n8)+int(n9))
print (i)
