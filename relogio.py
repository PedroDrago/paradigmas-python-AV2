def mostra_horas(hora, minuto, modelo):
    if modelo in 'Aa':
        relogio = f"{hora}:{minuto} AM"
    else:
        relogio = f"{hora}:{minuto} PM"

    return relogio

def converter_horas(hora, minuto, modelo):
    if modelo in 'Aa':
        hora = hora
    else:
        hora = hora - 12
    
    return mostra_horas(hora, minuto, modelo)


while True:

    hora = int(input('Hora: '))
    if hora < 0:
        break

    minuto = int(input('Minuto: '))
    modelo = str(input('AM ou PM [A/P]: '))

    print(converter_horas(hora, minuto, modelo))
