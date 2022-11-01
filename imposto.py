def soma_imposto(taxa_imposto, custo):
    imposto = taxa_imposto / 100
    custo += custo * imposto
    return custo


taxa_input = int(input('Digite a taxa de imposto do produto: '))
custo_input = float(input('DIgite o custo do produto: '))

valor_final = soma_imposto(taxa_input, custo_input)

print(f"O valor final do produto é: R${valor_final}")
