# questao 2 do trabalho de estrUtura de dados TABELA HASH
class Nodo:
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla
        self.nome_estado = nome_estado
        self.proximo = None

    def __repr__(self):
        return f"{self.sigla} ({self.nome_estado})"

class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None

    def inserir_no_inicio(self, nodo):
        nodo.proximo = self.head
        self.head = nodo

    def __iter__(self):
        atual = self.head
        while atual is not None:
            yield atual
            atual = atual.proximo

    def __repr__(self):
        if self.head is None:
            return "None"
        nodos = []
        atual = self.head
        while atual is not None:
            nodos.append(atual.sigla)
            atual = atual.proximo
        return " -> ".join(nodos)

class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [ListaEncadeadaSimples() for _ in range(tamanho)]

    def funcaohash(self, chave):
        return sum(ord(c) for c in chave) % self.tamanho

    def inserir(self, sigla, nome_estado):
        posicao = self.funcaohash(sigla)
        self.tabela[posicao].inserir_no_inicio(Nodo(sigla, nome_estado))

    def imprimir(self):
        for i, lista in enumerate(self.tabela):
            print(f"Posição {i}: {lista}")


tabela_hash = TabelaHash(10)


while True:
    print('| 1 - inserir na tabela |')
    print('| 2 - listar a tabela   |')
    print('| 3 - sair              |')

    escolher = int(input('Qual função deseja: '))
    if escolher == 1:
        sigla = input('Digite a sigla do estado: ').upper()
        nome_estado = input('Digite o nome do estado: ')
        tabela_hash.inserir(sigla, nome_estado)
    elif escolher == 2:
        tabela_hash.imprimir()
    elif escolher == 3:
        print('Encerrando...')
        break
    else:
        print('Opção inválida!')

