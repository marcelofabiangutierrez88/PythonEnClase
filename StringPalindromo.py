def palabraPalindroma(texto):
    cadenaInv=""
    if texto == texto[::-1]:
        print("Este String es palindromo")
    else:
        print("Este String no es palindromo")
def main():
    texto = input("Ingrese cadena a analizar: ")
    #palindromos: somos, neuquen, sos, etc.
    palabraPalindroma(texto)
main()