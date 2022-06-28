import sys

if len(sys.argv) == 3:
    nota1= float(sys.argv[1])
    nota2= float(sys.argv[2])

    if nota1 >= 7 and nota2 >= 7:
        print("promocionado")
    elif nota1 >= 4 and nota2 >=4:
        print("Aprobado , debe rendir final")
    elif (nota1<4 or nota2<4) and (not(nota1<4 and nota2<4)):
        if nota1<4 :
            print("Recupera el primero")
        else:
            print("Recupera el segundo")
    elif nota1<4 and nota2<4:
        print("Desaprobo ambos parciales , debe recursar") 
else :
    print ("Se deben ingresar parametros")   


