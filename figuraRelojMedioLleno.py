def figura (b,car, esp):
    for f in range (0,b):
        for c in range (0,b):
            if (f>=c and f+c>=b-1) and (f>=b-3) or f==c or f==b-1 or f==0 or f+c==b-1 or (f<=c and f+c<=b-1) and (f>=b//4) or c==(b//2) and f>=b//2 or f==0 :
            #(f<=c and f+c<=b-1) and (f>=b//3) :
            #f==c or f==b-1 or f==0 or f+c==b-1:
                print(" {}".format (car), end=" ")
            else :
                print(' '+esp,end =" ")
        print()
def main():
    b = 15
    car='*'
    esp = ' '
    figura (b,car,esp)
main()