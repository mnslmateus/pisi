from time import time

arquivo = open('10.txt', 'r')
todas_rotas = []
inicio = time()

def ler_dados():
    pontos = {}
    
    primeira_linha = arquivo.readline().strip()
    if not primeira_linha:
        raise ValueError('A primeira linha do arquivo está vazia.')
    
    linhas, colunas = map(int, primeira_linha.split(' '))
    
    for linha in range(linhas):
        conteudo = arquivo.readline().strip().split(' ')
        if len(conteudo) == colunas:
            for coluna in range(len(conteudo)):
                if conteudo[coluna] not in '0':
                    pontos[conteudo[coluna]] = (linha, coluna)
        else:
            raise ValueError('Inconsistência no número de colunas na linha.')
    return pontos

def permutar(pontos, i=0):
    # são obtidos todos os arranjos possiveis de n pontos sendo p = n.
    # gera todas as permutações possíveis dos pontos, garantindo que cada rota comece e termine em 'R'.
    if i == len(pontos):
        todas_rotas.append('R' + "".join(pontos) + 'R')

    for j in range(i, len(pontos)):
        rotas = [p for p in pontos]
        rotas[i], rotas[j] = rotas[j], rotas[i]
        permutar(rotas, i + 1)
    return todas_rotas

def custo_minimo(rotas, pontos):
    # recebe todas as possiveis rotas dos pontos da matriz e um dicionario com as coordenadas de cada ponto presente na matriz e retornara a rota menos custosa.
    custos_rotas = {}
    menor_custo = 10**6
    rota_menor = str
    for r in rotas:
        custo = 0
        # soma as distâncias entre cada par consecutivo de pontos
        for p in range(len(r) - 1):
            ponto_atual = r[p]
            proximo_ponto = r[p + 1]
            # distância manhattan: |x2 - x1| + |y2 - y1|
            custo += abs(pontos[proximo_ponto][0] - pontos[ponto_atual][0]) 
            custo += abs(pontos[proximo_ponto][1] - pontos[ponto_atual][1])
        # remove os 'R' das pontas para a chave do dicionário
        chave_rota = " ".join(r[1:-1])
        custos_rotas[chave_rota] = custo

    for chave, valor in custos_rotas.items():
        if valor < menor_custo:
            rota_menor = chave
            menor_custo = valor 

    return print(rota_menor)

entrada = ler_dados()
custo_minimo(permutar([p for p in entrada if p != 'R']), entrada)

fim = time()
print(fim - inicio)
