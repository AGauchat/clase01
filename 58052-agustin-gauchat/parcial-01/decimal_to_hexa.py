def decimal_hexa(number):
    i = 0
    j = 0
    hexa = []
    resto = 0
    if number < 9 or number < 16: 
        if number == 10:
            lista = 'A'
        if number == 11:
            lista = 'B'
        if number == 12:
            lista = 'C'
        if number == 13:
            lista = 'D'
        if number == 14:
            lista = 'E'
        if number == 15:
            lista = 'F'
        if number < 10:
            lista = number
    else:
        for i in range(i, number-1):
            resto = int(number % 16)
            number = int(number / 16)
            if resto == 10:
                hexa.insert(i, 'A')
            if resto == 11:
                hexa.insert(i, 'B')
            if resto == 12:
                hexa.insert(i, 'C')
            if resto == 13:
                hexa.insert(i, 'D')
            if resto == 14:
                hexa.insert(i, 'E')
            if resto == 15:
                hexa.insert(i, 'F')
            if 0 < resto < 10:
                hexa.insert(i, int(resto))

        lista = reversed(hexa)
        lista = ''.join(str(e) for e in lista)
        
    return lista