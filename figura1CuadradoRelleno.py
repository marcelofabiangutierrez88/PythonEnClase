def figura (b, car, esp):
    for f in range (0,b):
        for c in range (0,b):
            if c<=f or c>=f:
                print(" {}".format(car), end="")
            else:
                print(' '+esp,end="")
        print()
def main():
    b = 4
    car ="*"
    esp = ' '
    figura(b, car, esp)
main()