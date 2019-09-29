def relleno(b,car,esp):
    for f in range(0,b):
        for c in range(0,b):
            if (c>=b-1 or f<=c) and (f>=b//2) or (c>=0 and f+c<=b-1) and (f>=b//2) or c==0 or c==b-1 or f+c==b-1 or f==c :
            #(c>=0 and f+c<=b-1) and (f>=b//2) :
            #c==0 or c==b-1 or f+c==b-1 or f==c :
                print(" {}".format (car), end="")
            else:
                print (' '+esp,end="")
        print()
        
def main():
    b=15
    car='*'
    esp=' '
    relleno(b,car,esp)
main()