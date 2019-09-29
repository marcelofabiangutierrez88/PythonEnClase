def figura (b,car,esp):
    for f in range (0,b):
        for c in range (0,b):
            if f+c>=b-1 and c<=f or f ==b//2 or c ==b-4:
            
                print(" {}".format(car), end="")
            else:
                print(' ' + esp, end="")
        print()
def main ():
    b = 7
    car = '*'
    esp = ' '
    figura(b,car,esp)
main()