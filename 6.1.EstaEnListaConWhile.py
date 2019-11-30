def estaEnLaLista3(ent, lst):
    i = 0
    esta=False
    while i < len(lst):
        if ent in lst:
            esta=True
        i+=1
    return (esta)
def main():
    lst =[0,1,2,15,45]
    ent = 23
    print(ent,lst)
    print(estaEnLaLista3(ent,lst))
main()