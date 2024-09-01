# 1) Cálculo da variável SOMA
indice = 13
soma = 0
k = 0

while k < indice:
    k = k + 1
    soma = soma + k

print(soma)


# 2) Verificação de número na sequência de Fibonacci
def pertence_a_fibonacci(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

numero = int(input("Informe um número: "))

if pertence_a_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")


# 3) Cálculo do faturamento diário
faturamento = [100, 200, 0, 300, 0, 400, 500, 0, 600, 0, 700, 800, 0, 900, 1000]

faturamento_filtrado = [dia for dia in faturamento if dia > 0]

# Calculando o menor, maior e a média mensal
menor_valor = min(faturamento_filtrado)
maior_valor = max(faturamento_filtrado)
media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

# Calculando o número de dias acima da média
dias_acima_da_media = len([dia for dia in faturamento_filtrado if dia > media_mensal])

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")


# 4) Percentual de faturamento por estado
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")


# 5) Inversão de uma string
def inverte_string(string):
    string_invertida = string[::-1]
    return string_invertida

string = input("Informe a string a ser invertida: ")
print("String invertida:", inverte_string(string))