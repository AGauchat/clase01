import random

#Usuario adivina

class HumanAgainstComputerGame(object):

    def __init__(self):
        self.is_playing = True
        self.secret_number = random.randrange(101)

    def play(self, number_user):

        if number_user > self.secret_number:
            return 'My number is smaller'

        if number_user < self.secret_number:
            return 'My number is bigger'
        
        if number_user == self.secret_number:
            self.is_playing = False
            return 'You win'


#Pc adivina

class ComputerAgainstHumanGame(object):

    def __init__(self):
        self.is_playing = True
        self.numero = 0
        self.array = []
        for i in range(1, 101):
            self.array.insert(i, i)

        self.number_us = 0
        self.select = ''



    def input_text(self):
        mitad = int((len(self.array) / 2))
        if mitad < 50 and self.select == '=':
            self.numero = mitad + self.numero
        if mitad < 50 and self.select == '-':
            self.numero = self.numero - mitad
        else:
            self.numero = self.numero + mitad
        pregunta = 'Is it your number ' + str(self.numero) + '?'
        return pregunta
        

    def play(self, rango):
        
        if rango == '+':
            for i in range(0, int(len(self.array) / 2)):
                self.array.pop(0)
            self.select = '+'

        if rango == '-':
            for i in range(int((len(self.array) / 2)), len(self.array)):
                self.array.pop(int((len(self.array) / 2)))
            self.select = '-'

        if rango == '=':
            self.is_playing = False
