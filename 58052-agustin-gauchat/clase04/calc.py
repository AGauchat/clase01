class calculadora(object):

    sumaca = 0
    num = ''
    num1 = '0'
    operador = ''
    s1 = 0

    def ingresar(self, letra):
        if letra == '+':
            self.num1 = calculadora.sum(self)
            self.num = ''
        else:
            if letra == '=':
                calculadora.display(self)
            else:
                self.num = self.num + letra
           
    def sum(self):
        s = int(self.num) + int(self.num1)
        return str(s)


    def display(self):
        
        return int(self.num) + int(self.num1)