def sqrtBi(x,eps):
    assert(x>=0)
    low=0
    high=x
    guess=(high+low)/2.0
    ctr=1

    while(abs(guess*guess-x)>eps and ctr<100):
        if(guess*guess-x>0):
            high=guess



        else: low=guess
        ctr+=1
        guess=(high+low)/2.0


    return(guess)
        
