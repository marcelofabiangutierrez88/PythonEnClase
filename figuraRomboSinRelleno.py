def relleno (b, car, esp):
    for f in range (0,b):
        for c in range(0,b):
            if f+c ==b-1+(b//2) or f+c==b-1-(b//2) or f==c-(b//2) or f==c+(b//2) :
                print(" {}".format (car),end="")
            else:
                print(' ' + esp, end="")
        print()
def main():
    b = 5
    car ='*'
    esp=' '
    relleno(b,car,esp)
main()
