import itertools

class juego_adivinar(object):
    
    def comparador(self, numUS, numPC):
        r = 0
        b = 0
        i = 0
        j = 0
        nUS = str(numUS)
        nPC = str(numPC)

        for i in range(i, len(str(numPC))):
            for j in range(j, len(str(numUS))):
                if nUS[j] == nPC[i]:
                    r += 1
                if nUS[j] == nPC[i] and i == j:
                    b += 1
                    r -= 1
                j += 1
            i += 1
            j = 0
        return r, b
    
    def juego(self):
        l = 0
        i = 0
        s_n = 0
        j = 0
        c = -1
        r = -1
        n = []
        for i in range(i, 10):
            
            print('Su numero es ', i, i, i, i, '?')
            try:
                s_n = int(input('1-Si su numero es este\n2-Si el numero aparece\n0-Para saltar Numero\n>>'))
            except:
                print('\nERROR [2] - Ingrese un numero válido\n')
                juego()

            if s_n == 1:
                for l in range(l,4):
                    n.insert(l, i)
                return n

            if s_n == 2:  
                try:
                    c = int(input('Cuantos dijitos correctos hay?\n>>'))
                    r = int(input('Cuantos dijitos regulares hay?\n>>'))
                except:
                    print('\nERROR [2] - Ingrese un numero válido\n')
                    juego()
                if c == 1:
                    n.insert(j, i)
                    j += 1

        return n

    def ordenar(self, numUS):
        rta = 0
        i = 0
        ult = 0
        num = ''.join(str(e) for e in numUS)
        try:
            print('Su numero es ', num, '?')
            rta = int(input('1-Si\n2-No\n>>'))
        except:
            print('\nERROR [3] - Ingrese un numero válido\n')
            ordenar(numUS)
        if rta == 1:
            return num
        else:
            for i in itertools.permutations(num):
                num = ''.join(str(e) for e in i)
                try:
                    print('Su numero es ', num, '?')
                    rta = int(input('1-Si\n2-No\n>>'))
                except:
                    print('\nERROR [3] - Ingrese un numero válido\n')
                    ordenar(numUS)
                if rta == 1:
                    return num