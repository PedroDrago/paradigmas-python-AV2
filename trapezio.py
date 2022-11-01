def area_trapezio(base_maior, base_menor, altura):
    area = ((base_maior + base_menor) * altura)/2
    return area


base_maior_input = float(input('Digite digite a base maior: '))
base_menor_input = float(input('Digite digite a base menor: '))
altura_input = float(input('Digite digite a altura: '))

area = area_trapezio(base_maior_input, base_menor_input, altura_input)

print(f"A área é: {area}")