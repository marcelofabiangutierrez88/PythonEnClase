def estaEnLaListaB(ent,lst):
    esta=False
    for ent in lst:
        if ent in lst:
            esta=True
    return esta
def main():
    lst=[1,2,23,4]
    ent=23
    print(ent,lst)
    print(estaEnLaListaB(ent,lst))    
main()