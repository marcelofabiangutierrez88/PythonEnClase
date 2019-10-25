# def esLetra(x):
#     return (x>='a' and x<='z') or (x>='A' and x<='Z')
# def minusculaA(x):
#     res=x
#     if x>='A' and x<='Z':
#         res = chr(ord(x)+32)
#     return res
# 
# def minusculaB(xs):
#     res=""
#     for x in xs:
#         res = minusculaA(x)
#     return res
#         
# def esPalindromo(texto):
#     pal = ""
#     for c in texto:
#         if esLetra(c):
#             pal = pal + c
#     return minusculaB(pal) == minusculaB(pal[::-1])
# def main():
#     texto = "Somos o no somos"
#     if esPalindromo(texto):
#         print("true")
#     else:
#         print("false")
# main()


# def esLetra(x):
#     return (x>='a' and x<='z') or (x>='A' and x<='Z')
# 
# def minusculaA(x):
#     res=""
#     if x>='A' and x<='Z':
#         res=chr(ord(x)+32)
#     return res
# 
# def minusculaB(xs):
#     res =""
#     for x in xs:
#         res = minusculaA(x)
#     return res
# def main():
    
    


# def minCarRep(texto):
#     conCar=0
#     carMin=""
#     conCarMin=0
#     for car1 in texto:
#         conCar = 0
#         for car2 in texto:
#             if car1==car2:
#                 conCar+=1
#         if carMin !="":
#             if conCarMin > conCar:
#                 conCarMin = conCar
#                 carMin = car1
#         else:
#             conCarMin = conCar
#             carMin = car1
#     print(carMin,"->", conCarMin)
# def main():
#     minCarRep("aabbbbccdddd")
# main()


# def histograma(texto):
#     aux=""
#     for x in texto:
#         if x not in aux:
#             aux = aux+x
#     for car1 in aux:
#         conCar=0
#         for car2 in texto:
#             if car1 ==car2:
#                 conCar+=1
#         print(car1,"->", conCar)
# 
# def main():
#     histograma("aabbbbccdddd")
# main()

# def esLetra(x):
#     return x>='a' and x<='z' or x>='A' and x<='Z'
# def contarPal(texto):
#     i = 0
#     palMax=""
#     while i<len(texto) :
#         pal =""
#         while (i<len(texto)) and esLetra(texto[i]):
#             pal = pal+texto[i]
#             i+=1
#         if pal !="":
#             if palMax!="":
#                 if len(palMax) > len(texto):
#                     palMax = pal
#             else:
#                 palMax = pal
#         i+=1
#     print (palMax)
# def main():
#     contarPal("Hola 123soy m455654arcelo y tengo hambre")
# main()

