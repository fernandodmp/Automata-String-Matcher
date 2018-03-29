#Aluno: Fernando de Macedo Passos
#Versao do python utilizada: 3.5.3
#Trabalho de EDA2

text_size = int(input())
#original eh o texto original e text eh o mesmo texto comecando a posicao 1
original = input()
text = ' '
text += original
pattern = input()
operation = input()
m = len(pattern)
alphabet = set()

#Funcao que percorre o texto e determina um alfabeto para aquele texto
def set_alphabet():
    for i in text:
        if(i not in alphabet):
            alphabet.add(i)

#Funcao que calcula um prefixo de tamanho k do padrao e um sufixo de tamanho q do padrao
def pref_suf(k, q):
    prefix = ''
    sufix = ''
    for aux in range(k):
        prefix += pattern[aux]
    for aux in range(q):
        sufix += pattern[aux]
    return prefix, sufix

#Funcao que gera a tabela delta para o padrao dado
def generate_table():
    table= []
    for i in range(m + 1):
        table.append([])
    for state in range(m + 1):
        for letra in alphabet:
            k = min(m + 1, state + 2)
            k -= 1
            prefix, sufix = pref_suf(k, state)
            #sufix eh um sufixo de tamanho q do padrao concatenado com um caractere adicional
            sufix += letra
            #Este loop procura o maior prefixo do padrao igual a um sufixo do padrao mais um determinad caractere
            while(sufix.endswith(prefix) == False):
                k -= 1
                prefix, sufix = pref_suf(k, state)
                sufix += letra
            #Por fim salvamos a transicao encontrada na tabela delta
            pair = [letra, k]
            table[state].append(pair)
    return table

#Funcao que percorre as transicoes do estado atual e verifica qual a mudanca de estado a ser efetuada com base no caracter recebido
def look_table(state, letra, table):
    for i in table[state]:
        if (i[0] == letra):
            return i[1]

#Funcao que busca as ocorrencias do padrao no texto e printa suas posicoes iniciais
def text_search(table):
    state = 0
    for i in range(1, text_size + 1):
        state = look_table(state, text[i], table)
        if(state == m):
            shift = i - m
            print(shift + 1)

#Funcao que percorre a tabela e a imprime no formato solicitado pelo professor
def print_table(table):
    print("Tabela Delta:")
    for state in range(m + 1):
        for par in table[state]:
            if par[1] != 0:
                Resposta = '[' + str(state) + ', ' + par[0] + ']: ' + str(par[1])
                print(Resposta)


set_alphabet()
alphabet = sorted(alphabet)
while(operation != 'e'):
    table = generate_table()
    if(operation == 's'):
        text_search(table)
    if(operation == 'u'):
        print_table(table)
    operation = input()
