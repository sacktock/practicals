def NumCheckouts(Num):
    Scores = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,30,32,33,34,36,38,39,40,42,45,48,50,51,54,57,60]
    x=0
    Acum=Num
    Darts = [0,0,0]
    for i in Scores:
        Acum=Num
        Acum = Acum - i
        
        if Acum == 0 and i%2 == 0 and i <= 40:
            x = x+1
        print Acum
        for j in Scores:
            if Acum<=0:
                break
            Acum = Acum - j
            if Acum == 0 and j%2 == 0 and j <= 40:
                x=x+1
            print Acum
            for k in Scores:
                if Acum<=0:
                    break
                Acum = Acum - k
                print Acum
                if Acum == 0 and k%2 == 0 and k <= 40:
                    x=x+1
                    
                
    return x
                       
            

print NumCheckouts(32)    

        
