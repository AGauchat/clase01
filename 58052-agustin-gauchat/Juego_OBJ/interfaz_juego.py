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
                            print('\n¡Numero adivinado!\n')

            #PC adivina

            if c == 2:
                print('\nPiensa un numero del 1000 al 9999\n')
                
                for i in range(0, 10):
                    print('Su numero es ', ju.descartes(), '?\n1-Si su numero es este\n2-Si el numero aparece\n0-Para saltar Numero')
                    s_n = int(input('>>'))

                    if s_n != 1 or s_n != 2:
                        pass

                    if s_n == 1:
                        print('\nSu numero es: ', ju.respuesta(s_n), '\n')
                        main()

                    if s_n == 2:
                        try:
                            c = int(input('Cuantos dijitos correctos hay?\n>>'))
                            r = int(input('Cuantos dijitos regulares hay?\n>>'))

                            ju.respuesta(r)
                            
                        except:
                            print('\nERROR [2] - Ingrese un numero válido\n')
                            c = int(input('Cuantos dijitos correctos hay?\n>>'))
                            r = int(input('Cuantos dijitos regulares hay?\n>>'))
                            ju.respuesta(c)
                
                
                s_n = 0  

                num = ju.aleatorios()

                print('\nSu numero es: ', num, '\n')
              


    except:
        print('\n ERROR [1] - Ingrese un numero válido\n')
        main()



main()