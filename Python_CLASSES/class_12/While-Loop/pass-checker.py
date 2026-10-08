i = 1

while i<=5:
    x=int(input())
    i=i+1
    if i>5:
            print("Attempt ExaustedCard Blocked")
            break
    
    elif x!=3333:
        print("Worong pin ",6-i ,"try remaining" )
    
    else : 
        print("Unlocked")
        break


while i<=5:
    x=int(input())
    i=i+1
    
    if x!=3333:
        if i>5:
            print("Attempt Exausted Card Blocked")
            break
        print("Worong pin ",6-i ,"try remaining" )
    
    else : 
        print("Unlocked")
        break
    

