def estaEnLista(ent,lst):
    esta=False
    if ent in lst:
        esta=True
    return esta
def main():
    lst =[1,2,3,4]
    ent=23
    print(ent,lst)
    print(estaEnLista(ent,lst))
    
main()