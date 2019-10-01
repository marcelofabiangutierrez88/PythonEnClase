def figura (b,car,esp):
    for f in range (0,b):
        for c in range (0,b):
            if (f>=b//2 and c<=b//2 and f==b//2 or c==b//2) or (f>=b//2 and c==0) or (f>=b-((b//2)+1)//2 and c<=b//2) or (f<=c and f<=b//2 and c+f <=b-1): 
                print (" {}".format (car), end="")
            else :
                print (' '+esp,end="")
        print()
def main ():
    b = 15
    car ='*'
    esp=' '
    figura(b,car,esp)
main()