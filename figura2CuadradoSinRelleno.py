def figura(b, car, esp):
    for f in range (0,b):
        for c in range (0,b):
            if f==0 or c==0 or f==b-1 or c== :
                print(" {}".format(car),end="" )
            else:
                print(' '+esp,end="")
        print()
def main():
    b = 7
    car ='*'
    esp= ' '
    figura(b,car,esp)
main()