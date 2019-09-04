import itertools

class juego_adivinar(object):

    def __init__(self):
        self.contador = -1
        self.j = 0
        self.i = 0
        self.n = []
    
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
    
    def descartes(self):
        self.contador += 1
        if self.contador > 9:
            self.contador = -1
        return str(self.contador) + str(self.contador) + str(self.contador) + str(self.contador) 

    def respuesta(self, s_n):
        n = []

        if s_n == 1:
            for l in range(0, 4):
                n.insert(l, self.contador)
            n = ''.join(str(e) for e in n)
            return n

        if s_n != 1:
            self.n.insert(self.j, self.contador)
            self.j += 1
            

    
    def aleatorios(self):
        self.n = ''.join(str(e) for e in self.n)
        rta = 0

        for i in itertools.permutations(self.n):
            self.n = ''.join(str(e) for e in i)

            try:
                print('Tu numero es: ', self.n, '?')
                rta = int(input('1- SI\n2- NO\n>> '))
            except:
                print('\nINGRESE NUMERO VALIDO\n')
                print('Tu numero es: ', self.n, '?')
                rta = int(input('1- SI\n2- NO\n>> '))

            if rta == 1:
                return self.n


