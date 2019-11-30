def operaciones(x,y):
    suma = x+y
    resta = x-y
    mult=x*y
    div =x/y
# #     if div<=0:
# #         print("resultado invalido")
# #     else:
# #         div = x/y
    return (suma,resta,mult,div)

def main():
    x=18
    y= 9
    print(x,y)
    print(operaciones(x,y))
main()