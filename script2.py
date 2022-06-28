


# realizar un script que imprima una palabra , una cantidad de veces pasada por parametros
# imprimir hola 5 y que me imprima hola 5

if len(sys.argv) != 3:
    print("error , necesito 2 argumento")

else:
    for i in range(int(sys.argv[2])):
        print(sys.argv[1])



 # [nombrescript , parametro1 , parametro2 ]
