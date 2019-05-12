from random import randint, uniform, random
from Juego import juego_adivinar

def main():
    c = 0
    numPC = randint(1000, 9999)
    numUS = 0
    ju = juego_adivinar()
    try:
        while c != 3:

            #Eleccion usuario

            print('1-Adivinar numero\n2-Pensar numero\n3-Para salir')
            c = int(input('>>'))
            if c != 1 and c != 2 and c != 3:
                print('\n ERROR [1] - Ingrese un numero válido\n')
                main()

            #Usuario adivina

            if c == 1:
                print (numPC)
                while numUS != numPC:
                    try:
                        numUS = int(input('Ingrese numero de 4 dijitos: \n>>'))
                        print('Tu numero tiene', ju.comparador(numUS, numPC)[0], ' R y ', ju.comparador(numUS, numPC)[1], ' B\n')
                        if ju.comparador(numUS, numPC)[1] == 4:
                            print('¡Numero adivinado!\n')
                    except:
                        print('ERROR [1] - Ingrese numero valido')
                        numUS = int(input('Ingrese numero de 4 dijitos: \n>>'))
                        print('Tu numero tiene', ju.comparador(numUS, numPC)[0], ' R y ', ju.comparador(numUS, numPC)[1], ' B\n')
                        if ju.comparador(numUS, numPC)[1] == 4:
                            print('¡Numero adivinado!\n')

            #PC adivina

            if c == 2:
                print('Piensa un numero del 1 al 1000')
                k = ju.juego()
                if k[0] == k[1] == k[2] == k[3]:
                    k = ''.join(str(e) for e in k)
                    print('El numero es: ', k)
                else:
                    k = ju.ordenar(k)
                    print('El numero es: ', k)


    except:
        print('\n ERROR [1] - Ingrese un numero válido\n')
        main()



main()