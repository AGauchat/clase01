from decimal_to_hexa import decimal_hexa

def dec_o_carac(numero):
    
    try:
        num = decimal_hexa(int(numero))
    except:
        return print('No es un numero')

    return num